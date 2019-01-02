from flask import Flask, request

import pymysql

app = Flask(__name__)

class Mysql(object):

    def __init__(self):
        self.host = 'localhost'
        self.user = 'ip_user'
        self.password = 'password'
        self.db = 'ip'

    def conn(self):

        conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        return conn

@app.route('/')
def index():
    ip = request.remote_addr
    list = []
    list.append(ip)
    table_name = "ip_list"
    sql_1 = ' create table if not exists %s(`id` int UNSIGNED AUTO_INCREMENT,`ip` VARCHAR(20) ,primary key (`id`))ENGINE=InnoDB DEFAULT CHARSET=utf8;' % table_name
    sql_2 = 'truncate table ip_list'
    sql_3 = 'insert into ip_list(ip) values(%s)'
    conn = Mysql().conn()
    cursor = conn.cursor()
    cursor.execute(sql_1)
    cursor.execute(sql_2)
    cursor.execute(sql_3, list)
    conn.commit()
    cursor.close()
    conn.close()
    return(ip)

@app.route('/get')
def get():
    conn = Mysql().conn()
    cursor = conn.cursor()
    sql = 'select ip from ip_list'
    cursor.execute(sql)
    ip = cursor.fetchone()
    cursor.close()
    conn.close()
    return(ip)

if __name__ =="__main__":
    app.run()