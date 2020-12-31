# -*- coding: utf-8 -*-
# @Time : 2020/12/26 22:36
# @Author : zj12345
# @Email : 374680231@qq.com
# @File : tools.py
# @Project : CrmZDH.test
import xlrd


def data_Dl_ex():
    data = xlrd.open_workbook("../datas/crm_login.xlsx")
    table = data.sheet_by_name("login")
    e_list = []
    for n_row in range(1, table.nrows):
        e_list.append(table.row_values(n_row))
    return (e_list)

def data_clue_ex():
    data = xlrd.open_workbook("../datas/crm_case_datas.xlsx")
    table = data.sheet_by_name("clue")
    e_list = []
    for n_row in range(1, table.nrows):
        e_list.append(table.row_values(n_row))
    return (e_list)

def data_task_ex():
    data = xlrd.open_workbook("../datas/crm_case_datas.xlsx")
    table = data.sheet_by_name("task")
    e_list = []
    for n_row in range(1, table.nrows):
        e_list.append(table.row_values(n_row))
    return (e_list)

def data_mail_ex():
    data = xlrd.open_workbook("../datas/crm_case_datas.xlsx")
    table = data.sheet_by_name("mail")
    e_list = []
    for n_row in range(1, table.nrows):
        e_list.append(table.row_values(n_row))
    return (e_list)

def data_notice_ex():
    data = xlrd.open_workbook("../datas/crm_case_datas.xlsx")
    table = data.sheet_by_name("notice")
    e_list = []
    for n_row in range(1, table.nrows):
        e_list.append(table.row_values(n_row))
    return (e_list)


