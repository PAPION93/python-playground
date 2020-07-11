
# 가을 과일 찾기
q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for key in q1:
    if key == "가을":
        print("Found", q1[key])

for k, v in q1.items():
    if k == "가을":
        print("Found", v)

# 사과 포함되었는지 확인
q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for v in q1.values():
    if v == "사과":
        print("exist")

print()

# 가장 큰수 찾기(if 사용)
a, b, c = 132, 63, 18
max = a
if b > a:
    max = b
if c > b:
    max = c
print('max = ', max)

# while or for 사용
# 정 을 제외하고 출력
q = ['갑', '정', '병', '정']
for val in q:
    if val == '정':
        continue
    print(val, end=' ')

print()
# 1 ~ 101 홀수 출력
for n in range(102):
    if n % 2 == 1:
        print(n, end=' ')

print()
print()