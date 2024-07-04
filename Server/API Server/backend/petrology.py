'''

    用 fastapi 实现的后台REST ful api

    前提： 所有的经纬度必须用 Longitude Latitude来表示，注意大小写  todo: 目前没有支持其它的方式

    丁毅

'''
import json
import sys

import numpy as np
from fastapi import FastAPI, HTTPException, Query, Form, Request
import pandas as pd
from pydantic import BaseModel

import myservice

ktree_cache = {}  # 用来缓存ktree的结构，避免返回太慢。
leaflist_cache = {}  # 用来缓存ktree所有的叶子节点，避免返回太慢或者跨函数调用

columns_cache ={}  # 全列名缓存，key是totalaql，避免需要查全集导致慢

tags_metadata = [
    {
        # name 要对应 tags 参数值
        "name": "get_ktree",
        "description": "查询某一个用户私有的知识树结构。输入参数为用户名和根节点名称（英文，不能含有非法字符）。请求格式为/ktree/{用户名}/{根节点名称}/?refresh=False ，默认不刷新，如果需要强制刷新，请使用refresh=True（速度会慢）",
    },
    {
        # name 要对应 tags 参数值
        "name": "get_kdata",
        "description": "查询数据，请求格式为/{根节点名称}/{用户名}/?skip={掠过的记录数} & limit={返回的记录数，用于分页}，如果要用于全部数据获取，可以把skip设为0，limit设置为最大数量",
    },
]

app = FastAPI(title="OnePetrology Server Backend API",
              description="用于提供OnePetrology的知识树、数据、成图等服务的集合。任何非法使用本接口的行为将被记录并追究相关责任。谢谢配合。",
              version="0.5 ",
              contact={
                  "name": "访问网站",
                  "url": "https://petrology.deep-time.org/",
                  "email": "geowind@126.com"},
              openapi_tags=tags_metadata,
              openapi_url="/fastapi/data_manager.json",
              docs_url="/fastapi/docs",
              redoc_url="/fastapi/redoc"
              )
#  得到aql对应的全部列
def getColumnList(totalaql :str):
    if totalaql not in columns_cache.keys() or columns_cache.get(totalaql) is None:
        # 此时需要去db查询，并缓存后返回
         column_list = pd.DataFrame(myservice.arango.getByAQL(totalaql)).columns.tolist()
         columns_cache[totalaql] = column_list
         print("刷新列名",totalaql)
         return column_list
    else:
        return columns_cache.get(totalaql)


# 查询ktree的结构，返回json，前端根据返回结果构造web ui
@app.get("/fastapi/ktree/{user_id}/{knode_name}", tags=["get_ktree"])
def get_ktree(user_id: str ,
                    knode_name: str,
                    refresh: bool = False):
    # 根据传入的id查找Ktree的结构，返回对应ktree的结构
    # 拼装key
    keystr = '/'.join([user_id.upper(), knode_name])

    if refresh is False and keystr in ktree_cache.keys():
        return ktree_cache.get(keystr)
    # 注意用户名被转为了大写，以实现忽略大小写的操作。  但Ktree的name不能忽略大小写，必须严格匹配。
    rtn = myservice.arango.fetchKNodeByNameAndOwner(name=knode_name, owner=user_id.upper())
    # 此处假设有且仅有一个，多余的暂时不考虑，只取第一个  todo
    if len(rtn) < 1:
        raise HTTPException(status_code=404, detail="ktree not found,please check your request parameters.")
    # 查询填充所有的子节点
    myservice.arango.getDf(rtn[0])
    # 把它放入缓存
    # 把它转换为dict ，然后放入缓存
    rtnDict = rtn[0].__dict__
    # 默认只是结点的全部叶子节点，顺序与设计顺序一致
    myleaf_list=[]
    #print(rtn[0].leaf_list)
    for x in rtn[0].leaf_list:
        myleaf_list.append(x.name)
    # 把它放在全局缓存中，供其他位置调用
    leaflist_cache[keystr] = myleaf_list
    print("更新字段缓存",myleaf_list)

    # print("所有叶子节点：", rtnDict)
    # 清除掉不必要的属性
    rtnDict.pop('df', 'no df')
    rtnDict.pop('deep_level', 'no deep_level')
    rtnDict.pop('leaf_list', 'no leaf_list')
    rtnDict.pop('df_t', 'no df_t')

    ktree_cache[keystr] = rtnDict
    return rtnDict


