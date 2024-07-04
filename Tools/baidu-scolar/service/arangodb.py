import json

from pyArango.connection import *


import pandas as pd

'''   
  封装操作Arangodb
    
'''


class ArangoDBOper:
    conn = Connection(arangoURL='https://dde.igeodata.org/arangodb', username="dde", password="abcd1234")

    # conn = Connection(arangoURL='https://petrology.deep-time.org/arangodb', username="dde", password="abcd1234")
    def __init__(self):
        # 创建数据库
        if not self.conn.hasDatabase('dde'):
            self.conn.createDatabase(name="dde")
        self.db = self.conn['dde']
        # 创建集合
        if not self.db.hasCollection('KnowledgeNode'):
            self.db.createCollection(name='KnowledgeNode')
        self.knode_collection = self.db['KnowledgeNode']

    # 根据集合名称查询得到集合对象
    def getCollection(self, col_name):
        if not self.db.hasCollection(col_name):
            self.db.createCollection(name=col_name)
        return self.db[col_name]

    # 判断doc是否已经存在与col集合中
    def isExists(self, col, doc):
        if len(col.fetchFirstExample(doc)) == 0:
            return False
        else:
            return True

    # 往指定集合里插入doc，doc是json文档
    def insert(self, col, doc):
        col.createDocument(doc).save()

    def delete(self, col_name, sample):
        col = self.getCollection(col_name)
        query = col.fetchByExample(sample, batchSize=500)
        for doc in query:
            doc.delete()

    def fetchFromColByExample(self, col, sample, batchSize=500):
        query = col.fetchByExample(sample, batchSize, count=True)
        rtn = []
        for doc in query:
            rtn.append(doc.getStore())
        if len(rtn) > 1:
            rtn.sort(key=lambda x: x['update_time'])
        return rtn

    # 创建连接
    def insertKNode(self, k_node):
        doc = k_node.convertToJson()
        rtn = self.knode_collection.createDocument(doc).save()



    def getByAQL(self, aql):
        query = self.db.AQLQuery(aql)
        rtn = []
        for doc in query:
            rtn.append(doc.getStore())
        if len(rtn) > 1:
            rtn.sort(key=lambda x: x['update_time'])
        return rtn

    def getTotolCountByAQL(self, aql):
        totalAQL = " return count({})".format(aql)
        query = self.db.AQLQuery(totalAQL, rawResults=True)
        return query.result[0]
