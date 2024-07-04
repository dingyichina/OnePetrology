"""
    针对本应用的定制service，通过对client实现封装实现对数据的获取

    author:dingyi
    2021-12-5
"""
from myservice import client


class ScientistService:
    rootCommunityUUID = '2b78969e-1ce9-4204-a46b-9f37a64b596b'
    scientistCollectionUUID = '3eab38f6-fac7-4f63-9e54-35200dc7583d'

    #获取所有的科学家列表
    def getScientistList(self):
        return client.getCollectionItems(self.scientistCollectionUUID)

    # 得到根节点下的所有集合
    def getRootCollections(self):
        return client.getCollections(self.rootCommunityUUID)  # 根节点特藏社区的uuid


scientistService=ScientistService()