from flask import Flask, render_template, redirect, url_for, request
import numpy as np
from database import *  # 自己写的数据库函数的包
import random
import copy

# create Flask instance
app = Flask(__name__)
# username:学生名字
# password:学号
# depart:部门
# photo:头像
@app.route('/')
def index():
    return redirect(url_for('user_login'))


@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    # user information submitted methods must be POST
    if request.method == 'POST':  # 注册发送的请求为POST请求
        # get the user information that user submitted

        username = request.form['username']
        password = request.form['password']
        # if the information is correct(in our database)
        if is_existed(username, password):
            return render_template('init_game.html',nam = request.form['username'])#  成功登陆就去玩游戏
        else:
            login_massage = "Login Failed"
            return render_template('index.html', message=login_massage)     #账号不存在显示"Login Failed"
    return render_template('index.html')


@app.route("/register", methods=["GET", 'POST'])
def register():
    if request.method == 'POST':
        if is_existed(request.form['username'], request.form['password']):
            register_massage = "Register Failed"
            return render_template('register.html', message=register_massage)       #注册名字已存在显示"Register Failed"
        else:
            add_user(request.form['username'], request.form['password'], request.form['depart'], request.form['photo'])
            nn = request.form['username']
            return render_template('init_game.html',nam = nn)#  注册成功就去玩游戏
    return render_template('register.html')

@app.route("/judge_r", methods=["GET","POST"])
def judge_r():
    return render_template('judge_r.html')

@app.route("/judge_f", methods=["GET","POST"])
def judge_f():
    return render_template('judge_f.html')

@app.route("/game", methods=["GET","POST"])
def game():

    hang = get_hang()
    n = np.random.randint(1, hang + 1, size=1)[0]#1<=n<=hang 标准答案名字所在数据库中行数
    name = gain_namelist()     #名字列表
    random.shuffle(name)  # 随机排序后名字列表


    num = n - 1  # 标准答案名字所在列表索引
    pos = np.random.randint(0, 4, size=1)[0]  # 随机选取标准答案所在选项位置


    name_ori = copy.deepcopy(name)
    daan = name_ori[num]                #标准答案


    name.pop(num)
    samples = random.sample(name, 3)  # 三个错误选项
    n_1 = samples[0]
    n_2 = samples[1]
    n_3 = samples[2]

    option = [n_1, n_2, n_3, daan]   # 没被打乱的option
    random.shuffle(option)
    n1 = option[0]
    n2 = option[1]
    n3 = option[2]
    n4 = option[3]
    return render_template('game.html',nam = daan,n1 = n1,n2=n2,n3=n3,n4=n4)


if __name__ == "__main__":
    app.run()
