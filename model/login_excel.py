import xlrd  # 引入Excel模块


def read_excel(filename=None):  # 设置一个函数
    if not filename:
        filename = "../datas/login.xlsx"  # 找到Excel文件并设置为变量
    data = xlrd.open_workbook(filename)  # 打开Excel文件
    table = data.sheet_by_name("login")  # 找到文件中具体需要的表并设置为变量
    nrows = table.nrows  # 获取行数
    ncols = table.ncols  # 获取列数
    return [table.row_values(line) for line in range(1, table.nrows)]  # 使用列表生成式生成列表，并返回从第2个到最后一个的所有数据


print(read_excel())
