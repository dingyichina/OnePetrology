'''

    在这里定义一些对象模型，在其它地方引用

    dingyi
    2024-05014

'''
import json

from service import client, cms


# 与CMS系统中保持一致的数据库模型(包含专题库）
class DatabaseModel:

    def __init__(self,title,author,description,cover,owner,knode="Igneous_Rock",scope="private",extent=None,custom_map=None,show_global=True,html=None):
        self.title = title
        self.author = author
        self.description = description
        self.cover = cover
        self.owner = owner
        self.knode = knode
        self.scope = scope
        self.extent = extent
        self.custom_map = custom_map
        self.show_global = show_global
        self.html = html
        self.total_count = 0
        self.field_list = []
        # # 从服务器端获取数据量
        # self.get_info()

    def from_json(self,json_str):
        self.__init__(title=json_str['title'], author=json_str['author'], description=json_str['description'],
                      cover="https://petrology.deep-time.org/" + json_str['cover'],
                      owner=json_str['attribute']['owner'], knode=json_str['attribute']['k_node'],
                      scope=json_str['attribute']['scope'], extent=json_str['attribute']['extent'],
                      html=json_str['attribute']['text'])

        if hasattr(json_str['attribute'],"custom_map"):
            self.custom_map = json_str['attribute']['custom_map']
        if hasattr(json_str['attribute'],"show_global"):
            self.show_global = json_str['attribute']['show_global']
        return self

    # 访问服务器获取数据量，字段列表等信息
    def get_info(self):
        rtn = client.get_kdata(knode_name=self.knode, user_id=self.owner, scope=self.scope, boundary=self.extent, draw=1, start=0)
        self.total_count = rtn['recordsTotal']
        self.field_list = rtn['columns']
        # print(self.field_list)
        return self
        pass

# 系统模型类，把所有需要初始化的地方都放在这里
class SysModel:
    pass

def build_sys_model():
    sys_model = SysModel()
    sys_model.major_database = DatabaseModel("Igneous rock map of the world", "Dingyi", "This is a map of the world",
                              "/images/worldmap.gif", "geowind@126.com")
    sys_model.major_database.get_info()
    sys_model.subject_database_list=[]
    list = cms.get_subject_list()
    for l in list:
        model = DatabaseModel("Igneous rock map of the world", "Dingyi", "This is a map of the world",
                              "/images/worldmap.gif", "geowind@126.com").from_json(l)
        # print(model)
        model.get_info()
        sys_model.subject_database_list.append(model)
    return sys_model