# -*- coding:utf-8 -*-
'''*****************************************************************
    本程序用以访问Dspace系统的Rest api
    根据
    version：dspace v7
    Author: dingyi
********************************************************************
'''
import sys

import requests, json, warnings, threading

from requests_toolbelt.multipart import encoder

warnings.filterwarnings('ignore')


# Dspace Rest API的客户端类

# 返回值对象
class ReturnObject:
    def __repr__(self):
        return (self._embedded, self._links, self.page)


# 搜索结果对象
class SearchResult:
    def __repr__(self):
        return (self.searchResult, self.facets)


# Community对象
class Community:
    def __repr__(self):
        return (self.id, self.uuid, self.name, self.handle, self.metadata, self.type, self._links)

    def getSelfLink(self):
        return self._links['self']['href']

    def getSubCommunitiesLink(self):
        return self._links['subcommunities']['href']

    def getParentCommunityLink(self):
        return self._links['parentCommunity']['href']

    def getCollectionsLink(self):
        return self._links['collections']['href']

    def getLogoLink(self):
        return self._links['logo']['href']

    def getAdminGroupLink(self):
        return self._links['adminGroup']['href']


# Collection
class Collection:
    def __repr__(self):
        return (self.id, self.uuid, self.name, self.handle, self.metadata, self.type, self._links)

    def getSelfLink(self):
        return self._links['self']['href']

    def getHarvesterLink(self):
        return self._links['harvester']['href']

    def getItemTemplateLink(self):
        return self._links['itemtemplate']['href']

    def getLicenseLink(self):
        return self._links['license']['href']

    def getLogoLink(self):
        return self._links['logo']['href']

    def getMappedItemsLink(self):
        return self._links['mappedItems']['href']

    def getParentCommunityLink(self):
        return self._links['parentCommunity']['href']

    def getAdminGroupLink(self):
        return self._links['adminGroup']['href']

    def getSubmittersGroupLink(self):
        return self._links['submittersGroup']['href']

    def getItemReadGroupLink(self):
        return self._links['itemReadGroup']['href']

    def getBitstreamReadGroupLink(self):
        return self._links['bitstreamReadGroup']['href']

    def getWorkflowGroups(self):  # 返回工作流数组
        return self._links['workflowGroups']


# 条目，这个和之前版本不同，与entity合并在了一起
class Item:
    def __repr__(self):
        return (
        self.id, self.uuid, self.name, self.handle, self.metadata, self.inArchive, self.discoverable, self.withdrawn,
        self.lastModified, self.entityType, self.type, self._links)

    def getSelfLink(self):
        return self._links['self']['href']

    def getThumbnailLink(self):
        return self._links['thumbnail']['href']

    def getTemplateItemOfLink(self):
        return self._links['templateItemOf']['href']

    def getVersionLink(self):
        return self._links['version']['href']

    def getRelationshipsLink(self):
        return self._links['relationships']['href']

    def getOwningCollectionLink(self):
        return self._links['owningCollection']['href']

    def getMappedCollectionsLink(self):
        return self._links['mappedCollections']['href']

    def getBundlesLink(self):
        return self._links['bundles']['href']


# bundle
class Bundle:
    def __repr__(self):
        return (self.uuid, self.name, self.handle, self.metadata, self.type, self._links)

    def getSelfLink(self):
        return self._links['self']['href']

    def getItemLink(self):
        return self._links['item']['href']

    def getBitstreamsLink(self):
        return self._links['bitstreams']['href']

    def getPrimaryBitstreamsLink(self):
        return self._links['primaryBitstream']['href']


# bitstream
class Bitstream:
    def __repr__(self):
        return (
        self.id, self.uuid, self.name, self.handle, self.metadata, self.bundleName, self.sizeBytes, self.checkSum,
        self.sequenceId, self.type, self._links)

    def getSelfLink(self):
        return self._links['self']['href']

    def getContentLink(self):
        return self._links['content']['href']

    def getBundleLink(self):
        return self._links['bundle']['href']

    def getFormatLink(self):
        return self._links['format']['href']

    def getThumbnailLink(self):
        return self._links['thumbnail']['href']


# 实体，自定义对象，这个是7之后引入的特色功能
class EntityType:
    def __repr__(self):
        return (self.id, self.label, self.type, self._links)

    def getRelationshiptypesLink(self):
        return self._links['relationshiptypes']['href']

    def getSelfLink(self):
        return self._links['self']['href']



