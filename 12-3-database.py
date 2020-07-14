# 데이터 수정 삭제

import sqlite3

conn = sqlite3.connect('D:/Github/Repository/python-playground/resource/database.db')
c = conn.cursor()

c.execute("UPDATE users SET username = ? WHERE id = ?", ('papion2',2))
c.execute("UPDATE users SET username = :name WHERE id = :id", {"name":'papion5', "id":5})
c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('papion3', 3))

conn.commit()

for user in c.execute("SELECT * FROM users"):
    print(user)

print()

# delete
c.execute("DELETE FROM users WHERE id = ?", (2,))
c.execute("DELETE FROM users WHERE id = :id", {"id":5})
c.execute("DELETE FROM users WHERE id = '%s'" % 4)

for user in c.execute("SELECT * FROM users"):
    print(user)

print(conn.execute("DELETE FROM users").rowcount)

conn.commit()

