'''
    按照空间查询获取数据，根据数据对空间区域进行填图
    web性能超差，测试一下是否有更快的方法


    ----by  dingyi

'''

import pandas as pd
import numpy as np
from plotly import graph_objs as go
from shapely import geometry
import shapely.geometry as sg
from math import ceil
import re

from service.OnePetrologyClient import OnePetrologyRestClient


def split_coordinates(boundary):
    """ 从字符串中提取坐标信息。
    参数：
    s (str): 包含坐标对的字符串

    返回值：
    tuple: 包含x和y坐标的元组
    """
    x = []
    y = []
    for r in boundary.split("],["):
        rtn = r.replace('[', '').replace(']', '').split(",")
        x.append(float(rtn[0]))
        y.append(float(rtn[1]))
    return x, y


def create_polygon(x, y):
    """
    根据x和y坐标值数组，生成一个Polygon对象。

    参数：
    x (list): 包含x坐标的列表
    y (list): 包含y坐标的列表

    返回值：
    Polygon: 由给定坐标点构成的shapely Polygon对象
    """
    # 将坐标点打包成元组列表
    points = list(zip(x, y))
    # 创建并返回Polygon对象
    return geometry.Polygon(points)


class MyCell:
    pass


def create_grid(polygon, max_cells=50):
    """
    根据给定Polygon对象的边界，生成一个完全位于多边形内部的正方形网格划分。
    网格横向和纵向的最大单元数均不超过指定值。

    参数：
    polygon (shapely.geometry.Polygon): 需要划分网格的多边形区域
    max_cells (int): 单个方向上最大网格单元数，默认为100

    返回值：
    list of shapely.geometry.Polygon: 划分后的正方形网格列表
    """

    # 计算多边形的最小外接矩形并获取其宽高
    min_bound_rect = polygon.minimum_rotated_rectangle
    width = min_bound_rect.bounds[2] - min_bound_rect.bounds[0]
    height = min_bound_rect.bounds[3] - min_bound_rect.bounds[1]

    # 计算宽度和高度方向上的基本网格尺寸
    cell_width = width / max_cells if width > 0 else 0
    cell_height = height / max_cells if height > 0 else 0

    # 取较大值作为实际网格尺寸以保持正方形
    cell_size = max(cell_width, cell_height)

    # 调整实际网格数量以适应较大的维度
    cols = min(max_cells, ceil(width / cell_size))
    rows = min(max_cells, ceil(height / cell_size))

    # 初始化网格列表
    grid_polygons = []
    print("rows:", rows, "cols:", cols, "cell_size:", cell_size, "start_x:",
          polygon.minimum_rotated_rectangle.bounds[0], "start_y:", polygon.minimum_rotated_rectangle.bounds[1])
    # 遍历生成网格，并裁剪出与原始多边形相交的部分
    for row in range(rows):
        for col in range(cols):
            x_min = min_bound_rect.bounds[0] + col * cell_size
            y_min = min_bound_rect.bounds[1] + row * cell_size
            x_max = min(x_min + cell_size, min_bound_rect.bounds[2])
            y_max = min(y_min + cell_size, min_bound_rect.bounds[3])

            cell = MyCell()
            # 创建当前网格的边界框
            grid_box = sg.box(x_min, y_min, x_max, y_max)
            cell.cell = grid_box
            # 直接把单元格添加，不做筛选
            grid_polygons.append(cell)

            # # 与原始多边形进行交集操作，得到有效的网格区域
            # grid_polygon = polygon.intersection(grid_box)
            #
            # # 只添加非空且在多边形内部的网格
            # if not grid_polygon.is_empty and grid_polygon.within(polygon):
            #     grid_polygons.append(grid_polygon)

    return grid_polygons, cell_size, rows, cols, min_bound_rect.bounds[0], min_bound_rect.bounds[1]


def is_box_intersects_or_within_polygon(box_, polygon):
    """
    判断一个矩形box是否在多边形polygon内或与之相交。:


    参数：
    box_ (shapely.geometry.box): 矩形对象
    polygon (shapely.geometry.Polygon): 多边形对象

    返回值：
    bool: 如果box在polygon内或者与之相交则返回True，否则返回False
    """
    # 判断box是否在polygon内或与之相交
    return polygon.intersects(box_) or box_.within(polygon)


