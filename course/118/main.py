# import os
import sqlite3


db = sqlite3.connect("app.db")
# print(os.getcwd())

db.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER,user_id INTEGER)")

db.close()