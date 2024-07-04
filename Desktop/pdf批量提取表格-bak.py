#coding=utf-8
'''
python 3.6

实现从pdf中批量提取表格
采用了camelot-py类库
安装方法：

    pip install camelot-py  (参考requirements.txt)
    pip install opencv-python
    pip install xlwt
    然后需要安装ghostscript，可以从官网下载对应的操作系统的版本，然后安装。

使用方法：
    1）把需要提取的pdf文件，复制到input目录中，然后执行本文件
    2）所有的输出结果，在output目录中，一个pdf文件对应一个目录，目录里包含pdf对应的所有表格文件。
    3）默认编码为gbk（否则提不出中文）
    4）默认输出的格式为excel
    5)默认为采集pdf中的全部表格（可以指定某一页），导致的结果就是会出现一些空的excel

    作者：丁毅
    2019-11-11
'''
import os,camelot,operator
from pathlib import Path


def extractTable(file,flavor='lattice'):  #默认为按照线框提取表格数据，另外一种方式为stream
    fileName=file[:-4]
    os.makedirs("./output/"+fileName, exist_ok=True)
    try:
        tables = camelot.read_pdf("./input/"+file, flavor=flavor,pages="all", encoding='gbk')
    except Exception as ex2:
        print("读取失败：",ex2)
        return 0
    i=0
    for index,t in  enumerate(tables) :
        #GBK转出来的字符为全角，为了计算方便，需要转换为半角
        if isempty(t):
            print("表格索引：" ,index,"为空，舍弃不保存")
            continue
        else:
            transData(t)
            i = i + 1
            try:
                t.to_excel("./output/"+fileName+"/表格{0}.xlsx".format(i))
                print("表格：", i, "保存成功")
            except Exception as ex:
                print("表格：", i, "保存失败,原因：",ex)

    return i


def loop4all():
    fs=os.listdir("./input")
    for f in fs:
        ext = f[-3:]
        ext = ext.lower()
        if (operator.eq(ext, 'pdf') ):
            print("---开始处理:",f,"    -------")
            rtn =extractTable(f,flavor='stream')
            if(rtn==0):#没有提炼出有效表格，换stream试试
                print("---没有找到有效表格，换Lattice方式处理:", f, "    -------")
                rtn = extractTable(f)
            print("---处理完毕:", f, "    -------")
def loop4dir(srcDir,dstDir):
    fs=os.listdir(srcDir)

    for f in fs:
      if os.path.isdir(srcDir+f):
          loop4dir(srcDir+f)
      else:
        ext = f[-3:]
        ext = ext.lower()
        if (operator.eq(ext, 'pdf') ):
            print("---开始处理:",srcDir+f,"    -------")
            rtn =extractTable(srcDir+f,flavor='stream')
            if(rtn==0):#没有提炼出有效表格，换stream试试
                print("---没有找到有效表格，换Lattice方式处理:", srcDir+f, "    -------")
                rtn = extractTable(srcDir+f)
            print("---处理完毕:", srcDir+f, "    -------")
#检查是否是空的表格
def isempty(t):
    df = t.df
    #为了防止stream方式把排版算做表格，那么，所有的列数小于3的都算作空表
    if  df.shape[1] <=4:  #根据实际需要调整这个值
        return True
    #某些中文文献表头带线，但内容不带，所以需要判断行数，小于等于3的也算作空表
    if df.shape[0] <= 3:  # 根据实际需要调整这个值
        return True
    #判断是否为空的依据是一旦发现不为空的则返回
    for i in range(df.shape[0]):  # 行数
        for j in range(df.shape[1]):#列数
            c=df.iloc[i, j]
            if c != None and len(c.strip()) > 0:
                return False
    return  True

#转换所有的字符为半角
def transData(t):
   df=t.df
   #print("转换前：",df)
   for i in range(df.shape[0]): #行数
       for j in range(df.shape[1]):#列数
           df.iloc[i,j]=DBC2SBC(df.iloc[i,j])
   #检测是否有空行错位的情况
   #    如果存在空的单元格，那么就把该行所有的元素都取出来，然后用空格分割，如果分割之后的列表数恰好等于 该行的列数，那么就自动把这一行的值平均分配到每一个单元格
   #  此种算法不适应一个单元格里包含空格分开的内容的情况，这种情况暂时需要手工修正
   rows={}
   for i in range(df.shape[0]):  # 行数
       for j in range(df.shape[1]):#列数
           c = df.iloc[i, j]
           if c == None or len(c.strip()) ==0:
               rows[i]=i
   print("需要修正的行索引为：",rows)
   for row in rows.keys():
       content=[]
       for j in range(df.shape[1]):  # 列数
           c = df.iloc[row, j]
           if c != None and len(c.strip()) > 0:
               content=content+c.strip().split(' ')
       if len(content)==df.shape[1]:
           for i in range(df.shape[1]):  # 列数
               df.iloc[row, i] = content[i]
           print("修正了：",row, " 行")
   #print("转换后：",df)

'''
全角半角之间的转换
全角即：Double Byte Character，简称：DBC
半角即：Single Byte Character，简称：SBC
'''
def DBC2SBC(ustring):
    # 全角转半角 ”'
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x3000:
            inside_code = 0x0020
        else:
            inside_code -= 0xfee0
        if not (0x0021 <= inside_code and inside_code <= 0x7e):
            rstring += uchar
            continue
        rstring += chr(inside_code)
    return rstring

def SBC2DBC(ustring):
    #' 半角转全角 ”'
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x0020:
            inside_code = 0x3000
        else:
            if not (0x0021 <= inside_code and inside_code <= 0x7e):
                rstring += uchar
                continue
        inside_code += 0xfee0
        rstring += chr(inside_code)
    return rstring

if __name__ == "__main__":
    loop4all()
    #loop4dir("D:/北京离子探针中心shrimp论文集part/")
    pdflist=Path("D:/北京离子探针中心shrimp论文集part/").rglob("*.caj")
    for f in pdflist:
        print(f.absolute().parts [ len(Path("D:/北京离子探针中心shrimp论文集part/").parts):len(f.absolute().parts)-1 ])

