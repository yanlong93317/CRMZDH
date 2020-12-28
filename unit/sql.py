import pymysql             #引入pynysql数据库
def hhh():
    connect = pymysql.connect(
        host= 'localhost',       #数控库服务器地址，localhost表示beji
        port= 3306,               #数据库端口
        user='root',           #数据库账户
        password= '',           #数据库密码
        db= 'ecshop',           #数据库名称
        charset= 'utf8',         #设置编码格式
        cursorclass= pymysql.cursors.DictCursor   #已字典形式返回结果
    )
    cursor = connect.cursor()   #组建游标
    sql = 'SELECT * FROM ecs_user'     #写入查询语句
    cursor.execute(sql)     #执行查询语句
    data = list(cursor.fetchall())    #获取所有数据
    connect.close()       #关闭数据库
    list(data)   #将数据库转换为列表
    bb = []  #设置一个空列表
    for i in data:  #从列表data中取值
        bb.append(list(i.values()))   #将取出的值放入列表bb
    return bb  #返回值为一个列表
print(hhh())

