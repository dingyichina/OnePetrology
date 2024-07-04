'''
    访问OnePetrology backend 服务额客户端封装

    --- by  dingyi
     2023-11-24
'''
import json
import threading

import requests


# 主体访问入口类，一个客户端应该只持有一个实例
class OnePetrologyRestClient:
    baseUrl = "https://localhost/fastapi"
    userName = ""
    password = ""
    hasInit = False
    token = ""
    authorization = ""

    _instance_lock = threading.Lock()  # 单例锁

    def __new__(cls, *args, **kwargs):
        if not hasattr(OnePetrologyRestClient, "_instance"):
            with OnePetrologyRestClient._instance_lock:
                if not hasattr(OnePetrologyRestClient, "_instance"):
                    OnePetrologyRestClient._instance = object.__new__(cls)

        return OnePetrologyRestClient._instance

    def __init__(self):
        print("OnePetrologyRestClient init");
        self.session = requests.session();
        pass

    def __repr__(self):
        return (self.baseUrl, self.userName, self.password, self.hasInit,
                self.authorization, self.headers, self.cookies)

    def get_ktree(self, knode_name:str= "Igneous_Rock", user_id:str= "geowind@126.com", refresh:bool=False):
        myurl = self.baseUrl+'/ktree/'+user_id+'/'+knode_name
        headers = {}
        params = {
            'refresh': refresh,

        }
        rep = self.session.get(myurl, headers=headers, verify=False, params=params,
                               cookies=self.session.cookies)
        if (rep.status_code == requests.codes.ok):
            #   print(json.dumps(rep.json(), indent=4, ensure_ascii=False))
            return rep.json()
        else:
            rep.raise_for_status()

    def get_kdata(self, knode_name:str= "Igneous_Rock", user_id:str= "geowind@126.com", scope:str='private',boundary:str='',draw:int=1,start:int=0,length:int=50,condition:str='',refresh:bool=False):
        myurl = self.baseUrl+'/kdata/'+knode_name+'/'+user_id
        headers = {}
        params = {
            'refresh': refresh,
            'scope':scope,
            'draw':draw,
            'start':start,
            'length':length,
            'boundary':boundary,
            'condition':condition
        }
        rep = self.session.get(myurl, headers=headers, verify=False, params=params,
                               cookies=self.session.cookies)
        if (rep.status_code == requests.codes.ok):
            #print(json.dumps(rep.json(), indent=4, ensure_ascii=False))
            return rep.json()
        else:
            rep.raise_for_status()

if __name__ == "__main__":
    client = OnePetrologyRestClient()
