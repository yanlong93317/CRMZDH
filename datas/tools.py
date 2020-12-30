import xlrd


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
print(data_receivables_ex()[0])