def extract_column_names(expression_string):
    # 假设列名仅包含字母、数字和下划线，不以数字开头
    column_name_pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
    matches = re.findall(column_name_pattern, expression_string)
    return set(matches)


def makefig_withkrige(owner="geowind@126.com", knode_name="Igneous_Rock", scope="private", boundary="", condition="",
                      calculate_field="", is_expression=False, plot_width=800, min_value=None, max_value=None, size=0.1):
    client = OnePetrologyRestClient()

    # 把坐标字符串转化为x和y的数组
    x, y = split_coordinates(boundary)
    # print(x, y)

    # 根据xy序列构造polygon对象
    polygon = create_polygon(x, y)
    # print(polygon.bounds)
    grid, cell_size, rows, cols, x_min, y_min = create_grid(polygon)  # 得到所有的grid，均等分，包括polygon外部的单元格
    print("cell_size:", cell_size, "rows:", rows, "cols:", cols, "x_min:", x_min, "y_min:", y_min)  # "grid:",grid,
    # print(grid)
    # 循环便利所有grid，如果在polygon内

    rtn = client.get_kdata(boundary=boundary, knode_name=knode_name, user_id=owner, length=-1, scope=scope,
                           condition=condition)
    # print(rtn["data"])#,rtn['columns'],rtn['numbercolumns'])

    df = pd.DataFrame(data=rtn['data'])
    # print(df.info())
    # 去除所有必须字段为空的行

    filter_field_list = ['Longitude', 'Latitude']  # 默认除了需要的字段增加经纬度，如果没有需要在程序中默认增加
    if is_expression:
        # 提取所有列名
        columns = extract_column_names(calculate_field)
        for c in columns:
            filter_field_list.append(c)
        print("过滤字段：", filter_field_list)
        df.dropna(how='any', subset=filter_field_list, inplace=True)  # 过滤字段需要从外部传入，这样可以适应不同的头图
        # 计算新的列的值
        # 首先把表达式修改为numexpr能够识别的格式
        # calc_expr = calculate_field
        # for c in columns:
        #     exp = "df['"+c+"']"
        #     calc_expr = calc_expr.replace(c, exp)
        # print("计算表达式",calc_expr)
        # print("所有列名：",df["Nd"])
        # 使用numexpr执行表达式并创建新列
        # print("columns:",df.columns,"Nd:",df['Nd'])
        df[calculate_field] = df.eval(calculate_field)  # ne.evaluate(calculate_field)
    else:
        filter_field_list.append(calculate_field)
        df.dropna(how='any', subset=filter_field_list, inplace=True)  # 过滤字段需要从外部传入，这样可以适应不同的头图

    # 筛选缩小范围
    # df = df[df['SiO2'] > 60]
    # print("筛选后：", df.shape)
    print("开始插值：")
    # 把所有的数据复制到每个grid上，原理就是如果经纬度点在grid内，则附加到grid上；如果不在，则掠过
    for index, row in df.iterrows():
        # 生成point
        point = sg.Point(row["Longitude"], row["Latitude"])
        # 遍历grid
        for mycell in grid:
            cell = mycell.cell  #
            if cell.contains(point):
                if hasattr(mycell, 'value_list'):
                    if is_expression:
                        mycell.value_list.append(
                            eval(calculate_field, row.to_dict()))  # 要勇于插值的可能是多个字段，这里需要调整为能够支持多个字段，todo，后期修改为函数
                    else:
                        mycell.value_list.append(row[calculate_field])
                else:
                    if is_expression:
                        mycell.value_list = [eval(calculate_field, row.to_dict())]
                    else:
                        mycell.value_list = [row[calculate_field]]

                break  # 一个点只会在一个cell中，找到以后就跳出
            else:
                continue
    # 已经把所有行数据附加到了grid的每个cell上
    # 现在需要计算polygon内的每个cell的值，不在其内的直接赋值none，在其内的，有value_list的则根据其内值计算平均值，没有的则使用克里金插值，构建克里金的前提是必须要在polygon内，不在其内的不参与插值计算
    for cell in grid:
        if hasattr(cell, 'value_list'):
            # 如果有值，则计算平均值
            cell.value = np.mean(cell.value_list, axis=0)
        else:
            # 如果没有值，则使用克里金插值，则暂时不处理
            pass
    x4ok = []
    y4ok = []
    z4ok = []
    # 第二次遍历，生成克里金插值需要的参数
    for cell in grid:
        if hasattr(cell, 'value'):
            # 添加到克里金插值参数列表中
            x4ok.append(cell.cell.centroid.x)
            y4ok.append(cell.cell.centroid.y)
            z4ok.append(cell.value)
    print("插值开始")
    # 生成克里金插值对象
    from pykrige.ok import OrdinaryKriging
    OK = OrdinaryKriging(x4ok, y4ok, z4ok, variogram_model='gaussian', nlags=6)
    # 第三次遍历grid，凡是不在ploygon内的，赋值None；在polygon内的，如果已经有值，则忽略；如果没有值，则计算克里金插值
    for cell in grid:
        if is_box_intersects_or_within_polygon(cell.cell, polygon):  # 有效的值
            if hasattr(cell, 'value'):
                pass
            else:
                # 插值
                zvalues, sigmasq = OK.execute(style='points', xpoints=[cell.cell.centroid.x],
                                              ypoints=[cell.cell.centroid.y], backend='loop',
                                              n_closest_points=5)  # 单独插出当前单元格的值
                cell.value = zvalues[0]  # 只有一个值
                # print(cell.value)
        else:
            cell.value = np.NAN  # 是否用None ？
    print("插值完成")
    # 现在每个cell都有值了，生成图形，根据plotly的要求拼装参数
    # x_values = [cell.centroid.x for cell in grid]
    x_values = np.linspace(start=x_min, stop=x_min + rows * cell_size, num=rows)
    y_values = np.linspace(start=y_min, stop=y_min + cols * cell_size, num=cols)
    # min_rect = polygon.minimum_rotated_rectangle
    # for i in range(0,rows,20):
    #    x_values.append(min_rect.bounds[0]+i*cell_size)
    #  y_values = [cell.centroid.y for cell in grid]
    # for i in range(0,cols,20):
    #    x_values.append(min_rect.bounds[1] + i * cell_size)

    z_values = [cell.value for cell in
                grid]  # np.array([cell.value for cell in grid]).reshape((rows, cols))  # 假设这是网格排列顺序
    # 把z_values重构为二维数组，行列分别为rows和cols
    one_dim_array = np.array(z_values)

    # 将其转化为二维数组，例如转为3x3的矩阵
    two_dim_array = one_dim_array.reshape(rows, cols)
    # print("z值：", two_dim_array)

    trace_1 = go.Contour(
        x=x_values,
        y=y_values,
        z=two_dim_array,
        colorscale='Inferno',  # 或选择其他颜色映射
        showscale=True,  # 显示颜色条
        ncontours=100,
        contours={
            "start": min_value,
            "end": max_value,  # 设置标签字体大小
            "size": size,  # 设置等值线间隔
            "showlines": False,
        },

    )

    # 设置地图布局
    layout = go.Layout(
        geo=dict(
            showland=True,  # 显示陆地
            landcolor='rgb(250, 250, 250)',  # 陆地颜色
            showcoastlines=True,  # 显示海岸线
            projection_type='mercator',  # 使用Mercator投影或其他适合经纬度的投影vv
            lonaxis=dict(range=[x_min, x_min + rows * cell_size]),  # 经度范围
            lataxis=dict(range=[y_min, y_min + cols * cell_size])  # 纬度范围
        ),
        title=dict(text=calculate_field + "  Interpolation  by krige ",
                   font=dict(  # 设置标题字体样式
                       family="Arial, sans-serif",  # 字体系列
                       size=28,  # 字体大小
                       color="crimson",  # 颜色（可以是颜色名称或RGB、RGBA等格式）
                   ),
                   x=0.5,
                   y=0.95,
                   xanchor="center",
                   yanchor="top",
                   ),
        # 假设legend占用130个像素宽，这一点可能会有细微误差 todo
        width=(plot_width-130),
        height=ceil((plot_width-130) * rows /cols),  # 注意行列数量是与常规意义反的，对应到create grid函数中

        # margin=dict(r=0, t=0, b=0, l=0),  # 调整边距
        # autosize=True,
        showlegend=True,

        xaxis=go.layout.XAxis(
            title_text="Longitude",  # 设置 X 轴标题
            title_font=dict(size=24),  # 设置标题字体大小
            tickfont=dict(size=14),  # 设置刻度标签字体大小
            showgrid=False,  # 显示网格线
            gridcolor="lightgray",  # 设置网格线颜色
            showline=True,
            linewidth=4,
            linecolor="black",
            showticklabels=True,
            showdividers=True ,
            tickcolor="black",
            tickwidth=2,
            mirror=True,
        ),
        yaxis=go.layout.YAxis(
            title_text="Latitude",  # 设置 X 轴标题
            title_font=dict(size=24),  # 设置标题字体大小
            tickfont=dict(size=14),  # 设置刻度标签字体大小
            showgrid=False,  # 显示网格线
            gridcolor="lightgray",  # 设置网格线颜色
            showline=True,
            linewidth=4,
            linecolor="black",
            showticklabels=True,
            showdividers=True,
            tickcolor="black",
            tickwidth=2,
            mirror=True,
        )
    )
    fig = go.Figure(data=[trace_1], layout=layout)

    # 生成散点图，叠加到图上
    scatter = go.Scatter(
        x=df['Longitude'].values.tolist(),
        y=df['Latitude'].values.tolist(),
        mode='markers',  # 设置为散点模式
        name='Points( {} )'.format(len(df[calculate_field].values)),  # 可选，设置trace名称
        text=df[calculate_field].values.tolist(),  # 可选，设置文本标签
        marker=dict(  # 设置标记样式（如颜色、大小等）
            color='blue',
            size=4,
            opacity=0.5
        )
    )
    fig.add_trace(scatter)
    # 配置导出为SVG格式的选项
    config = {'toImageButtonOptions': {'format': 'svg', 'filename': 'interpolation'}}
    fig.show(config=config)
    pass


