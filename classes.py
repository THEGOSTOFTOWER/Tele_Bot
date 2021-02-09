import sqlite3


class Sqliter:
    def __init__(self, database):
        self.con = sqlite3.connect(database)
        self.cur = self.con.cursor()

    def add(self, user_id, address):
        return self.cur.execute("""INSERT INTO users(users_id, address) VALUES(?,?)""", (user_id, address,))

    def delete(self, user_id, address):
        return self.cur.execute("""DELETE FROM users WHERE user_id=? AND address=?""", (user_id, address,))

    def list(self, user_id):
        res = self.cur.execute("""SELECT address FROM users WHERE user_id=?""", (user_id,))
        a = []
        for i in res:
            for j in i:
                a.append(j)
        return a

    def in_in(self, user_id, address):
        return address in list(user_id)
