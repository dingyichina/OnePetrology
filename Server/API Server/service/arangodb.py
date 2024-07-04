import json

from pyArango.connection import *


from model.KnowledgeNode import KnowledgeNode, KNodeType
import pandas as pd

'''   
  封装操作Arangodb
    
'''


class ArangoDBOper:
    conn = Connection(arangoURL='https://localhost:8529', username="dde", password="abcd1234")


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

    # 得到所有知识结点
    def fetchAllEntity(self, owner="ROOT", skip=0, limit=20):
        query = self.knode_collection.fetchByExample({'parent': owner, "type": "ENTITY"}, batchSize=500, count=True)
        rtn = []
        for doc in query:
            k = KnowledgeNode()
            k.__dict__ = doc.getStore()
            rtn.append(k)
        if len(rtn) > 1:
            rtn.sort(key=lambda x: x.order)
        return rtn

    # 根据所有者去选择根节点
    def fetchAllKNodeByOwner(self, owner_uuid="ROOT", parent="ROOT", batchSize=500):
        query = self.knode_collection.fetchByExample({'parent': parent, 'owner': owner_uuid}, batchSize=batchSize,
                                                     count=True)
        rtn = []
        for doc in query:
            k = KnowledgeNode()
            k.__dict__ = doc.getStore()
            rtn.append(k)
        if len(rtn) > 1:
            rtn.sort(key=lambda x: x.order)
        return rtn

    # 根据名字和所有者查询是否存在
    def fetchKNodeByNameAndOwner(self, name, owner, batchSize=500):
        query = self.knode_collection.fetchByExample({'name': name, 'owner': owner}, batchSize=batchSize,
                                                     count=True)
        rtn = []
        for doc in query:
            k = KnowledgeNode()
            k.__dict__ = doc.getStore()
            rtn.append(k)
        if len(rtn) > 1:
            rtn.sort(key=lambda x: x.order)
        return rtn

    # 根据名字和所有者查询是否存在
    def fetchKNodeByNameAndOwnerAndParentid(self, name, owner, parentid, batchSize=500):
        query = self.knode_collection.fetchByExample({'name': name, 'owner': owner, "parent": parentid},
                                                     batchSize=batchSize,
                                                     count=True)
        rtn = []
        for doc in query:
            k = KnowledgeNode()
            k.__dict__ = doc.getStore()
            rtn.append(k)
        if len(rtn) > 1:
            rtn.sort(key=lambda x: x.order)
        return rtn

    # 根据uuid查询，只会返回一个
    def fetchKNodeByUUID(self, uuid, batchSize=10):
        query = self.knode_collection.fetchByExample({'uuid': uuid}, batchSize=batchSize, count=True)
        rtn = []
        for doc in query:
            k = KnowledgeNode()
            k.__dict__ = doc.getStore()
            rtn.append(k)
        if len(rtn) > 0:
            return rtn[0]  # uuid只返回第一个
        else:
            return None

    # 根据parent的uuid查询所有的children节点，默认为根节点
    def fetchChildrenKNodeByParent(self, parent_uuid='ROOT', batchSize=500):
        query = self.knode_collection.fetchByExample({'parent': parent_uuid}, batchSize=batchSize, count=True)
        rtn = []
        for doc in query:
            k = KnowledgeNode()
            k.__dict__ = doc.getStore()
            rtn.append(k)
        if len(rtn) > 1:
            rtn.sort(key=lambda x: int(x.order))
        return rtn

    # 复制一个ROOT的节点的所有下属子节点到新的用户下
    def copyChildren(self, root_parent_uuid, my_parent_uuid, owner, batchSize=500, update=False):
        import myservice
        knlist = self.fetchChildrenKNodeByParent(root_parent_uuid, batchSize=batchSize)
        myservice.logger.info("public parent uuid :{} has {} sub nodes".format(root_parent_uuid, knlist.__len__()))
        for knode in knlist:
            # 首先检查是否已存在新的
            rtnList = self.fetchKNodeByNameAndOwnerAndParentid(knode.name, owner, my_parent_uuid)
            if len(rtnList) == 0:
                # 此时不存在需要插入
                myservice.logger.info("add new sub node {}".format(knode.name))
                newKnode = KnowledgeNode()
                # 挨个复制属性值
                newKnode.name = knode.name  # 这个肯定有，不会为空
                newKnode.uuid = uuid.uuid4()
                newKnode.parent = my_parent_uuid  # 当前的子节点
                newKnode.owner = owner.upper()  # 默认所有者也是用户名的大写（为了好记，都用大写）
                if hasattr(knode, "cn_name"):
                    newKnode.cn_name = knode.cn_name
                if hasattr(knode, "desc"):
                    newKnode.desc = knode.desc
                if hasattr(knode, "type"):
                    newKnode.type = knode.type
                if hasattr(knode, "expr"):
                    newKnode.expr = knode.expr
                if hasattr(knode, "value_type"):
                    newKnode.value_type = knode.value_type
                if hasattr(knode, "rel_entity"):
                    newKnode.rel_entity = knode.rel_entity
                if hasattr(knode, "order"):
                    newKnode.order = knode.order
                # 插入到数据库
                self.insertKNode(newKnode)
                # 递归复制下一级的子节点
                self.copyChildren(knode.uuid, newKnode.uuid, owner, batchSize, update)
            else:
                myservice.logger.info("update  sub node {}".format(knode.name))

                # 此时检查是否需要复制更新
                if update:
                    # 此时用新的值更新旧的
                    for newKnode in rtnList:
                        newKnode.parent = my_parent_uuid  # 当前的子节点
                        newKnode.owner = owner.upper()  # 默认所有者也是用户名的大写（为了好记，都用大写）
                        if hasattr(knode, "cn_name"):
                            # print("复制cn_name")
                            newKnode.cn_name = knode.cn_name
                        if hasattr(knode, "desc"):
                            newKnode.desc = knode.desc
                        if hasattr(knode, "type"):
                            newKnode.type = knode.type
                        if hasattr(knode, "expr"):
                            newKnode.expr = knode.expr
                        if hasattr(knode, "value_type"):
                            newKnode.value_type = knode.value_type
                        if hasattr(knode, "rel_entity"):
                            newKnode.rel_entity = knode.rel_entity
                        if hasattr(knode, "order"):
                            newKnode.order = knode.order
                        self.updateKNode(newKnode)  # 更新完成
                # 递归复制下一级的子节点
                self.copyChildren(knode.uuid, rtnList[0].uuid, owner, batchSize, update)

    # 删除一个结点
    def deleteKNode(self, knode):
        query = self.knode_collection.fetchByExample({'uuid': knode.uuid}, batchSize=10)
        for doc in query:
            doc.delete()

    # 更新一个结点
    def updateKNode(self, knode):
        # 首先根据uuid查询到该节点，然后再对该节点进行逐个字段更新。 即除了uuid，其它字段均需要更新
        query = self.knode_collection.fetchByExample({'uuid': knode.uuid}, batchSize=50)

        for doc in query:
            if hasattr(knode, "name"):
                doc["name"] = knode.name
            if hasattr(knode, "cn_name"):
                doc["cn_name"] = knode.cn_name
            if hasattr(knode, "type"):
                doc["type"] = knode.type
            if hasattr(knode, "desc"):
                doc["desc"] = knode.desc
            if hasattr(knode, "expr"):
                doc["expr"] = knode.expr
            if hasattr(knode, "value_type"):
                doc["value_type"] = knode.value_type
            if hasattr(knode, "rel_entity"):
                doc["rel_entity"] = knode.rel_entity
            if hasattr(knode, "order"):
                doc["order"] = knode.order
            doc.save()

    # 更新某一条记录的某个字段的值，对应在界面上的一对一编辑功能
    def updateOneRecordValue(self, k_nname, field_name, key_value, value):
        from string import Template
        if value is None:
            aql = Template('UPDATE { _key: "$key" }  WITH { $field: null } IN $collection ').substitute(
                key=key_value,
                field=field_name,
                collection=k_nname)
            print("更新数据:", aql)
            self.db.AQLQuery(aql)
            return  # 直接退出

        # 判断value 类型
        if isinstance(value,str):
           aql = Template('UPDATE { _key: "$key" }  WITH { `$field`: "$value" } IN $collection ').substitute(key=key_value,
                                                                                                         field=field_name,
                                                                                                         value=value,
                                                                                                         collection=k_nname)
           print("更新数据:", aql)
           self.db.AQLQuery(aql)

        else:
           aql = Template('UPDATE { _key: "$key" }  WITH { `$field`: $value } IN $collection ').substitute(
                key=key_value,
                field=field_name,
                value=value,
                collection=k_nname)
           print("更新数据:", aql)
           self.db.AQLQuery(aql)

    # 递归得出动态设置的数据结构，只有实体entity才可以递归生成动态数据结构。
    # 去掉所有的DIR ，保留PROP 和 ENUM，并按照order进行排序，该方法主要是生成数据结构
    def getLeafList4Entity(self, k_node, rtn):
        try:
            # 递归查找children
            k_node._children = self.fetchChildrenKNodeByParent(parent_uuid=k_node.uuid)
            for k in k_node._children:
                if k.isLeaf():
                    rtn.append(k)
                else:
                    self.getLeafList4Entity(k, rtn)

        except Exception as e:
            print(e)

        return rtn

    # 递归得出动态设置的数据结构，只有实体entity才可以递归生成动态数据结构。
    # 去掉所有的DIR ，保留PROP 和 ENUM，并按照order进行排序，该方法主要是生成数据结构
    def getLeafList4Enum(self, k_node, rtn):
        try:
            # 递归查找children
            k_node._children = self.fetchChildrenKNodeByParent(parent_uuid=k_node.uuid)
            for k in k_node._children:
                k._children = self.fetchChildrenKNodeByParent(parent_uuid=k.uuid)
                if len(k._children) == 0:  # 针对枚举类型，只有下面没有子节点了，才认为是叶子结点
                    rtn.append(k)
                else:
                    self.getLeafList4Enum(k, rtn)  # 递归继续

        except Exception as e:
            print(e)

        return rtn

    # 得到从子节点到根节点的路径，自下而上
    def getLeafToParent(self, leaf, parent_node, rtn):
        if leaf.parent == parent_node.uuid:
            return
        else:
            temp = self.fetchKNodeByUUID(leaf.parent)
            rtn.append(temp)
            self.getLeafToParent(temp, parent_node, rtn)

    # entity节点传入，得到一个对应的df结构
    def getEntityDf(self, k_node):
        rtn = []
        self.getLeafList4Entity(k_node, rtn)
        deep_level = 0
        for m in rtn:
            pth = []
            self.getLeafToParent(m, k_node, pth)
            m.pth = pth
            # print([m.name, m.cn_name], len(pth))
            if (len(pth) > deep_level):
                deep_level = len(pth)
        # print("deep_level", deep_level)

        data = []
        # 二次遍历生成长短一致的series
        for m in rtn:
            se = [m.cn_name, m.name]
            # 首先把pth中的插入
            for i in m.pth:
                se.insert(0, i.name + " / " + i.cn_name)
            for j in range(0, deep_level - len(m.pth)):
                se.insert(0, None)
            # print(se)
            data.append(se)
        columns = []
        for i in range(0, deep_level + 2):
            columns.append("Column{}".format(i))
        index = []
        for i in range(0, deep_level):
            index.append("Column{}".format(i))
        df = pd.DataFrame(data=data, columns=columns)
        # df.info()
        newdf = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)  # 转置
        # 统一把需要的值附加到k_node上面
        k_node.df = newdf
        k_node.deep_level = deep_level
        k_node.leaf_list = rtn
        k_node.df_t = df
        return k_node

    # 枚举分类结点传入，得到一个对应的df结构
    def getEnumDf(self, k_node):
        rtn = []
        self.getLeafList4Enum(k_node, rtn)
        deep_level = 0
        for m in rtn:
            pth = []
            self.getLeafToParent(m, k_node, pth)
            m.pth = pth
            # print([m.name, m.cn_name], len(pth))
            if (len(pth) > deep_level):
                deep_level = len(pth)
        # print("deep_level", deep_level)
        data = []
        # 二次遍历生成长短一致的series，后补齐
        for m in rtn:
            se = [m.cn_name, m.name]
            # 首先把pth中的插入
            for i in m.pth:
                se.insert(0, i.name + " / " + i.cn_name)
            for j in range(0, deep_level - len(m.pth)):
                se.append(None)
            # print(se)
            data.append(se)
        columns = []
        for i in range(0, deep_level + 2):
            columns.append("Column{}".format(i))
        index = []
        for i in range(0, deep_level):
            index.append("Column{}".format(i))
        df = pd.DataFrame(data=data, columns=columns)
        # df.info()
        newdf = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)  # 转置
        # 统一把需要的值附加到k_node上面
        k_node.df = newdf
        k_node.deep_level = deep_level
        k_node.leaf_list = rtn
        k_node.df_t = df
        return k_node

    def getDf(self, k_node):
        if k_node.type == KNodeType.CLASSIFY.value:  # 只有枚举类型单独处理
            return self.getEnumDf(k_node)
        else:
            return self.getEntityDf(k_node)

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
