'''

    本类用来操作pgsql数据库，以及实现db到类对象的转换

    author: 丁毅
    2021-12-19
'''

from sqlalchemy import Column, ForeignKey, Integer, String,Float,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine,MetaData
import uuid,random
from sqlalchemy import text
from sqlalchemy import and_
from sqlalchemy import or_

# 生成uuid
def gen_uuid():
    return uuid.uuid4().hex


Base = declarative_base()

# 知识树
class KTree(Base):
    __tablename__ = 'k_tree'
    id=Column(Integer,primary_key=True)
    uuid=Column(String(32),default=gen_uuid,nullable=False)
    name=Column(String(250),nullable=False)
    owneruserid=Column(String(32),nullable=False) # 此处uuid应该从别处带来
    rel_tree_id=Column(String(32))
    type=Column(String(20))  # 用常量类型填充
    rel_formula=Column(String(255))   # 与其他知识树的关系，用公式表示计算模式

class KNode(Base):
    __tablename__ = 'k_node'
    id=Column(Integer,primary_key=True)
    uuid=Column(String(32),default=gen_uuid,nullable=False)
    parentuuid=Column(String(32),nullable=False)  # 有且只有一个父节点。要么指向KNode，要么指向KTree
    code=Column(String(20),nullable=False)   # 代码，控制在20字符以内
    name=Column(String(32))   # 显示的名字
    type=Column(String(20))  # 用常量类型填充
    formula=Column(String(255))  # 与其他变量之间的计算关系，用code表述

class WordList(Base):
    __tablename__ = 'k_wordlist'
    id=Column(Integer,primary_key=True)
    uuid=Column(String(32),default=gen_uuid,nullable=False)
    nodeid=Column(String(32),nullable=False)
    name = Column(String(32))  # 显示的名字
    language=Column(String(10)) # 语言代码

class KValue(Base):
    __tablename__ = 'k_value'
    id = Column(Integer, primary_key=True)
    itemuuid = Column(String(32),  nullable=False)
    nodeuuid = Column(String(32), nullable=False)
    value=Column(Float)
    text = Column(Text)

class KItem(Base):
    __tablename__ = 'k_item'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(32),default=gen_uuid, nullable=False)
    ktreeuuid = Column(String(32), nullable=False)
    owneruseruuid = Column(String(32), nullable=False)

engine = create_engine('postgresql://dde:dde@localhost:{}/dde'.format(5432))

class DBOper:

    def __init__(self):
        self.DBSession = sessionmaker(bind=engine)
        self.session = self.DBSession()

    def add(self, object):
        self.session.add(object)
        self.session.commit()

    def addmany(self, objectlist):
        self.session.add_all(objectlist)
        self.session.commit()

    def filterone(self, object, filter):
        return self.session.query(object).filter(filter).first()

    def filter(self,object,filter):
        return self.session.query(object).filter(filter)

    def update(self, object, filter, updic):
        self.session.query(object).filter(filter).update(updic)
        self.session.commit()

    # 得到指定Tree所有子节点为Float 或者String类型的，也就是字段列表
    def getAllFields(self,tree_uuid):
        rtn=[]
        childList=self.filter(KNode, KNode.parentuuid == tree_uuid)
        for k in childList:
            if k.type in ["Float","String"]:  #注意大小写
                rtn.append(k)
            else:
                rtn.extend(self.getAllFields(k.uuid))
        return rtn


dbOper=DBOper()
if __name__=='__main__':
    # Base.metadata.create_all(engine)   # 只需执行一次，创建数据表

    oper=DBOper()

    '''ktree=KTree()
    ktree.name="岩浆岩"
    ktree.owneruserid=gen_uuid()
    ktree.rel_type = "知识体系根节点"

    oper.add(ktree)

    kNode=KNode()
    kNode.parentuuid="71b247bd1e4640eba7ccd100c6c05c6b"
    kNode.name="Data_Source"
    kNode.type="属性"
    kNode.code="Data_Source"
    oper.add(kNode)

    rtn=oper.filterone(KTree,KTree.id==2)

    filedList=oper.getAllFields(rtn.uuid)
    filedmap={}
    for f in filedList:
        print(f.name,"   ",f.uuid,"   ",f.type)
        filedmap[f.name]=f

    for i in range(1,100000):  # 生成10万条测试数据
        # 采用随机数 生成不同的item
        kitem=KItem()
        kitem.uuid=gen_uuid()
        kitem.ktreeuuid='68e964e6bf074e149fbb13ba0c509fd9'
        kitem.owneruseruuid="testuser"
        oper.add(kitem)

        data={
            "longitude":random.uniform(100,120),
            "latitude":random.uniform(40,65),
            "Age": random.uniform(100, 1000),
            "Data_Source":'测试数据',
            "SiO2": random.uniform(10, 100),
            "TiO2": random.uniform(10, 100),
            "Al2O3": random.uniform(10, 100),
        }
        for k in data.keys():
            kv=KValue()
            kv.itemuuid=kitem.uuid
            kv.nodeuuid=filedmap[k].uuid
            if filedmap[k].type=="Float":
                kv.value=data[k]
            else:
                kv.text=data[k]
            oper.add(kv)
        print("添加第 ",i ," 个记录")'''

    # 循环遍历所有数据
    itemList=oper.filter(KItem,KItem.ktreeuuid=="68e964e6bf074e149fbb13ba0c509fd9")
    filedList = oper.getAllFields("68e964e6bf074e149fbb13ba0c509fd9")
    for k,v in enumerate(itemList):
        row={}
        for f in filedList:
            # 多条件查询
            filter = and_(KValue.nodeuuid == f.uuid, KValue.itemuuid==v.uuid)
            temp=oper.filterone(KValue,filter)
            if temp==None:
                row[f.name] = None
                continue
            if f.type=="Float":
                row[f.name]=temp.value
            else:
                row[f.name]=temp.text
        print("当前 ",k," 条记录的数据值为",row)



