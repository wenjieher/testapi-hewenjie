# -*- coding: utf-8 -*-

import xlrd, requests, json, xlutils,jsonpath
from xlutils.copy import copy
from APItest.inter import *
from APItest.sendmail import *

# 读取用例
excelDir = '/Users/wenjiehe/Documents/GitHub/testapi-hewenjie/APItest/hongkou2020test.xls'
# 打开表格
workbook = xlrd.open_workbook(excelDir, formatting_info=True)
print(workbook.sheet_names())
# 读取第一个sheet
# worksheet = workbook.sheet_names()[1]

worksheet = workbook.sheet_by_name('首页')
# 读取第一行
rows = worksheet.row_values(1)
print(rows)
# 复制
workbookWr = copy(workbook)
Wrsheet = workbookWr.get_sheet(0)
# 读取一列
# clox = worksheet.cell_value(1)
# print(clos)

# 读取指定单元格
for one in range(1,38):
    cellData = worksheet.cell_value(one, 6)
    urlData = worksheet.cell_value(one, 3)
    dy = worksheet.cell_value(one, 10)
    dyData = worksheet.cell_value(one, 11)
    #token = worksheet.cell_value(one, 7)
    #number1 = int(worksheet.cell_value(one,12))

    print(cellData)
    print(urlData)
    #print(token)
    print(worksheet.cell(one, 6).ctype)  # 单元格数据类型 0 1：字符串 2 3 4 5

    # 构建接口对应请求
    test_url = urlData
    test_data = cellData
    headers = {
            'Content-Type': 'application/json',
            'siteId':'18',
            'token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJjODE1NmM2MTU4Y2Q0MjQ3YTAzMGExNThkZDg1NjZkYzsxOCIsImlhdCI6MTU5MjYzNDYyMCwiZXhwIjoyMTExMDM0NjIwfQ.0O6eBB5CIKKG9dsZz-9akLGHiZFnSoDi3rIQ7iJClTtlju_hmyn1LFrRR4kIbMNDWtaJdhg4xJm3BRf9Rx3lCw'
            #'token': token
        }
    test_resp = requests.post(test_url, data=test_data, headers=headers)
    print(test_resp.text)
    print(headers)
    # token = test_resp.json()["data"]["access_token"]
    # print(token)
    res = test_resp.json()[dy]
    #res = token
    print(res)

    if res == dyData:
        print('成功')
        excel_res = 'pass'
    else:
        print('失败')
        excel_res = 'fail'
    result = test_resp.text

    # 写入结果
    # workbookWr = xlrd.open_workbook(excelDir)


    Wrsheet.write(one, 9, excel_res)
    Wrsheet.write(one, 8, result)


workbookWr.save('/Users/wenjiehe/Documents/GitHub/testapi-hewenjie/APItest/result-hongkou2020test.xls')
#发送邮件
#sen_email()














