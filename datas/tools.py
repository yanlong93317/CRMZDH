# -*- coding: utf-8 -*-
# @Time : 2020/12/26 22:36
# @Author : zj12345
# @Email : 374680231@qq.com
# @File : tools.py
# @Project : CrmZDH.test
import xlrd


def data_Dl_ex():
    data = xlrd.open_workbook("../datas/ecshop.xlsx")
    table = data.sheet_by_name("houlogin")
    e_list = []
    for n_row in range(1, table.nrows):
        e_list.append(table.row_values(n_row))
    return (e_list)


print(data_Dl_ex())