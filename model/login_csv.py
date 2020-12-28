import csv #引入CSV模块
def readcsv():   #设置一个函数
    with open(file="../datas/login.csv") as fw:  #打开CSV文件，并命名
        date=csv.reader(fw)   #读取文件中的所有数据
        ree=[]      #设置一个空列表
        for line in date:    #循环读取data中的数据
            ree.append(line)     #将每一次读取到的数据放入列表
        return ree[1:]      #  返回列表从2个到最后一个的数据

print(readcsv())