# 查询数据 ，暂不支持 datatable的server端 search和sort
@app.get("/fastapi/kdata/{knode_name}/{user_id}/", tags=["get_kdata"])
def get_kdata(knode_name: str,#= Query(None, max_length=100, description="有效的实体名，不能包含空格等字符"),
              user_id: str ,#= Query(None, max_length=50, regex="^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(.[a-zA-Z0-9_-]+)+$",
                            #       description="所有者的邮件，请输入有效的邮箱地址"),
              scope: str = "private",
              draw: int = Query(1, description="datatable请求的默认参数"),
              start: int = Query(0, description="分页开始的第一个记录的索引值."),
              length: int = Query(50, description="分页的记录数。如果设置为-1则不进行分页全部返回。"),
              boundary: str = Query(None, max_length=8192,
                                    description="要查询的空间边界，多边形，用坐标点的数组来表示，格式为[x1,y1],[x2,y2]...首尾点坐标重合，支持最大长度8k。"),
              # 最大8k的长度
              condition: str = Query(None, max_length=8192,
                                     description="查询条件，支持多个字段条件的组合查询。示例： c.age >=30  &&  c.name LIKE 'a%' 。具体语法遵循AQL，对象以c指代. "),
              refresh:bool=False
              ):
    totalaql = " for c in {}  filter  c.scope =='{}'  ".format(knode_name,  scope)  # 用来查询当前条件下的所有的条数
    # aql = " for c in {} limit {},{}  filter c.owner =='{}' && c.scope =='{}'  ".format(knode_name, start, length,
    #                                                                           user_id.upper(),scope)
    aql = " for c in {}  filter  c.scope =='{}'  ".format(knode_name,  scope)
    # 如果用户不是geowind@126.com，则认为是专题库，
    if user_id.upper() !="GEOWIND@126.COM":
        totalaql = totalaql + " && c.owner =='{}' ".format(user_id.upper())
        aql = aql + " && c.owner =='{}' ".format(user_id.upper())

    # if length == -1 :# 此时不进行分页
    #
    # 判断空间区域条件
    print("new get request:", totalaql)
    if boundary is None or boundary.strip(' ') == '':
        print("输入空间条件为空，不进行空间检索")
    else:
        # 根据传入的坐标点拼装查询条件
        # 例子数据 (96.328125,48.748945),(91.318359,43.644026),(102.568359,36.173357),(110.742188,43.261206),(102.392578,43.197167),(105.205078,47.457809),(96.328125,48.748945)
        points = boundary.replace('(', '[').replace(')', ']')  # 把小括号转为中括号，以适配AQL语法
        spatial_filter = " FILTER c.Longitude <=180 && c.Longitude >=-180 && c.Latitude <=90 && c.Latitude >=-90  &&  GEO_CONTAINS(GEO_POLYGON([{}]),[c.Longitude,c.Latitude]) ".format(
            points)  # 前部分的条件是为了过滤掉不合法的经纬度
        print(spatial_filter)
        totalaql = totalaql + spatial_filter  # 作为条件拼装在后面 ，多个filter属于and与的关系
        aql = aql + spatial_filter
        pass
  
    # 判断condition条件
    if condition is None or condition.strip(' ') == '':
        print("字段过滤为空，不进行条件判断")
    else:
        # 对传入的条件进行校对和 拼装
        condition_filter = " FILTER {}".format(condition)
        totalaql = totalaql + condition_filter
        aql = aql + condition_filter

    # 拼装最后的return c
    totalaql = totalaql + " return c"
    if length == -1:
        aql = aql + " return c"
    else:
        aql = aql + " limit {},{}  return c".format(start, length)
    total_count = myservice.arango.getTotolCountByAQL(totalaql)  # 查询总条数
    print("totalcount:", total_count, " ,total aql:", totalaql)
    print("aql:", aql)
    doc_list = myservice.arango.getByAQL(aql)
    df = pd.DataFrame(doc_list)
    # 为了得到全部列名，需要先查一下全部，这个方法不可取，后期再改。 todo
    # 此时需要能够把列名根据知识树的顺序进行排序，顺序与设计一致。。。 todo********

     # 暂时去掉该功能，不支持翻页

    #检查是否存在全局的叶子节点缓存
    # 拼装key
    keystr = '/'.join([user_id.upper(), knode_name])

    # 目前为了测试，每次强刷：
    if keystr not in leaflist_cache.keys()  or  leaflist_cache.get(keystr) is None:  # 不在缓存中，直接强刷一次缓存
        print(" 没有缓存，刷新一下")
        get_ktree(user_id=user_id,knode_name=knode_name,refresh=True)
    all_leaf_list = leaflist_cache.get(keystr)
    ordered_columns = []  # 按照知识树排序之后的表头
    dfcolumnlist = getColumnList(totalaql)# 用这个是为了过滤掉空值的列，即没有值的咧不需要返回
    for i in range(len(all_leaf_list)):
        if all_leaf_list[i] in dfcolumnlist:
            ordered_columns.append(all_leaf_list[i])

    # 去除掉arangodb 的默认列，不在ui上显示，公共的默认不需要显示scope
    if total_count > 0:
        df.drop(columns=["_id", "_key", "_rev", "import from"], axis="columns", inplace=True)
        # totaldf.drop(columns=["_id", "_key", "_rev", "import from"], axis="columns", inplace=True) # 暂时去掉该功能
    # 计算所有列中为字符的单独返回，便于前端计算
    numColumns = []


    for n in df.columns:
        if df[n].dtype is np.dtype('float'):  # 浮点数则添加
            numColumns.append(n)

    # 把在总的df中存在但不在当前df中存在的列添加进来
    # 暂时去掉该功能
    #for c in totaldf.columns:
    #    if c not in df.columns:
    #        df[c] = None
    return {"draw": draw,
            "recordsTotal": total_count,
            "recordsFiltered": total_count,
            "skip": start,
            "limit": length,
            "count": len(doc_list),
            "columns": ordered_columns,# df.columns.tolist(),#totaldf.columns.tolist(), # 此处返回total的字段是因为避免翻页时导致列名导致一会出现一会不出现？，为了提高效率，暂时去掉该功能,即取消分页支持，每次都取回全部数据
            "numbercolumns": numColumns,  # 允许客户端计算的字段  todo：暂未添加到post方法中
            "data": json.loads(df.to_json(orient="records", force_ascii=False))}

