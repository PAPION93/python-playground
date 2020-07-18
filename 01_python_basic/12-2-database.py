# 파이썬 데이터베이스(SQLite)

# 데이터 베이스 조회

import sqlite3
conn = sqlite3.connect('D:/Github/Repository/python-playground/resource/database.db')

# 커서 바인딩
c = conn.cursor()

# select
c.execute("SELECT * FROM users")

# 커서 위치 변경
# print('ONE -> \n', c.fetchone())

# 지정 로우 선택
# print("Three -> \n", c.fetchmany(size=3))

# All
# print("All -> \n", c.fetchall())

print()

# 순회1
# rows = c.fetchall()
# for row in rows:
#     print(row)

# 2
# for row in c.fetchall():
#     print(row)

# 3
# for row in c.execute("SELECT * FROM users ORDER BY id desc"):
#     print(row)

print()

# WHERE Retrieve1
param1 = (3,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall())

# 2
param2 = 4
c.execute('SELECT * FROM users WHERE id="%s"' % param2)
print('param2', c.fetchone())
print('param2', c.fetchall())

# 3
c.execute('SELECT * FROM users WHERE id=:Id', {"Id": 3})
print('param2', c.fetchone())
print('param2', c.fetchall())

# 4
param4=(3,5)
c.execute('SELECT * FROM users WHERE id IN(?,?)', param4)
print('param4', c.fetchall())

# 5
c.execute("SELECT * FROM users WHERE id IN('%d','%d')" % (3,5))
print('param5', c.fetchall())

# 5
c.execute("SELECT * FROM users WHERE id = :Id1 OR id = :Id2", {"Id1":2, "Id2": 5})
print('param6', c.fetchall())


# Dump 출력
with conn:
    with open('D:/Github/Repository/python-playground/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print complete')