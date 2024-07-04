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
    baseUrl = "https://petrology.deep-time.org/fastapi"
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
        print("OnePetrologyRestClient init")
        self.session = requests.session()
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
    boundary="[-56.55761699999999,51.761267],[-59.326171999999985,48.789224],[-59.392089999999996,47.201377],[-56.53564499999999,47.484265],[-56.16210899999999,46.430538],[-54.71191399999998,47.111729],[-52.756348,46.430538],[-51.833496000000025,48.074868],[-52.932128999999975,48.991482],[-53.942871000000025,49.948127],[-55.12939499999999,49.607595],[-55.61279300000001,50.384443],[-56.16210899999999,50.230077],[-54.93164100000001,51.396207],[-56.55761699999999,51.761267]"
    # print(client.get_ktree())
    rtn = client.get_kdata(user_id='geowind@126.com', length=-1)
    import pandas as pd
    df = pd.DataFrame(data=rtn['data'])
    df.to_excel("d:/全球数据20240327.xlsx")
    # rtn=client.get_kdata(boundary=boundary,user_id='wangcags@126.com',length=-1)
    # print(rtn["recordsTotal"],rtn['columns'],rtn['numbercolumns'])