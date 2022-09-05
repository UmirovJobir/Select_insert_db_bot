import sqlite3

class DBHelper:
    def __init__(self):
        self.conn = sqlite3.connect('base.db', check_same_thread=False)
        self.cur = self.conn.cursor()

    def select_db(self):
        sql = "select * from client"
        self.cur.execute(sql)
        
        return self.cur


    def insert_bd(self, id, name):
        sql = f"insert into client values({id}, '{name}')"
        self.cur.execute(sql)
        self.conn.commit()


#data = DBHelper()
# data.insert_bd(id =5, name="")
#data.select_db()
