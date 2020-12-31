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


def data_Dl_ex():
    data = xlrd.open_workbook("../datas/crm_login.xlsx")
    table = data.sheet_by_name("login")
    e_list = []
    for n_row in range(1, table.nrows):
        e_list.append(table.row_values(n_row))
    return (e_list)


def data_product_ex():
    data = xlrd.open_workbook("../datas/crm_casedata.xlsx")
    table = data.sheet_by_name("product")
    e_list = []
    for n_row in range(1, table.nrows):
        e_list.append(table.row_values(n_row))
    return (e_list)


def data_receivables_ex():
    data = xlrd.open_workbook("../datas/crm_casedata.xlsx")
    table = data.sheet_by_name("receivables")
    e_list = []
    for n_row in range(1, table.nrows):
        e_list.append(table.row_values(n_row))
    return (e_list)




def data_knowledge_ex():
    data = xlrd.open_workbook("../datas/crm_casedata.xlsx")
    table = data.sheet_by_name("knowledge")
    e_list = []
    for n_row in range(1, table.nrows):
        e_list.append(table.row_values(n_row))
    return (e_list)
print(data_knowledge_ex()[1][3])


def data_clue_ex():
    data = xlrd.open_workbook("../datas/crm_casedata.xlsx")
    table = data.sheet_by_name("clue")
    e_list = []
    for n_row in range(1, table.nrows):
        e_list.append(table.row_values(n_row))
    return (e_list)


def data_task_ex():
    data = xlrd.open_workbook("../datas/crm_casedata.xlsx")
    table = data.sheet_by_name("task")
    e_list = []
    for n_row in range(1, table.nrows):
        e_list.append(table.row_values(n_row))
    return (e_list)


def data_mail_ex():
    data = xlrd.open_workbook("../datas/crm_casedata.xlsx")
    table = data.sheet_by_name("mail")
    e_list = []
    for n_row in range(1, table.nrows):
        e_list.append(table.row_values(n_row))
    return (e_list)


def data_notice_ex():
    data = xlrd.open_workbook("../datas/crm_casedata.xlsx")
    table = data.sheet_by_name("notice")
    e_list = []
    for n_row in range(1, table.nrows):
        e_list.append(table.row_values(n_row))
    return (e_list)








def data_systemsettings_ex():
    data = xlrd.open_workbook("../datas/crm_casedata.xlsx")
    table = data.sheet_by_name("systemsettings")
    e_list = []
    for n_row in range(1, table.nrows):
        e_list.append(table.row_values(n_row))
    return (e_list)
