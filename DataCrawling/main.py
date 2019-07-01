import glob
from crawling import data_crawling
from crawlingV2 import data_crawlingV2
from writeInExcel import writeInExcel

if __name__ == '__main__':

    #存放PDF的文件名
    file_list = 'F:/test/CutResult/'
    pdfs = glob.glob("{}/*.pdf".format(file_list))
    list_Message = []

    #读取所有的PDF爬取数据放入list_Message中
    for pdf in pdfs:
        simple_Message = data_crawlingV2(pdf)
        if simple_Message is not None:
            list_Message.append(simple_Message)

    # 读取完数据后可以写入数据到ECEXL中
    writeInExcel(list_Message)
