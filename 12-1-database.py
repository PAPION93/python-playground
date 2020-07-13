# database SQLite
# 테이블 생성 및 삽입

import sqlite3
import datetime

now = datetime.datetime.now()
print(now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

print(sqlite3.version)
print(sqlite3.sqlite_version)


# DB 생성 & Auto Commit
conn = sqlite3.connect('D:/Github/Repository/python-playground/resource/database.db', isolation_level=None)

# Cursor
c = conn.cursor()
print(type(c))

# create Table(Data Type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# insert
c.execute("INSERT INTO users VALUES(1, 'Jun', 'test@naver.com', '000111', 'test.com', ?)", (nowDatetime,))
c.execute("INSERT INTO users (id, username, email, phone, website, regdate) VALUES(?, ?, ?, ?, ?, ?)", (2, 'Son', 'email@eaf', '010-2345-1234', '.com', nowDatetime,))

# Many 삽입(튜플, 리스트)
userList = (
    (3, 'lee1', 'lee1@naver.com', '010-1234-1231', 'lee1.com', nowDatetime),
    (4, 'lee2', 'lee2@naver.com', '010-1234-1232', 'lee2.com', nowDatetime),
    (5, 'lee3', 'lee3@naver.com', '010-1234-1233', 'lee3.com', nowDatetime),
)

c.executemany("INSERT INTO users (id, username, email, phone, website, regdate) VALUES(?, ?, ?, ?, ?, ?)", userList)

# delete table
# print("users db deleted", conn.execute('DELETE FROM users').rowcount)

# commit : isolation_level = None(Auto commit)
# conn.commit()

# rollback
# conn.rollback()

# 접속
conn.close()