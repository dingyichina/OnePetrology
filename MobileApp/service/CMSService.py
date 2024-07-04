'''
    访问publicCMS的后台接口，获取有关数据
    ---by dingyi
    20240509
'''
import json

import requests

import urllib3

# from Model import DatabaseModel

urllib3.disable_warnings()  # 禁用ssl的警告信息
class CMService:

    def __init__(self):
        self.base_url = "https://petrology.deep-time.org"
        self.appKey = "7de76e9c-c1ca-4315-af5e-1e367eec3e33"  # 来自于publiccms的后台配置
        self.appSecret = "eff39e03-aa24-41b0-8a1d-8ad13482b15e" # 来自于publiccms的后台配置
        self.session = requests.session()
        self.getToken()

    def getToken(self):
        path = "/api/appToken?appKey={0}&appSecret={1}".format(self.appKey,self.appSecret)
        rep = self.session.get(self.base_url+path, verify=False)
        if rep.status_code == requests.codes.ok:
            print( json.dumps(json.loads(rep.content), indent=4, sort_keys=True))
            self.token = json.loads(rep.content)["appToken"]
        else:
            rep.raise_for_status()

    def getCategoryId(self,code):
        path = "/api/directive/category?appToken={0}&code={1}".format(self.token,code)
        rep = self.session.get(self.base_url+path)
        if rep.status_code == requests.codes.ok:
            # print(json.dumps(json.loads(rep.content), indent=4, sort_keys=True))
            return json.loads(rep.content)['object']["id"]
        else:
            rep.raise_for_status()

    def getContentList(self,categoryId):
        # 设置较大的pageSize =120，以实现一次性取来所有的，如果需要分页，则需要调整pageSize和pageIndex
        path = "/api/directive/contentList?appToken={0}&categoryId={1}&showParameters=true&pageSize=120".format(self.token, categoryId)
        rep = self.session.get(self.base_url + path)
        if rep.status_code == requests.codes.ok:
            # print( json.dumps(json.loads(rep.content), indent=4, sort_keys=True))
            return json.loads(rep.content)["page"]["list"]
        else:
            rep.raise_for_status()

    def getContentAttribute(self,id):
        path = "/api/method/getContentAttribute?appToken={0}&parameters={1}".format(
            self.token,id )
        rep = self.session.get(self.base_url + path)
        if rep.status_code == requests.codes.ok:
            # print(path)
            # print( json.dumps(json.loads(rep.content), indent=4, sort_keys=True))
            return json.loads(rep.content)["result"]
        else:
            rep.raise_for_status()


    # 查找专题库，返回一个专题库对象的列表
    def get_subject_list(self):
        id = self.getCategoryId("subject")
        subject_list = self.getContentList(id)
        for c in subject_list:
            c["attribute"] = self.getContentAttribute(c["id"])
            # print(c)
            # model = DatabaseModel()
        return subject_list
if __name__ == "__main__":
    cms= CMService()
    # cms.getToken()
    # id = cms.getCategoryId("subject")
    # contentlist = cms.getContentList(id)
    # for c in contentlist:
    #     print(c["id"])
    #     cms.getContentAttribute(c["id"])
    cms.get_subject_list()