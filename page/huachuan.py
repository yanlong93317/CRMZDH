import xlrd


def loginuser(sheet,filename=None):
    if not filename:
        filename = "../datas/chuancrm_login.xlsx"
    date = xlrd.open_workbook(filename)
    table = date.sheet_by_name(sheet)
    nrow = table.nrows  # 获取行数
    ncol = table.ncols  # 获取列数
    return [table.row_values(line) for line in range(1, table.nrows)]
    # return table.row_values(1)
