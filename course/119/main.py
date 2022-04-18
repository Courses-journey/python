# import os
import sqlite3


db = sqlite3.connect("app.db")
# print(os.getcwd())

cr = db.cursor()

cr.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER,user_id INTEGER)")

cr.execute("CREATE TABLE IF NOT EXISTS users (name TEXT,user_id INTEGER)")


cr.execute("INSERT INTO users(name ,user_id ) VALUES('ali',1)")
cr.execute("INSERT INTO users(name ,user_id ) VALUES('ahmad',2)")
cr.execute("INSERT INTO users(name ,user_id ) VALUES('sayed',3)")
db.commit()

db.close()
