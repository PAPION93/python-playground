# 타이핑 게임
import random
import time


words = []
n = 1 # 게임시도횟수
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
        cor_cnt += 1
    else:
        print("Worng!")

    n+=1

end = time.time()
print(end - start, cor_cnt)

if __name__ == '__main__':
    pass