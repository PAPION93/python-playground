# 조건문 실습

print(type(True))
print(type(False))

# ex 1
if True:
    print('Yes')

# ex 2
if False:
    print('No')

# ex 3
if False:
    print('No')
else:
    print('Yes')

# 연산자
# >, >=, <, <=, ==, !=
a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print()

str = ""
if str:
    print(True)
else:
    print(False)

print()
print()

# and or not
a = 100
b = 60
c = 15
print('and : ', a > b and b > c)
print('or : ', a > b or b > c)
print('not : ', not b > c)

print()
print()
print()

print('ex1 : ', 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'

if score1 <= 90 and score2 == 'A':
    print("pass")
else:
    print("fail")

print()
print()
num = 90
if num >= 90:
    print("A", num)
elif num <= 90:
    print("B", num)
else:
    print("C", num)

age = 27
height = 159
if age >= 20:
    if height >= 170:
        print("all pass")
    elif height >= 160:
        print("part pass")
    else:
        print("height fail")
else:
    print("age fail")