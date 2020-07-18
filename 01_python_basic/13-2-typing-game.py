# 타이핑 게임
# DB, sound 추가

import random
import time

# sound
import winsound
import sqlite3
import datetime


# DB 생성 & Auto Commit
conn = sqlite3.connect('D:/Github/Repository/python-playground/resource/game-records.db', isolation_level=None)

# cursor
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regdate text)")

words = []
n = 3 # 게임시도횟수
cor_cnt = 0 # 정답 개수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

# print(words) # 리스트 확인

input("Ready? Press Enter")
start = time.time()

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)
    print()

    print("*Question# {}".format(n))
    print(q)

    x = input()
    print()

    if str(q).strip() == str(x).strip():
        print("Pass!")
        winsound.PlaySound("./sound/good.wav", winsound.SND_FILENAME)
        cor_cnt += 1
    else:
        print("Worng!")
        winsound.PlaySound("./sound/bad.wav", winsound.SND_FILENAME)

    n+=1

end = time.time()
et = end - start

cursor.execute("INSERT INTO records ('cor_cnt', 'record', 'regdate') VALUES (?, ?, ?)", (cor_cnt, et, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

print("걸린시간: ", et, "정답개수 : ", cor_cnt)

if __name__ == '__main__':
    pass