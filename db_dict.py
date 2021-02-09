import sqlite3
import psycopg2

def create_connection(db_name, db_user, db_password, db_host, db_port):
    con = psycopg2.connect(database=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
    return con

def db_dict(database_name):
    con = sqlite3.connect(database_name)  # create_connection(*args)
    cur = con.cursor()
    res = cur.execute("""SELECT address, date FROM ___""").fetchall()
    a = {}
    for i in res:
        s = []
        for j in i:
            s.append(j)
        if s[1] not in a:
            a[s[1]] = [s[0]]
        else:
            a[s[1]].append(s[0])
    return a


def list_address(database_name):
    con = sqlite3.connect(database_name)  # create_connection(*args)
    cur = con.cursor()
    res = cur.execute("""SELECT address FROM ___""").fetchall()
    a = dict()
    a['дом'] = []
    a['улица'] = []
    s = []
    for i in res:
        for j in i:
            j = list(j)
            j.remove(')')
            j = ''.join(j)
            s = j.split('(')
            if s[1] == 'дом':
                a['дом'].append(s[0])
            else:
                a['улица'].append(s[0])
    return a