def upload_monitor(monitor):
    print(round(monitor.bytes_read/monitor.len*100,2))


# 主体访问入口类，一个客户端应该只持有一个实例
class DspaceRestClient:
    baseUrl = "https://petrology.deep-time.org/server2/api"
    userName = ""
    password = ""
    hasInit = False
    token = ""
    authorization = ""

    _instance_lock = threading.Lock()  # 单例锁

    def __new__(cls, *args, **kwargs):
        if not hasattr(DspaceRestClient, "_instance"):
            with DspaceRestClient._instance_lock:
                if not hasattr(DspaceRestClient, "_instance"):
                    DspaceRestClient._instance = object.__new__(cls)

        return DspaceRestClient._instance

    def __init__(self):
        print("DspaceRestClient init");
        self.session = requests.session();
        pass

    def __repr__(self):
        return (self.baseUrl, self.userName, self.password, self.hasInit,
                self.authorization, self.headers, self.cookies)

    # 得到token
    def getToken(self):
        rep = self.session.get(self.baseUrl, verify=False)
        if rep.status_code == requests.codes.ok:
            self.token = rep.headers.get('DSPACE-XSRF-TOKEN')
        else:
            rep.raise_for_status()
    # 根据返回的header刷新本地缓存的token和Authorization
    def refreshTokenByHeader(self,repHeader):
        token = repHeader.get('DSPACE-XSRF-TOKEN')
        if token != None:
            self.token = token
        authorization = repHeader.get('Authorization')
        if authorization!=None:
            self.authorization=authorization

    # 登陆
    def login(self, user, password):
        if len(self.token) == 0:
            self.getToken()
        path = "/authn/login"
        data = {
            'user': user,
            'password': password
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", 'X-XSRF-TOKEN': self.token}
        rep = self.session.post(self.baseUrl + path, data=data, headers=headers, verify=False,
                                cookies=self.session.cookies)
        self.refreshTokenByHeader(rep.headers)
        if (rep.status_code == requests.codes.ok):
            # print(rep.headers)
            # print(rep.content)
            pass
        else:
            print(rep.headers)
            print(rep.content)
            rep.raise_for_status()

    # 得到Communities列表,page为页码，从0开始，默认的每页size为20
    def getCommunities(self, page=0, size=20):
        rtnList = []
        path = "/core/communities"
        headers = {'X-XSRF-TOKEN': self.token, 'Authorization': self.authorization}
        params = {
            'page': page,
            'size': size
        }
        rep = self.session.get(self.baseUrl + path, headers=headers, params=params, verify=False,
                               cookies=self.session.cookies)
        self.refreshTokenByHeader(rep.headers)
        if (rep.status_code == requests.codes.ok):
            rto = ReturnObject()
            rto.__dict__ = rep.json()
            # todo:此处获得了page的参数之后，需要判断是否需要翻页并发起进一步的请求
            # print(rto.page)
            if (rto.page['totalPages'] - 1) > page:  # 没有到最后一页，循环调用
                rtnList += (self.getCommunities(page + 1, size))
            # print(json.dumps(rto._embedded, indent=4, ensure_ascii=False))
            for i in rto._embedded['communities']:
                myComunity = Community()
                myComunity.__dict__ = i
                rtnList.append(myComunity)

            return rtnList
        else:
            print(rep.headers)
            print(rep.content)
            rep.raise_for_status()

    # 根据uuid获得指定的Community
    def getCommunity(self, uuid):
        path = "/core/communities/" + uuid
        headers = {'X-XSRF-TOKEN': self.token, 'Authorization': self.authorization}

        rep = self.session.get(self.baseUrl + path, headers=headers, verify=False,
                               cookies=self.session.cookies)
        self.refreshTokenByHeader(rep.headers)
        if (rep.status_code == requests.codes.ok):
            myComunity = Community()
            myComunity.__dict__ = rep.json()
            return myComunity
        else:
            print(rep.headers)
            print(rep.content)
            rep.raise_for_status()

    # 根据uuid得到Collection
    def getCollectionByUuid(self, uuid):
        path = "/core/collections/" + uuid
        headers = {'X-XSRF-TOKEN': self.token, 'Authorization': self.authorization}

        rep = self.session.get(self.baseUrl + path, headers=headers, verify=False,
                               cookies=self.session.cookies)
        self.refreshTokenByHeader(rep.headers)
        if (rep.status_code == requests.codes.ok):
            myCollection = Collection()
            myCollection.__dict__ = rep.json()
            return myCollection
        else:
            print(rep.headers)
            print(rep.content)
            rep.raise_for_status()

    #通过url得到id
    def getItemByUrl(self,url):

        headers = {'X-XSRF-TOKEN': self.token, 'Authorization': self.authorization}

        rep = self.session.get(url, headers=headers, verify=False,
                               cookies=self.session.cookies)
        self.refreshTokenByHeader(rep.headers)
        if (rep.status_code == requests.codes.ok):
            myItem = Item()
            myItem.__dict__ = rep.json()
            return myItem
        else:
            print(rep.headers)
            print(rep.content)
            rep.raise_for_status()
        # 根据uuid获得指定的Community

    # 根据uuid获得指定的Community
    def getItem(self, uuid):
        path = "/core/items/" + uuid
        return self.getItemByUrl(self.baseUrl + path)

        # 根据uuid获得指定的Community

    def getBundle(self, uuid):
        path = "/core/bundles/" + uuid
        headers = {'X-XSRF-TOKEN': self.token, 'Authorization': self.authorization}

        rep = self.session.get(self.baseUrl + path, headers=headers, verify=False,
                               cookies=self.session.cookies)
        self.refreshTokenByHeader(rep.headers)
        if (rep.status_code == requests.codes.ok):
            myBundle = Bundle()
            myBundle.__dict__ = rep.json()
            return myBundle
        else:
            print(rep.headers)
            print(rep.content)
            rep.raise_for_status()

    # 根据传入的url调取子community
    def getSubCommunities(self, url, page=0, size=20):
        rtnList = []
        headers = {'X-XSRF-TOKEN': self.token, 'Authorization': self.authorization}
        params = {
            'page': page,
            'size': size
        }
        rep = self.session.get(url, headers=headers, verify=False, params=params,
                               cookies=self.session.cookies)
        self.refreshTokenByHeader(rep.headers)
        if (rep.status_code == requests.codes.ok):
            rto = ReturnObject()
            rto.__dict__ = rep.json()
            # todo:此处获得了page的参数之后，需要判断是否需要翻页并发起进一步的请求
            # print(rto.page)
            if (rto.page['totalPages'] - 1) > page:  # 没有到最后一页，循环调用
                rtnList += (self.getSubCommunities(url, page + 1, size))
            # print(json.dumps(rto._embedded, indent=4, ensure_ascii=False))
            for i in rto._embedded['subcommunities']:
                myComunity = Community()
                myComunity.__dict__ = i
                rtnList.append(myComunity)
            return rtnList
        else:
            print(rep.headers)
            print(rep.content)
            rep.raise_for_status()

    # 根据communityId获取下属所有的集合
    def getCollections(self,communityId):
        path="/core/communities/"+communityId+ "/collections"
        return self.getCollectionsByUrl(self.baseUrl+path)

    # 根据传入的url调取集合
    def getCollectionsByUrl(self, url):
        rtnList = []
        headers = {'X-XSRF-TOKEN': self.token, 'Authorization': self.authorization}
        rep = self.session.get(url, headers=headers, verify=False,
                               cookies=self.session.cookies)
        self.refreshTokenByHeader(rep.headers)
        if (rep.status_code == requests.codes.ok):
            # print(rep.headers)
            # print(rep.content)
            rto = ReturnObject()
            rto.__dict__ = rep.json()
            # todo:此处获得了page的参数之后，需要判断是否需要翻页并发起进一步的请求 ,代码暂缺，会忽略掉后面的
            # print(json.dumps(rto._embedded, indent=4, ensure_ascii=False))
            for i in rto._embedded['collections']:
                myCollection = Collection()
                myCollection.__dict__ = i
                rtnList.append(myCollection)
            return rtnList
        else:
            print(rep.headers)
            print(rep.content)
            rep.raise_for_status()

    # 得到所有的实体类型
    def getEntityTypes(self, page=0, size=20):
        rtnList = []
        path = "/core/entitytypes"
        headers = {'X-XSRF-TOKEN': self.token, 'Authorization': self.authorization}
        params = {
            'page': page,
            'size': size
        }
        rep = self.session.get(self.baseUrl + path, headers=headers, params=params, verify=False,
                               cookies=self.session.cookies)
        self.refreshTokenByHeader(rep.headers)
        if (rep.status_code == requests.codes.ok):
            # print(rep.headers)
            # print(rep.content)
            rto = ReturnObject()
            rto.__dict__ = rep.json()
            # print(json.dumps(rto._embedded, indent=4, ensure_ascii=False))
            # todo:此处获得了page的参数之后，需要判断是否需要翻页并发起进一步的请求
            # print(rto.page)
            if (rto.page['totalPages'] - 1) > page:  # 没有到最后一页，循环调用
                rtnList += (self.getEntityTypes(page + 1, size))

            for i in rto._embedded['entitytypes']:
                myEntityType = EntityType()
                myEntityType.__dict__ = i
                rtnList.append(myEntityType)
            return rtnList
        else:
            print(rep.headers)
            print(rep.content)
            rep.raise_for_status()

    # 根据Collections的uuid得到其下属的items
    def getCollectionItems(self, uuid, page=0, size=20):
        rtnList = []
        path = "/discover/search/objects"
        headers = {'X-XSRF-TOKEN': self.token, 'Authorization': self.authorization}
        params = {
            'page': page,
            'size': size,
            'dsoType': 'item',
            'scope': uuid
        }

        rep = self.session.get(self.baseUrl + path, headers=headers, params=params, verify=False,
                               cookies=self.session.cookies)
        self.refreshTokenByHeader(rep.headers)
        if (rep.status_code == requests.codes.ok):
            # print(rep.headers)
            # print(rep.content)
            searchResult = SearchResult()
            searchResult.__dict__ = rep.json()['_embedded']
            rto = ReturnObject()
            rto.__dict__ = searchResult.searchResult
            # print(json.dumps(rto._embedded, indent=4, ensure_ascii=False))
            # todo:此处获得了page的参数之后，需要判断是否需要翻页并发起进一步的请求
            # print(rto.page)
            if (rto.page['totalPages'] - 1) > page:  # 没有到最后一页，循环调用
                rtnList += (self.getCollectionItems(uuid, page + 1, size))

            for i in rto._embedded['objects']:
                myItem = Item()
                myItem.__dict__ = i['_embedded']['indexableObject']
                rtnList.append(myItem)
            return rtnList
        else:
            print(rep.headers)
            print(rep.content)
            rep.raise_for_status()

    # 根据Collections的uuid得到其下属的items
    def getCollectionItemsByScientist(self, collection_uuid, scientistName, page=0, size=20):
                rtnList = []
                path = "/discover/search/objects"
                headers = {'X-XSRF-TOKEN': self.token, 'Authorization': self.authorization}
                params = {
                    'page': page,
                    'size': size,
                     'dsoType': 'item',
                    'scope': collection_uuid,
                    "f.dcScientistName": scientistName + ',query' ,   #这个是配置在服务端的discovery中，只能用于查询非科学家集合的其它集合
                    #"sort":"dateissued,desc"
                }

                rep = self.session.get(self.baseUrl + path, headers=headers, params=params, verify=False,
                                       cookies=self.session.cookies)
                self.refreshTokenByHeader(rep.headers)
                if (rep.status_code == requests.codes.ok):
                    # print(rep.headers)
                    # print(rep.content)
                    searchResult = SearchResult()
                    searchResult.__dict__ = rep.json()['_embedded']
                    rto = ReturnObject()
                    rto.__dict__ = searchResult.searchResult
                    # print(json.dumps(rto._embedded, indent=4, ensure_ascii=False))
                    # todo:此处获得了page的参数之后，需要判断是否需要翻页并发起进一步的请求
                    # print(rto.page)
                    if (rto.page['totalPages'] - 1) > page:  # 没有到最后一页，循环调用
                        rtnList += (self.getCollectionItemsByScientist(collection_uuid,scientistName, page + 1, size))

                    for i in rto._embedded['objects']:
                        myItem = Item()
                        myItem.__dict__ = i['_embedded']['indexableObject']
                        rtnList.append(myItem)
                    return rtnList
                else:
                    print(rep.headers)
                    print(rep.content)
                    rep.raise_for_status()
                # 根据Collections的uuid得到其下属的items

    def getCollectionItemsByFilter(self, collection_uuid, filter, scientistName, page=0, size=20):
        rtnList = []
        path = "/discover/search/objects"
        headers = {'X-XSRF-TOKEN': self.token, 'Authorization': self.authorization}
        params = {
            'page': page,
            'size': size,
            'dsoType': 'item',
            'scope': collection_uuid,
            "f."+filter: scientistName + ',contains',  # 这个是配置在服务端的discovery中，只能用于查询非科学家集合的其它集合
            # "sort":"dateissued,desc"
        }

        rep = self.session.get(self.baseUrl + path, headers=headers, params=params, verify=False,
                               cookies=self.session.cookies)
        self.refreshTokenByHeader(rep.headers)
        if (rep.status_code == requests.codes.ok):
            # print(rep.headers)
            # print(rep.content)
            searchResult = SearchResult()
            searchResult.__dict__ = rep.json()['_embedded']
            rto = ReturnObject()
            rto.__dict__ = searchResult.searchResult
            # print(json.dumps(rto._embedded, indent=4, ensure_ascii=False))
            # todo:此处获得了page的参数之后，需要判断是否需要翻页并发起进一步的请求
            # print(rto.page)
            if (rto.page['totalPages'] - 1) > page:  # 没有到最后一页，循环调用
                rtnList += (self.getCollectionItemsByScientist(collection_uuid, page + 1, size))

            for i in rto._embedded['objects']:
                myItem = Item()
                myItem.__dict__ = i['_embedded']['indexableObject']
                rtnList.append(myItem)
            return rtnList
        else:
            print(rep.headers)
            print(rep.content)
            rep.raise_for_status()
    # 根据itemuuid对应的item得到对应的所有bundle，然后检查是否有和它重名的
    def isBundleExists(self,itemuuid,bundleName):
        for b in self.getItemBundles(self.getItem(itemuuid).getBundlesLink()):
            if b.name==bundleName:
                return True
        return False
    # 得到指定名字的bundle
    def getItemBundle(self,itemuuid,bundleName):
        for b in self.getItemBundles(self.getItem(itemuuid).getBundlesLink()):
            if b.name==bundleName:
                return b


    # 通过item获得的bundle的链接
    def getItemBundles(self, url):
        rtnList = []
        headers = {'X-XSRF-TOKEN': self.token, 'Authorization': self.authorization}
        rep = self.session.get(url, headers=headers, verify=False,
                               cookies=self.session.cookies)
        self.refreshTokenByHeader(rep.headers)
        if (rep.status_code == requests.codes.ok):
            # print(rep.headers)
            # print(rep.content)
            rto = ReturnObject()
            rto.__dict__ = rep.json()
            # todo:此处获得了page的参数之后，需要判断是否需要翻页并发起进一步的请求 ,代码暂缺，会忽略掉后面的
            # print(json.dumps(rto._embedded, indent=4, ensure_ascii=False))
            for i in rto._embedded['bundles']:
                myBundle = Bundle()
                myBundle.__dict__ = i
                rtnList.append(myBundle)
            return rtnList
        else:
            print(rep.headers)
            print(rep.content)
            rep.raise_for_status()

    def getBitstreams(self, url):
        rtnList = []
        headers = {'X-XSRF-TOKEN': self.token, 'Authorization': self.authorization}
        rep = self.session.get(url, headers=headers, verify=False,
                               cookies=self.session.cookies)
        self.refreshTokenByHeader(rep.headers)
        if (rep.status_code == requests.codes.ok):
            # print(rep.headers)
            # print(rep.content)
            rto = ReturnObject()
            rto.__dict__ = rep.json()
            # todo:此处获得了page的参数之后，需要判断是否需要翻页并发起进一步的请求 ,代码暂缺，会忽略掉后面的
            # print(json.dumps(rto._embedded, indent=4, ensure_ascii=False))
            for i in rto._embedded['bitstreams']:
                myBitstream = Bitstream()
                myBitstream.__dict__ = i
                rtnList.append(myBitstream)
            return rtnList
        else:
            print(rep.headers)
            print(rep.content)
            rep.raise_for_status()
        pass

    # 创建bundle，默认的BUNDLE有ORIGINAL，LICENSE，THUMBNAIL，其余还有一个EXTRA，用来存储其它信息  。返回的是创建成功的对象
    def createBundle(self, itemuuid, bundlename):
        data = {
            "name": bundlename,
            "metadata": {}
        }
        path = "/core/items/" + itemuuid + "/bundles"
        headers = {
            "Accept": "application/hal+json, application/json, */*; q=0.01",
            "Content-Type": "application/json", 'X-XSRF-TOKEN': self.token,
            'Connection': 'keep - alive',
            'Authorization': self.authorization}
        rep = self.session.post(self.baseUrl + path, json=data, headers=headers, verify=False,
                                cookies=self.session.cookies)
        self.refreshTokenByHeader(rep.headers)
        if (rep.status_code == requests.codes.created):
            # print(rep.headers)
            # print(rep.content)
            rtn=Bundle()
            rtn.__dict__=rep.json()
            return  rtn
            pass
        else:
            print(rep.headers)
            print(rep.content)
            rep.raise_for_status()

    # 创建一个bitstream对象 注意： 文件名的后缀一定要带着，后台会自动区分类型。如果没有类型，则生成缩略图会失败。
    def createBitstream(self, bundleuuid, filename, filepath, callback=None):
        multipart_encoder = encoder.MultipartEncoder(
            fields={
                'file': (filename, open(filepath, 'rb'), 'application/pdf')  # 根据上传文件类型的不同而不同，这里给出了一个默认的。前置的file,为了和后台呼应。如果格式不对，后台不接受。
            },
        )
        monitor = encoder.MultipartEncoderMonitor(multipart_encoder, callback)

        boundary = multipart_encoder.content_type.split('=')[-1]
        #print('boundary',boundary,' monitor',monitor.__dict__)

        path = "/core/bundles/" + bundleuuid + "/bitstreams"
        headers = {'Connection':'keep-alive',
            "Content-Type": multipart_encoder.content_type, 'X-XSRF-TOKEN': self.token,
            'Authorization': self.authorization}
        #print('header:',headers)
        #self.session.options(self.baseUrl + path)
        #先上传然后再修改元数据???
        rep = self.session.post(self.baseUrl + path, data=monitor, headers=headers, verify=False,
                                cookies=self.session.cookies)
        self.refreshTokenByHeader(rep.headers)
        if (rep.status_code == requests.codes.created):  #创建成功不返回ok，返回created
            # print(rep.headers)
            # print(rep.content)
            rtn=Bitstream()
            rtn.__dict__=rep.json()
            #print(json.dumps(rep.json(), indent=4, ensure_ascii=False))
            return rtn
        else:
            print(rep.headers)
            print(rep.content)
            rep.raise_for_status()
        pass

    # 创建一个item，只有 dc.tile的名字，其它待补充
    def createItem(self,collection_uuid,itemname):
        data = {
              "name": itemname,
              "metadata": { #  必须把该集合所需要的必填项的所有元数据都填进去，  todo：
                "dc.contributor.author": [
                      {
                          "value": "python程序",
                          "language": "Zh_CN",
                          "authority": "null",
                          "confidence": -1
                      }
                ],
                  "scientist.name": [
                      {
                          "value": itemname,
                          "language": "zh_CN",
                          "authority": 'null',
                          "confidence": -1
                      }
                  ],
                  "scientist.gender": [
                      {
                          "value": "男",
                          "language": "zh_CN",
                          "authority": 'null',
                          "confidence": -1
                      }
                  ],
                "dc.title": [
                  {
                    "value": itemname,
                    "language": "zh_CN",
                    "authority": 'null',
                    "confidence": -1
                  }
                ],
                "dspace.entity.type": [
                      {
                          "value": 'Scientist',
                          "language": "zh_CN",
                          "authority": 'null',
                          "confidence": -1
                      }
                  ]
              },
              "inArchive": "true",
              "discoverable": "true",
              "withdrawn": "false",
              "type": "item"
            }
        path = "/core/items?owningCollection=" + collection_uuid
        headers = {
            "Accept": "application/hal+json, application/json, */*; q=0.01",
            "Content-Type": "application/json", 'X-XSRF-TOKEN': self.token,
            'Connection': 'keep - alive',
            'Authorization': self.authorization}
        rep = self.session.post(self.baseUrl + path, json=data, headers=headers, verify=False,
                                cookies=self.session.cookies)
        self.refreshTokenByHeader(rep.headers)
        if (rep.status_code == requests.codes.created):
            item=Item()
            item.__dict__=rep.json()
            return item
        else:
            print(rep.headers)
            print(rep.content)
            rep.raise_for_status()
        return False

    # 创建一个item，只有 dc.tile的名字，其它待补充
    def createItemWithJson(self, collection_uuid, data):
        path = "/core/items?owningCollection=" + collection_uuid
        headers = {
            "Accept": "application/hal+json, application/json, */*; q=0.01",
            "Content-Type": "application/json", 'X-XSRF-TOKEN': self.token,
            'Connection': 'keep - alive',
            'Authorization': self.authorization}
        rep = self.session.post(self.baseUrl + path, json=data, headers=headers, verify=False,
                                cookies=self.session.cookies)
        self.refreshTokenByHeader(rep.headers)
        if (rep.status_code == requests.codes.created):  #创建成功返回的代码，不见得每次都是ok
            item = Item()
            item.__dict__ = rep.json()
            return item
        else:
            print(rep.headers)
            print(rep.content)
            rep.raise_for_status()
        return False

    def deleteitem(self,itemuuid):
        path="/core/items/"+itemuuid
        headers = {
            "Accept": "application/hal+json, application/json, */*; q=0.01",
            "Content-Type": "application/json", 'X-XSRF-TOKEN': self.token,
            'Connection': 'keep - alive',
            'Authorization': self.authorization}
        rep = self.session.delete(self.baseUrl + path,  headers=headers, verify=False,
                                cookies=self.session.cookies)
        self.refreshTokenByHeader(rep.headers)
        if (rep.status_code == requests.codes.ok):
            # print(rep.headers)
            # print(rep.content)
            return True
        else:
            print(rep.headers)
            print(rep.content)
            rep.raise_for_status()
        return False

if __name__ == "__main__":
    client = DspaceRestClient()
    client.login('goaksoft@126.com', 'goaksoft123')
    #client.getCollectionItemsByFilter('3eab38f6-fac7-4f63-9e54-35200dc7583d', filter='title', scientistName='朵英贤')

    #client.findSubmitAuthorizedByEntityType('isScientistOfOther','isScientistOfOther')
    # client.getCollectionItems('1bdf7cea-d5ff-48f4-a4f3-0b5701382b65')
    for t in client.getEntityTypes():
       print(t.__dict__)
    # print(len(client.getItems()))
    # client.createBundle('e723f1bf-ee62-4e15-845f-2d9b7840b598','ORIGINAL')
    #client.createBitstream('58dfa1ea-7c05-411d-a4b4-b90053d3a6ac', '测试word.doc', 'd:/dde 岩浆岩数据组 产品施工方案 2.docx',upload_monitor)
    #sys.exit(1)
    '''for i in client.getCollectionItems('3eab38f6-fac7-4f63-9e54-35200dc7583d'):  #科学家j集合
        print('      条目:', i.name, 'uuid', i.uuid)
        for b in client.getItemBundles(i.getBundlesLink()):
            print('          Bundle:', b.name, 'uuid', b.uuid)
            for bs in client.getBitstreams(b.getBitstreamsLink()):
                print('              BitStream:', bs.name, 'uuid', bs.uuid)'''
    #if client.isBundleExists('0f856b39-75f9-4ef4-9bef-769d0401b9fa', 'EXTRA')==False:
    #    client.createBundle('0f856b39-75f9-4ef4-9bef-769d0401b9fa', 'EXTRA')
    #

    for c in client.getCommunities():
        print('社区：', c.name,'  集合链接',c.getCollectionsLink())
        for s in client.getSubCommunities(c.getSubCommunitiesLink()):
            print('  子社区:', s.name,)
        for col in client.getCollectionsByUrl(c.getCollectionsLink()):
            print('  集合：', col.name,'uuid', col.uuid)
            '''for i in client.getCollectionItems(col.uuid):
                print('      条目:', i.name, 'uuid', i.uuid)
                for b in client.getItemBundles(i.getBundlesLink()):
                    print('          Bundle:', b.name, 'uuid', b.uuid)
                    for bs in client.getBitstreams(b.getBitstreamsLink()):
                        print('              BitStream:', bs.name, 'uuid', bs.uuid)'''
