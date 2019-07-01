from PyPDF2 import PdfFileReader
import os
import datetime
import re


#
# 方法：爬取数据
#
def data_crawlingV2(pdf):

    pdf_input = PdfFileReader(open(pdf, 'rb'))
    # 获取 pdf 的文件名
    pdf_name = os.path.basename(pdf).split('.')[0]
    # 获取pdf中的信息
    pdf_text = pdf_input.getPage(0).extractText().split('\n')

    return pdf_text
    # print(pdf_text)
    # if len(pdf_text) == 5:
    #     name = re.split("\.+\\s+", pdf_text[0])[1]
    #     course = pdf_text[1]
    #     # 英文时间格式转换为y/m/d
    #     certificateTime = pdf_text[2]
    #     #certificateTime = datetime.datetime.strptime(pdf_text[2], '%d %b %Y').strftime('%Y/%m/%d')
    #     certificateNum = pdf_text[3]
    #     print(name + ',' + course+','+certificateTime+','+certificateNum)
    #     return [name, course, certificateTime, certificateNum, pdf_name]
    #
    # if len(pdf_text) == 6:
    #     name = pdf_text[1]
    #     course = pdf_text[2]
    #     # 英文时间格式转换为y/m/d
    #     certificateTime = pdf_text[3]
    #    # certificateTime = datetime.datetime.strptime(pdf_text[3], '%d %b %Y').strftime('%Y/%m/%d')
    #     certificateNum = pdf_text[4]
    #     print(name + ',' + course+','+certificateTime+','+certificateNum)
    #     return [name, course, certificateTime, certificateNum, pdf_name]