

import  pandas as pd

import  geopandas as gpd
from shapely.geometry import Point,polygon

# 主程序入口
if __name__ == "__main__":
    # 判断一个点是否在ploygon列表中，如果在，则填充对应字段的值

    # 用shaply的polygon 判断point是否在其内     通过预置坐标串来构造polygon，用xy构建point即可判断

    df = pd.read_excel('database20231027.xlsx')
    for index, row in df.iterrows():
       print(row['Longitude'],row['Latitude'])