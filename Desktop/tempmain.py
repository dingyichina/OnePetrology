'''
    本文件用来执行一些临时的导入工作


from service.DSpace7RestClient import client
import os
if __name__=='__main__':
    client.login('goaksoft@126.com', 'goaksoft123')
    work_dir = "C:/Users/Ding/Desktop/fia/800×1200"
    for parent, dirnames, filenames in os.walk(work_dir):
        for filename in filenames:
            basename, ext = os.path.splitext(filename)
            print(basename,",",ext)
            if (len(client.getCollectionItemsByFilter('3eab38f6-fac7-4f63-9e54-35200dc7583d', filter='title', scientistName=basename))==0): #不存在则创建
                pass

                client.createItem('3eab38f6-fac7-4f63-9e54-35200dc7583d',basename)
                # 查询创建是否成功
                items = client.getCollectionItemsByFilter('3eab38f6-fac7-4f63-9e54-35200dc7583d', filter='title',
                                                          scientistName=basename)
                #pass


                if(len(items)>0):
                    # 以第一个为标准检查
                    if client.isBundleExists(items[0].uuid,"ORIGINAL")==False:
                        client.createBundle(items[0].uuid,"ORIGINAL")
                        # 查到bundleid  todo：此处应该是create之后的返回结果即可，代码待修改。
                        for b in client.getItemBundles(items[0].getBundlesLink()):
                            if b.name=="ORIGINAL":
                                # 上传该文件
                                client.createBitstream(b.uuid,filename, parent+"/"+filename)

            else:
                items = client.getCollectionItemsByFilter('3eab38f6-fac7-4f63-9e54-35200dc7583d', filter='title',
                                                          scientistName=basename)

                for item in items:
                    if item.name not in ['彭士禄']:
                        print(item.name, ' 删除结果:', client.deleteitem(item.uuid))'''
import pandas as pd
from pandasgui import show


df = pd.read_excel("葛茂卉东北_hf样品full3.xlsx", sheet_name='Sheet1', header=0)
show(df)