'''
# 查询数据 ，暂不支持 datatable的server端 search和sort
@app.post("/fastapi/data4table/{knode_name}/{user_id}/", tags=["get_kdata"])
def get_kdata(request: Request,
              knode_name: str = Query(None, max_length=100, description="有效的实体名，不能包含空格等字符"),
              user_id: str = Query(None, max_length=50, regex="^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(.[a-zA-Z0-9_-]+)+$",
                                   description="所有者的邮件，请输入有效的邮箱地址"),
              scope: str = Form(...),
              boundary: str = Form(...),
              condition: str = Form(...),
              length: int = Form(...),
              start: int = Form(...),
              draw: int = Form(...)
              ):
    print('通过requests获取参数', request.form(), scope, condition, boundary)

    # scope='private'
    # boundary = None
    # condition = None
    # length=50
    # draw = 1
    # start = 0
   
    totalaql = " for c in {}  filter c.owner =='{}' && c.scope =='{}'  ".format(knode_name, user_id.upper(),
                                                                                scope)  # 用来查询当前条件下的所有的条数
    # aql = " for c in {} limit {},{}  filter c.owner =='{}' && c.scope =='{}'  ".format(knode_name, start, length,
    #                                                                           user_id.upper(),scope)
    aql = " for c in {}  filter c.owner =='{}' && c.scope =='{}'  ".format(knode_name, user_id.upper(), scope)
    # if length == -1 :# 此时不进行分页
    #
    # 判断空间区域条件
    if boundary is None or boundary.strip(' ') == '':
        print("输入空间条件为空，不进行空间检索")
    else:
        # 根据传入的坐标点拼装查询条件
        # 例子数据 (96.328125,48.748945),(91.318359,43.644026),(102.568359,36.173357),(110.742188,43.261206),(102.392578,43.197167),(105.205078,47.457809),(96.328125,48.748945)
        points = boundary.replace('(', '[').replace(')', ']')  # 把小括号转为中括号，以适配AQL语法
        spatial_filter = " FILTER c.Longitude <=180 && c.Longitude >=-180 && c.Latitude <=90 && c.Latitude >=-90  &&  GEO_CONTAINS(GEO_POLYGON([{}]),[c.Longitude,c.Latitude]) ".format(
            points)  # 前部分的条件是为了过滤掉不合法的经纬度
        print(spatial_filter)
        totalaql = totalaql + spatial_filter  # 作为条件拼装在后面 ，多个filter属于and与的关系
        aql = aql + spatial_filter
        pass

    # 判断condition条件
    if condition is None or condition.strip(' ') == '':
        print("字段过滤为空，不进行条件判断")
    else:
        # 对传入的条件进行校对和 拼装
        condition_filter = " FILTER {}".format(condition)
        totalaql = totalaql + condition_filter
        aql = aql + condition_filter

    # 拼装最后的return c
    totalaql = totalaql + " return c"
    if length == -1:
        aql = aql + " return c"
    else:
        aql = aql + " limit {},{}  return c".format(start, length)
    total_count = myservice.arango.getTotolCountByAQL(totalaql)  # 查询总条数
    print("totalcount:", total_count, " ,total aql:", totalaql)
    print("aql:", aql)
    doc_list = myservice.arango.getByAQL(aql)
    df = pd.DataFrame(doc_list)
    # 为了得到全部列名，需要先查一下全部，这个方法不可取，后期再改。 todo
    totaldf = pd.DataFrame(myservice.arango.getByAQL(totalaql))
    # 去除掉arangodb 的默认列，不在ui上显示，公共的默认不需要显示scope
    if total_count > 0:
        df.drop(columns=["_id", "_key", "_rev", "import from"], axis="columns", inplace=True)
        totaldf.drop(columns=["_id", "_key", "_rev", "import from"], axis="columns", inplace=True)
    # 把在总的df中存在但不在当前df中存在的列添加进来
    for c in totaldf.columns:
        if c not in df.columns:
            df[c] = None
    return {"draw": draw,
            "recordsTotal": total_count,
            "recordsFiltered": total_count,
            "skip": start,
            "limit": length,
            "count": len(doc_list),
            # "columns":totaldf.columns.tolist(),
            "data": json.loads(df.to_json(orient="records", force_ascii=False))}
'''
import uvicorn


if __name__ == '__main__':
    ip = "10.15.15.191"
    port = 9001
    if len(sys.argv) != 3:
        print(" The argv must be  ip  port")

    else:
        ip = sys.argv[1]
        port = int(sys.argv[2])
    uvicorn.run(app="petrology:app", host=ip, port=port, reload=True)
