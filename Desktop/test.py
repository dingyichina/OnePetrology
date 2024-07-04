import math
import pathlib
import sys

import camelot
from PyQt5 import Qt
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPixmap, QPainter, QColor, QBrush, QFont, QTextOption
from PyQt5.QtWidgets import QApplication
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams, LTTextBox, LTFigure, LTImage, LTCurve
from pdfminer.converter import PDFPageAggregator


def test() :
    path = list(pathlib.Path.cwd().parents)[1].joinpath('data/automate/002pdf')
    f_path = path.joinpath('d:/A-type granites in the western margin of the Siberian Craton_ implications for breakup of the Precambrian supercontinents Columbia_Nuna and Rodinia.pdf')
    app = QApplication(sys.argv)

    with open(f_path, 'rb') as f:
        parser = PDFParser(f)
        doc = PDFDocument(parser)
        print(doc.info)
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        text=""
        i=1
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
            print(page.resources.get('Font').get('C0_0').objid)
            pixmap=QPixmap(math.ceil(page.mediabox[2]),math.ceil(page.mediabox[3]))
            width=math.ceil(page.mediabox[2])
            height=math.ceil(page.mediabox[3])
            pixmap.fill(QColor(255,255,255))
            painter=QPainter(pixmap)
            painter.setBackground(QBrush(QColor(255,255,255)))
            painter.setFont(QFont("simsong",9))
            painter.begin(pixmap)
            layout = device.get_result()
            for x in layout:
                #print(x)
                # 获取文本对象
                if isinstance(x, LTTextBox):
                    ctm,ts,gs=interpreter.get_current_state()
                    print(ctm)
                    print(gs)
                    print(ts)
                    font=QFont("simsun")
                    font.setKerning(True)
                    font.setLetterSpacing(QFont.AbsoluteSpacing,ts.charspace-1)
                    #font.setPointSize(ts.fontsize)
                    font.setPixelSize(ts.fontsize)

                    font.setWordSpacing(ts.wordspace-3)
                    painter.scale(1,1)
                    painter.setFont(font)

                    rectF=QRectF(x.x0,height-x.y1,x.x1,height-x.y0)
                    rectF.adjust(0,0,0,50)
                    print(x.bbox,"转换后，",rectF, x.get_text())
                    option=QTextOption()
                    option.setWrapMode(QTextOption.NoWrap)
                    painter.drawText(rectF,x.get_text(),option)
                    #print("LTTextBox")
                    #(x.bbox)
                    #print(x.get_text().strip())
                    text+=x.get_text().strip()
                    pass
                # 获取图片对象
                if isinstance(x,LTImage):
                    #painter.drawImage(x.bbox,x.)
                    pass
                    #print('这里获取到一张图片')
                # 获取 figure 对象
                if isinstance(x,LTFigure):
                    #print(x._objs)
                    pass
                    #x.analyze(laparams)
                    #print('这里获取到一个 figure 对象')
                    #print(x)
                if isinstance(x,LTCurve):
                    #print("LTCurve:",x)
                    pass
            painter.end()
            pixmap.save("d:/page{}.jpg".format(i),"JPG")
            i+=1
            break
        #print(text)

if __name__ == "__main__":


    tables = camelot.read_pdf("d:/2023年上半年通信费.pdf", flavor="stream", pages="1", encoding='gbk', flag_size=True,table_areas=["20,380,800,300"],
                              strip_text='\n')
    df = tables[0].df
    print(df)
    df.to_excel("d:/testpdf.xlsx",index=False)
    pass