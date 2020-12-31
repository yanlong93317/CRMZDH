# -*- coding: utf-8 -*-
# @Time : 2020/12/31 11:28
# @Author : yanlong
# @Email : tangli@tmail.com
# @File : tools.py
# @Project : CRMZDH
import xlrd


def loginuser(sheet, filename=None):
    if not filename:
        filename = "../datas/crm_login.xlsx"
    date = xlrd.open_workbook(filename)
    table = date.sheet_by_name(sheet)
    nrow = table.nrows  # 获取行数
    ncol = table.ncols  # 获取列数
    return [table.row_values(line) for line in range(1, table.nrows)]
    # return table.row_values(1)


def datas(sheet, filename=None):
    if not filename:
        filename = "../datas/crm_casedata.xlsx"
    date = xlrd.open_workbook(filename)
    table = date.sheet_by_name(sheet)
    nrow = table.nrows  # 获取行数
    ncol = table.ncols  # 获取列数
    return [table.row_values(line) for line in range(1, table.nrows)]
    # return table.row_values(1)
