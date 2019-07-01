from PyPDF2 import PdfFileReader, PdfFileWriter
import glob
import os
import time

def GoInPDF(CLD_Path):
    Root_file = os.listdir(CLD_Path)
    for partment_list in Root_file:
        person_list = os.listdir(CLD_Path + '/' + partment_list)
        for filePersonName in person_list:
            # 如果当前全是人名为目录的目录下选中的filePersonName是文件则跳过不切
            if os.path.isfile(CLD_Path + '/' + partment_list + '/' + filePersonName):
                print(CLD_Path + '/' + partment_list + '/' + filePersonName)
            else:
                files_list = os.listdir(CLD_Path + '/' + partment_list + '/' + filePersonName)
                #每个人下面的文件夹
                for file in files_list:
                    #PDF就切，JGP跳过
                    if file == 'pdf':
                        print(file)
                        pdfs = glob.glob("{}/*.pdf".format(CLD_Path + '/' + partment_list + '/' + filePersonName+'/'+file))
                        print(pdfs)
                        for pdf in pdfs:
                            split_pdf(pdf, CLD_Path + '/' + partment_list + '/' + filePersonName)
                    else:
                        continue

def split_pdf(infn, newPdfDir):

    # 路径不存在就新建一个
    subdir = newPdfDir + '/PDFS'
    if not os.path.exists(subdir):
        os.mkdir(subdir)
        print('文件夹创建成功:' + subdir)
    try:
        print('正在打开文件:' + infn)
        pdf_input = PdfFileReader(open(infn, 'rb'))
        # 获取 pdf 的文件名
        pdf_name = os.path.basename(infn).split('.')[0]
        # 获取 pdf 共用多少页
        page_count = pdf_input.getNumPages()
    except:
        print('出现异常的文件为:'+infn)
        page_count = 0
    # 获取当前时间戳
    #t = time.time()
    #timeInt = (int(round(t * 1000)))
    # 将 pdf 第j页之后的页面，输出到一个新的文件
    j = 0
    for i in range(j, page_count):
        pdf_output = PdfFileWriter()
        pdf_output.addPage(pdf_input.getPage(i))
        outfn = subdir+'/'+ pdf_name +'-'+i.__str__()+'.pdf'
        j = j + 1
        pdf_output.write(open(outfn, 'wb'))
        print(outfn+'已生成')
    print(infn+'已经切割完成!')


if __name__ == '__main__':
    #GoInPDF('F:/test/2. DQ045')
    GoInPDF('F:/实习工作/2. DQ045')
    GoInPDF('F:/实习工作/3. DQ046')
    GoInPDF('F:/实习工作/4. DQ047')
    GoInPDF('F:/实习工作/5. DQ048')
    GoInPDF('F:/实习工作/6. DQ049')
    GoInPDF('F:/实习工作/7. DQ050')
