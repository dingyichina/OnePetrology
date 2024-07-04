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
import os,camelot,operator,re,sys
import shutil
from pathlib import Path
from DayLogger import DayLogger
from cajparser import CAJParser

#表格提取类，从Pdf文件中
class  TableExtracter(object):

    #初始化参数，输入目录，输出目录，穷举下面的目录和文件
    def __init__(self,inputDir='./input/',outputDir='./output/'):
        self.logger=DayLogger('表格提取').logger # 日志记录
        self.inputDir=Path(inputDir)
        self.outputDir=Path(outputDir)
    #确保文件名对应的目录存在
    def ensureOutputDir(self,file):
        filedir=file.relative_to(self.inputDir).parts[:-1] #file.absolute().parts[len(self.inputDir.parts):len(file.absolute().parts) - 1]
        newfiledir=re.sub(r'[\\/:*?"<>|\r\n]+', "_", file.stem).strip()  #去除某些文件名中的特殊字符，以适应windows的目录和文件名命名规则
        #如果过长，则截取左边的
        if len(newfiledir)>250:
            newfiledir=newfiledir[:250]
        newPath=self.outputDir.joinpath(*filedir).joinpath(newfiledir)#/newdir/newfiledir
        newp=Path('\\\?\\'+str(newPath.absolute()))
        newp.mkdir(exist_ok=True,parents=True) #目录不存在则创建，存在则不处理
        return newp

    #从一篇文件中提取表格，输入参数：文件（path对象）,flavor的两个参数之一：lattice或者stream
    def extractTable(self,file,flavor='lattice'):  #默认为按照线框提取表格数据，另外一种方式为stream
        fileDir=self.ensureOutputDir(file)
        i = 0
        try:
            predf=None
            if (flavor =='lattice'):
                tables = camelot.read_pdf(str(file.absolute()), flavor=flavor,pages="all", encoding='gbk',flag_size=True,strip_text='\n',copy_text=['v'],line_scale=40)
            else :
                tables = camelot.read_pdf(str(file.absolute()), flavor=flavor, pages="all", edge_tol=200,row_tol=10,encoding='gbk', flag_size=True, strip_text='\n')
            #从第一个循环到最后一个，逐个判断是否需要和前一个合并（ 解决 表格 跨页的问题）
            for tpos in range(0,tables.n-1):#确保从前往后的顺序
                #camelot.plot(tables[tpos], kind='textedge').show() #可视化调试，使用中用不上
                if self.isempty(tables[tpos]):
                    self.logger.info("表格索引："+str(tpos) + "为空，舍弃不保存")
                    predf=tables[tpos].df
                    continue
                #判断是否需要与上一个表格合并，这里的上一个表格指的是成功保存的表格
                rtn=self.needCombine(predf,tables[tpos].df)
                if self.needCombine(predf,tables[tpos].df):
                    #合并两个df
                    tables[tpos].df.columns = predf.columns
                    predf=predf.append(tables[tpos].df)  # 合并完毕
                    #去重，滤掉有可能的重复行(此时有可能是行列转置的，需要补充判断 ） todo：
                    predf.drop_duplicates(inplace=True)
                    kw = {
                        "sheet_name": f"page-{tables[tpos].page}-table-{tables[tpos].order}",
                        "encoding": "utf-8",
                    }
                    self.write2excel(fileDir, predf, i,**kw)
                else:
                    predf=tables[tpos].df
                    kw = {
                        "sheet_name": f"page-{tables[tpos].page}-table-{tables[tpos].order}",
                        "encoding": "utf-8",
                    }
                    i=i+1
                    self.write2excel(fileDir,predf,i,**kw)
            #处理完成，把文件从input输入目录转移到输出目录，代码暂缺，调试完成后加上
            #shutil.copy2(str(file.absolute()),str(fileDir)) #目前是copy，后期改为move
            #os.system('copy "'+ str(file.absolute())+'"  "'+str(fileDir)+'"')
            (fileDir/'原始文件.pdf').write_bytes(file.read_bytes())  #复制二进制文件
        except Exception as ex2:
            self.logger.error("读取失败："+str(ex2))
            return i

        return i
    #写入到文件
    def write2excel(self,fileDir,df,num,**kwargs):
        # GBK转出来的字符为全角，为了计算方便，需要转换为半角
        self.transData(df)
        try:
            df.to_excel(str(fileDir / "表格{0}.xlsx".format(num)), index=False,**kwargs)
            self.logger.info("表格：" + str(num) + "保存成功")
        except Exception as ex:
            self.logger.info("表格：" + str(num) + "保存失败,原因：", ex)

    # 判断是否需要与上一个表格合并，输入参数为得到的table列表和需要判断的索引
    def needCombine(self,predf,df):
        if predf is None:#第一个表格不需要合并
            return False;
        #判断的依据首先是列数相同
        if(predf.shape[1] == df.shape[1] ): #列数相同
            #检查后一个df的第一行中是否存在'续' 'continue'  的续前表的字眼，如果有，是需要合并的
            columnlist=df[0:1]
            for col in columnlist:
                if('续' in str(col).strip().lower() or 'continue' in str(col).strip().lower() ):
                    df.drop(df[0],inplace=True)
                    break
            return True
        #默认返回不合并
        return False

    #循环处理目录下所有的pdf和caj、kdh文件，目前仅支持以上格式。对于扫描的pdf和caj不支持。
    def loop4all(self):
        #首选把所有的caj和kdh文件都转化为pdf，然后再进行识别
        fs = self.inputDir.rglob('*.caj')  # 循环所有的caj
        for f in fs:
            self.cajconvert(f)
        fs = self.inputDir.rglob('*.kdh')  # 循环所有的kdh
        for f in fs:
            self.cajconvert(f)
        #已转换完毕，开始pdf识别
        fs=self.inputDir.rglob('*.pdf') #循环所有的pdf
        for f in fs:
            self.logger.info("---开始处理:"+str(f.stem)+"    -------")
            rtn =self.extractTable(f,flavor='stream')
            if(rtn==0):#没有提炼出有效表格，换stream试试
               self.logger.info("---没有找到有效表格，换Lattice方式处理:"+ str(f.stem)+"    -------")
               rtn = self.extractTable(f)
            self.logger.info("---处理完毕:"+str(f.stem)+"    -------")

    #检查是否是空的表格
    def isempty(self,t):
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
                if c != None and len(c.strip()) > 0 and len(c.strip())<50:  #如果文本过长，也认为是误伤，暂定50
                    return False
        return  True

    #转换所有的字符为半角
    def transData(self,t):
       df=t
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
       self.logger.info("需要修正的行索引为："+str(rows))
       for row in rows.keys():
           content=[]
           for j in range(df.shape[1]):  # 列数
               c = df.iloc[row, j]
               if c != None and len(c.strip()) > 0:
                   content=content+c.strip().split(' ')
           if len(content)==df.shape[1]:
               for i in range(df.shape[1]):  # 列数
                   df.iloc[row, i] = content[i]
               self.logger.info("修正了："+str(row)+" 行")
       #print("转换后：",df)

    #caj或者kdh转换为pdf,传入的是一个path对象，返回的是转换之后的pdf的对象
    def cajconvert(self,cajfile):
        dst = cajfile.parent / (re.sub(r'[\\/:*?"<>|\r\n]+', "_", cajfile.stem) + '.pdf')
        try:
            caj = CAJParser(str(cajfile.absolute()))
            caj.convert(str(dst.absolute()))
            self.logger.info(str(cajfile.absolute())+" 转换为pdf成功。")
        except Exception as ex:
            self.logger.error(str(cajfile.absolute())+" 转换为pdf 失败！！！！！！")
        return dst

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


    if len(sys.argv)==3:
        #检查两个参数是否目录，如果不是则打印提示
        p1=Path(sys.argv[1])
        p2=Path('\\\?\\'+sys.argv[2])  #添加'\\\?\\'是为了突破256路径长度的限制，实际上添加的是\\?\
        if (p1.is_dir() and p2.is_dir()):
            extracter=TableExtracter(sys.argv[1],sys.argv[2])
            extracter.loop4all()
        else:
            usage = '''  输入的参数不是目录。 
                    本命令需要两个参数，均为字符串。命令的形式如下：
                          python  myname.py   源文件目录   输出目录
                             -----  源文件目录   ,需要处理的包含pdf、caj、kdh格式文献的目录
                             -----  输出目录    ，期望输出的目录，最好是已建好的空目录。路径分割符用 / 
                     '''
            print(usage)
    elif len(sys.argv)==1:
        extracter = TableExtracter()
        extracter.loop4all()
    else:
        usage = ''' 本命令需要两个参数，均为字符串。命令的形式如下：
                    python  myname.py   源文件目录   输出目录
                        -----  源文件目录   ,需要处理的包含pdf、caj、kdh格式文献的目录
                        -----  输出目录    ，期望输出的目录，最好是已建好的空目录。路径分割符用 / 
                    '''
        print(usage)

