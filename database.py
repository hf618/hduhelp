import pymysql

config = {
    "host": "localhost",
    "user": "root",
    "password": "Dingge32420329",
    "db": "test"
}  # 连接服务器的信息

# create connection
conn = pymysql.connect(**config)  # 两个*表示是用字典解释参数(适用于有关键字的参数)
# create operator
cur = conn.cursor()


#重连MySql
def reConnect(sql):
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()




#添加用户
def add_user(username, password, depart,photo):
    # sql commands
    sql = "INSERT INTO user(username, password,depart,photo) VALUES ('%s','%s','%s','%s')" %(username, password,depart,photo) #改
    # execute(sql)
    #cur.execute(sql)



    # commit
    conn.commit()  # 对数据库内容有改变，需要commit()
    conn.close()
#获取表行数（学生人数）
def get_hang():
    sql = "select count(*) from user"

    reConnect(sql)
    cur.execute(sql)
    re = cur.fetchone()
    return int(re[0])
#判断是否名字学号重复
def is_existed(username,password):
    sql="SELECT * FROM user WHERE username ='%s' and password ='%s'"%(username,password)

    cur.execute(sql)
    result = cur.fetchall()
    if (len(result) == 0):
        return False
    else:
        return True
#生成名字列表
def gain_namelist():
    sql = "select * from user"
    reConnect(sql)
    cur.execute(sql)
    re = cur.fetchall()
    a = []
    hang = get_hang()
    for id in range(0, hang):
        a.append(re[id][1])
    return a
#生成所有字段列表
def gain_allist():
    sql = "select * from user"
    reConnect(sql)
    cur.execute(sql)
    re = cur.fetchall()
    all = []
    hang = get_hang()

    for id in range(0, hang):
        all.append(re[id])
    return all
