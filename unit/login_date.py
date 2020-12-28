import xlrd
def read_excel(filename=None):
    if not filename:
        filename="lgoin.xlsx"
    data=xlrd.open_workbook(filename)
    table=data.sheet_by_name("login")
    nrows=table.nrows   #获取行数
    ncols=table.ncols   #获取列数
    #返回列表
    # return  table.row_values(1)
    # ret_list=[]
    # for line in range(1,table.nrows):
    #     ret_list.append(table.row_values(line))
    # return ret_list

    # 列表生成式
    return [table.row_values(line) for line in range(1,table.nrows)]
print(read_excel())

