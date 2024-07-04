'''

    知识结点

'''

from enum import Enum, unique


# 结点类型


@unique
class KNodeType(Enum):
    ENTITY = "ENTITY"
    DIR = "DIR"
    PROP = "PROP"
    CLASSIFY = "CLASSIFY"


# 值类型
@unique
class ValueType(Enum):
    STRING = "String"
    FLOAT = "Float"
    ENUM = "Enum"
    RELATION = "RELATION"  # 枚举类型，当关联关系不对时，默认当作描述性类型String来处理


# 知识结点，用来定义数据结构的，力争和知识体系相关
class KnowledgeNode:

    def __init__(self):
        self._children = []  # 初始化为空列表
        self.order = 0  # 默认order 为整数
        pass

    def __init__(self, **entries):
        self._children = []  # 初始化为空列表
        self.order = 0  # 默认order 为整数
        self.__dict__.update(entries)

    def __repr__(self):
        return (self.uuid, self.name, self.cn_name, self.desc, self.type, self.expr, self.value_type, self.rel_entity,
                self.order, self.owner, self.parent)  #, self._children)

    def convertToJson(self):
        return {
            "uuid": self.uuid,
            "name": self.name,
            "cn_name": self.cn_name,
            "desc": self.desc,
            "type": self.type,
            "expr": self.expr,
            "value_type": self.value_type,
            "rel_entity": self.rel_entity,
            "order": self.order,
            "owner": self.owner,
            "parent": self.parent
        }


    # 判断是否需要赋值的叶子节点
    def isLeaf(self):
        if self.type in [KNodeType.PROP.value, KNodeType.CLASSIFY.value]:
            return True
        else:
            return False

