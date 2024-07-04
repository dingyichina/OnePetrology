'''
    本类用来定义全局的单例对象


'''
from PyQt5.QtCore import QThread

from DayLogger import DayLogger
from service.DSpace7RestClient import DspaceRestClient
from service.OnePetrologyClient import OnePetrologyRestClient
from service.arangodb import ArangoDBOper
import pandas as pd

arango = ArangoDBOper()


client = DspaceRestClient()

logger = DayLogger("OnePetrology.log", level='debug').logger

username = "GEOWIND@126.COM"


endpoint = OnePetrologyRestClient()


__version__ = 0.49


# 检查是否需要升级，返回True代表需要升级，返回False代表不需要升级
def checkUpdate():
    # 检查是否是最新版本
    # 目前写死item，从item中获取元数据，然后对比版本号。如果版本号不一致，则提示需要升级
    item = client.getItem("69bbb230-73a4-4b47-b279-94c2f4f15060")
    server_version =  float(item.metadata['dc.description.version'][0]['value'])
    if server_version > __version__:
        return True
    else:
        return False

cache_leafliet ={}  # 缓存知识节点的叶子节点

def getleaflist(k_name,owner=username):
    keystr = '/'.join([k_name, owner.upper()])
    if keystr in cache_leafliet.keys():
        return cache_leafliet.get(keystr)
    # 访问并缓存
    print(k_name, owner.upper())
    k =  arango.fetchKNodeByNameAndOwner(k_name, owner.upper())[0]
    rtn = arango.getDf(k).leaf_list
    cache_leafliet[keystr] = rtn
    return rtn

# 后台启动线程，去获取数据，避免后期操作卡顿
def initData():
    thread = InitDataThread()
    thread.start()
    pass

# 初始化数据的线程
class InitDataThread(QThread):

    def __init__(self,  parent=None):
        super(InitDataThread, self).__init__(parent)

        pass

    # 处理提交到db的操作
    def run(self):

        logger.info("init data  Start:")
        try:
            # 得到所有实体列表，并循环得到所有的叶子节点
            kn_list = arango.fetchAllEntity(owner=username.upper())
            for k in kn_list:
                logger.info("get data  for:" + k.name)
                getleaflist(k.name,username.upper())

            logger.info("init data  Finished:" )
            self.finishSignal.emit("Query private Finished:" + self.k_node.name)
        except Exception as ex:
            import traceback
            msg = traceback.format_exc()
            logger.error(msg)




if __name__ == '__main__':
    aql="for c in Igneous_Rock   return c"
    print("开始获取数据")
    doc_list = arango.getByAQL(aql)
    df = pd.DataFrame(doc_list)
    print("开始写入")
    # 创建一个ExcelWriter对象
    with pd.ExcelWriter("d:/主库全部数据-分组.xlsx") as writer:

        # 遍历每个类别
        for category, group_df in df.groupby('owner'):
            # 将每个分组写入到相应的Sheet中
            group_df.to_excel(writer, sheet_name=category, index=False,engine="xlsxwriter")

    #df.to_excel("d:/主库全部数据2.xlsx",sheet_name="Igneous_Rock",index=False,engine="xlsxwriter")
    print("结束写入")
    exit(0)

    rtn = getleaflist("Igneous_Rock","GEOWIND@126.COM")
    #arango.getLeafList4Entity(k, rtn)
    for r in rtn:
        print(r.name,r.value_type)
    rtn = getleaflist("Igneous_Rock", "GEOWIND@126.COM")
    # arango.getLeafList4Entity(k, rtn)
    for r in rtn:
        print(r.name, r.value_type)
    pass
    '''
    knlist = arango.fetchAllEntity()
    for k in knlist:
        rtn = []
        arango.getLeafList4Entity(k, rtn)
        deep_level = 0
        for m in rtn:
            pth = []
            arango.getLeafToParent(m, k, pth)
            m.pth = pth
            print([m.name, m.cn_name], len(pth))
            if (len(pth) > deep_level):
                deep_level = len(pth)
        print("deep_level", deep_level)

        data = []
        # 二次遍历生成长短一致的series
        for m in rtn:
            se = [m.cn_name, m.name]
            # 首先把pth中的插入
            for i in m.pth:
                se.insert(0, i.name)
            for j in range(0, deep_level - len(m.pth)):
                se.insert(0, None)
            print(se)
            data.append(se)
        columns = []
        for i in range(0, deep_level + 2):
            columns.append("Column{}".format(i))
        index = []
        for i in range(0, deep_level):
            index.append("Column{}".format(i))
        df = pd.DataFrame(data=data, columns=columns)
        df.info()

        newdf = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)  # 转置
        newdf.to_excel("temp.xlsx", index=False)
        # 根据前deep_level个column进行group分组'''
