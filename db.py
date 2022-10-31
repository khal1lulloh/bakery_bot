import sqlite3

class Sql:
        def __init__(self):
                self.connection = sqlite3.connect('tort.db')
                self.cursor = self.connection.cursor()

        def tablitsa_yaratish(self):
                self.cursor.execute("""
        		CREATE TABLE IF NOT EXISTS baza (
        		user_id integer,
                        username varchar(60)
                        )
                        """)
        def tablitsa_qushish(self, user_id, username):
                self.cursor.execute("INSERT INTO baza VALUES ({},'{}')".format(user_id,username))
                return self.connection.commit()
        def id_user(self,user_id):
                self.cursor.execute(f"SELECT user_id FROM baza WHERE user_id = {user_id}")
                data = self.cursor.fetchone()
                return data
        def rec(self):
                self.cursor.execute(f"SELECT * FROM baza")
                idila = self.cursor.fetchall()
                return idila
        def userlar(self):
                self.cursor.execute(f"SELECT COUNT(user_id) FROM baza")
                info = self.cursor.fetchall()
                r = None
                for i in info:
                        r = i[0]
                return r