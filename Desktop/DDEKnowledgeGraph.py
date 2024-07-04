#coding=utf-8
'''
    DDE项目的知识图谱

    目标：
        封装知识图谱应用中的对象和关系

    运行环境：
        python 3.7
        py2neo   (neo4j 4.2.5)


'''

from py2neo import Graph
from py2neo.ogm import GraphObject, Property,RelatedTo, RelatedFrom
import pandas as pd

graph = Graph('http://localhost:7474', username='neo4j', password='jasmine') # 自己在http://localhost:7474登录之后修改之后的密码


class Table(GraphObject):
    __primarykey__ = 'name'

    name = Property()
    cnName = Property()  # 对应的中文名字
    mycolumns=RelatedTo('TabHeader','HAS_COLUMN')

#表头
class TabHeader(GraphObject):
    __primarykey__ = 'name'

    name = Property()
    cnName=Property()#对应的中文名字
    desc=Property()  #对于表头的描述
    alias=RelatedTo('TabHeaderAlias','ALIAS')


#表头别名
class TabHeaderAlias(GraphObject):
    __primarykey__ = 'name'
    name = Property()

#主程序入口
if __name__ == "__main__":
    df=pd.read_excel('import/岩石数据库-黄河数据.xlsx',sheet_name='锆石数据',header=0)
    t=Table().match(graph,'ZiconData').first()
    if t is None:
        t=Table()
        t.name='ZiconData'
        t.cnName='锆石数据'

    for index,s in enumerate( df.iloc[1]):
        th=TabHeader.match(graph,s).first()
        if(th is None):
            th=TabHeader()
            th.name=s
            th.cnName=df.iloc[0][index]
        t.mycolumns.add(th)

    graph.push(t)

    '''
    t=TabHeader()
    t.name="Sample"
    t.cnName='样品号'
    t.desc='野外采集的样品编号'

    graph.pull(t)
    t.name='Sample_Id'
    ta=TabHeaderAlias()
    ta.name='Sample'
    t.alias.add(ta)
    graph.push(t)
    '''