if __name__ == "__main__":
    boundary = "[-54.811279,48.327876],[-54.967802,48.274891],[-55.052929,48.18524],[-55.091373,48.165093],[-55.102358,48.091763],[-54.97604,48.089929],[-55.063913,48.012817],[-55.168262,47.920867],[-55.209453,47.843503],[-55.291833,47.777098],[-55.341262,47.710609],[-55.297325,47.68103],[-55.206706,47.693973],[-55.127072,47.74017],[-55.077643,47.76233],[-54.984279,47.753098],[-54.956818,47.699519],[-54.857961,47.721696],[-54.816771,47.749404],[-54.756359,47.780789],[-54.726152,47.808466],[-54.66574,47.766022],[-54.591597,47.751251],[-54.511962,47.777098],[-54.46528,47.861933],[-54.454296,47.955827],[-54.49274,48.029351],[-54.5202,48.047715],[-54.671232,48.009142],[-54.676724,48.051388],[-54.759105,48.001792],[-54.786565,48.033024],[-54.786565,48.071579],[-54.72066,48.091763],[-54.668486,48.069744],[-54.547661,48.141272],[-54.602581,48.174252],[-54.684962,48.174252],[-54.781073,48.122941],[-54.863453,48.130275],[-54.901898,48.119274],[-54.90739,48.188903],[-54.852469,48.249293],[-54.811279,48.327876]"  # "[-55.154305,49.117441],[-55.368495,49.049983],[-55.433027,48.99595],[-55.493439,48.918401],[-55.519527,48.847961],[-55.492066,48.70044],[-55.445384,48.659637],[-55.398702,48.599733],[-55.268265,48.691376],[-55.129591,48.737588],[-55.073298,48.781042],[-54.986798,48.89132],[-54.952473,49.000455],[-54.960711,49.079676],[-55.052702,49.114744],[-55.13371,49.133617],[-55.154305,49.117441]"# "[-54.887695,48.321903],[-55.195313,48.142609],[-55.310669,48.039873],[-55.508423,47.922209],[-55.728149,47.796898],[-55.914917,47.711956],[-56.200562,47.623174],[-56.25,47.47858],[-56.085205,47.363362],[-55.678711,47.359641],[-55.371094,47.389401],[-55.316162,47.556488],[-55.112915,47.549073],[-54.744873,47.612065],[-54.398804,47.741517],[-54.321899,48.032527],[-54.492187,48.274396],[-54.656982,48.373014],[-54.887695,48.321903]"

    makefig_withkrige(owner="wangcags@126.com", boundary=boundary, calculate_field='SiO2', is_expression=False,
                      plot_width=1400)
    exit(0)