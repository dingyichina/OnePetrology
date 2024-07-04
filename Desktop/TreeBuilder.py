'''

    本类用来分离tree的构建代码

'''
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt

from model.KnowledgeNode import ValueType, KNodeType
from myservice import client

#返回第二列的类型，该列不可编辑，不可被选中
def getTypeItem(strType):
    rtn= QStandardItem(strType)
    rtn.setEditable(False)
    rtn.setSelectable(False)
    return rtn

# 设置用户数据，根据需要，设置uuid，type
def setUserData(obj,item):
    item.setData(obj.uuid, Qt.ItemDataRole.UserRole )
    item.setData(obj.type, Qt.ItemDataRole.UserRole +1)


# 根据传入的Community对象，返回一个QStandardItem
def getCommunityItem(community):
    rtn = QStandardItem(community.name)
    rtn.setEditable(False)
    rtn.setEnabled(True)
    #设置用户数据
    setUserData(community,rtn)
    rtn.setIcon( QIcon("./res/community.png"))
    return rtn

# 设置用户数据，根据需要，设置uuid，type
def setKtreeUserData(obj,item):
    item.setData(obj.uuid, Qt.ItemDataRole.UserRole )
    item.setData(obj.type, Qt.ItemDataRole.UserRole +1)
    item.setData(obj.name, Qt.ItemDataRole.UserRole + 2)

# 得到ktree对应的item
def getKTreeItem(knode):
    rtn = QStandardItem(knode.name)
    rtn.setEditable(False)
    rtn.setEnabled(True)
    # 设置用户数据
    setKtreeUserData(knode, rtn)
    rtn.setIcon(QIcon("./res/community.png"))
    return rtn
# 得到ktree对应的item
def getKNodeItem(knode):
    rtn = QStandardItem(knode.name)
    rtn.setEditable(False)
    rtn.setEnabled(True)
    # 设置用户数据
    setKtreeUserData(knode, rtn)
    # 此处需要修改，不同结点类型显示不同图标 todo :
    if knode.type in [KNodeType.PROP]:
        rtn.setIcon(QIcon("./res/leaf.png"))
    else:
        rtn.setIcon(QIcon("./res/collection.png"))
    return rtn


# 得到科学家信息，传入的item为科学家集合的条目
def getScientist(item):
    rtn = QStandardItem(item.name)
    rtn.setEditable(False)
    rtn.setEnabled(True)
    # 设置用户数据
    rtn.setData(item.uuid, Qt.ItemDataRole.UserRole)
    rtn.setData('科学家', Qt.ItemDataRole.UserRole + 1)
    rtn.setData(item.name, Qt.ItemDataRole.UserRole + 2)  #把科学家的名字存起来

    rtn.setIcon(QIcon("./res/scientist.png"))
    return  rtn


def getCollectionItem(collection):
    rtn = QStandardItem(collection.name)
    rtn.setEditable(False)
    rtn.setEnabled(True)
    # 设置用户数据
    setUserData(collection, rtn)
    rtn.setIcon(QIcon("./res/collection.png"))
    return rtn


def getItemItem(item):
    rtn = QStandardItem(item.name)
    rtn.setEditable(False)
    rtn.setEnabled(True)
    # 设置用户数据
    setUserData(item, rtn)
    rtn.setIcon(QIcon("./res/item.png"))
    return rtn

def getBundleItem(bundle):
    rtn = QStandardItem(bundle.name)
    rtn.setEditable(False)
    rtn.setEnabled(True)
    # 设置用户数据
    setUserData(bundle, rtn)
    rtn.setIcon(QIcon("./res/bundle.png"))
    return rtn

def getBitstreamItem(bitstream):
    rtn = QStandardItem(bitstream.name)
    rtn.setEditable(False)
    rtn.setEnabled(True)
    # 设置用户数据
    setUserData(bitstream, rtn)
    rtn.setIcon(QIcon("./res/bitstream.png"))
    return rtn



# 根据uuid和type调用对应的函数进行获取
def getChildrenItem(uuid,strType,parent):
    if(strType=='collection'):
        #查找collection下面所有的items
        for itemIndex, i in enumerate(client.getCollectionItems(uuid)):
           item = getItemItem(i)
           parent.appendRow(item)
           parent.setChild(itemIndex, 1, getTypeItem(i.type))
    elif strType=='community':
        # 查找Community下面所有的subCommunity和Collections
        community=client.getCommunity(uuid)

        for itemIndex, i in enumerate(client.getSubCommunities(community.getSubCommunitiesLink())):
            item = getCommunityItem(i)
            parent.appendRow(item)
            parent.setChild(itemIndex, 1, getTypeItem(i.type))
        for itemIndex, i in enumerate(client.getCollectionsByUrl(community.getCollectionsLink())):
            item = getCommunityItem(i)
            parent.appendRow(item)
            parent.setChild(itemIndex, 1, getTypeItem(i.type))
    elif strType=='item':
        #item需要展开bundle，首先根据uuid得到item对象，然后获取bundle链接
        item=client.getItem(uuid)
        for bundleIndex,bundle in enumerate(client.getItemBundles(item.getBundlesLink())):
            item = getBundleItem(bundle)
            parent.appendRow(item)
            parent.setChild(bundleIndex, 1, getTypeItem(bundle.type))

    elif strType=='bundle':
        #需要展开下面的bitstream
        bundle=client.getBundle(uuid)
        for bitstreamIndex,bitstream in enumerate(client.getBitstreams(bundle.getBitstreamsLink())):
            item = getBundleItem(bitstream)
            parent.appendRow(item)
            parent.setChild(bitstreamIndex, 1, getTypeItem(bitstream.type))

        pass


# 根据uuid和type调用对应的函数进行获取
def getChildrenItem(uuid,strType,parent,scientistName=None):
    if(strType=='collection'):
        items=[]
        if scientistName==None:
            items=client.getCollectionItems(uuid)
        else:
            items = client.getCollectionItemsByScientist(uuid, scientistName)
        #查找collection下面所有的items
        for itemIndex, i in enumerate(items):
           #print(i.__dict__)
           item = getItemItem(i)
           parent.appendRow(item)
           parent.setChild(itemIndex, 1, getTypeItem(i.type))
    elif strType=='community':
        # 查找Community下面所有的subCommunity和Collections
        community=client.getCommunity(uuid)

        for itemIndex, i in enumerate(client.getSubCommunities(community.getSubCommunitiesLink())):
            item = getCommunityItem(i)
            parent.appendRow(item)
            parent.setChild(itemIndex, 1, getTypeItem(i.type))
        for itemIndex, i in enumerate(client.getCollectionsByUrl(community.getCollectionsLink())):
            item = getCommunityItem(i)
            parent.appendRow(item)
            parent.setChild(itemIndex, 1, getTypeItem(i.type))
    elif strType=='item':
        #item需要展开bundle，首先根据uuid得到item对象，然后获取bundle链接
        item=client.getItem(uuid)
        for bundleIndex,bundle in enumerate(client.getItemBundles(item.getBundlesLink())):
            item = getBundleItem(bundle)
            parent.appendRow(item)
            parent.setChild(bundleIndex, 1, getTypeItem(bundle.type))

    elif strType=='bundle':
        #需要展开下面的bitstream
        bundle=client.getBundle(uuid)
        for bitstreamIndex,bitstream in enumerate(client.getBitstreams(bundle.getBitstreamsLink())):
            item = getBundleItem(bitstream)
            parent.appendRow(item)
            parent.setChild(bitstreamIndex, 1, getTypeItem(bitstream.type))

        pass
