import xlrd


def data_Dl_ex():
    data = xlrd.open_workbook("../datas/crm_login.xlsx")
    table = data.sheet_by_name("login")
    e_list = []
    for n_row in range(1, table.nrows):
        e_list.append(table.row_values(n_row))
    return (e_list)


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


print(data_receivables_ex()[0][:4])


def data_knowledge_ex():
    data = xlrd.open_workbook("../datas/crm_casedata.xlsx")
    table = data.sheet_by_name("knowledge")
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
