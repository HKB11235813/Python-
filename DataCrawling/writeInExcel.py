# coding=utf-8
from openpyxl import Workbook

def writeInExcel(list_Message):

    wb = Workbook()
    ws = wb.create_sheet("certificate")
    label = ["name", "course", "certificateTime", "certificateNum", "path"]
    #这个地方之所以 变成numpy格式是因为在很多时候我们都是在numpy格式下计算的，模拟一下预处理
    rowLength = 5

    ws.append(label)
    for i in range(len(list_Message)):
        ws.append(list_Message[i])
    wb.save("F:/test/test.xlsx")
    print("写入成功!")