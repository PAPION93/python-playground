
#import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# if
name = 'jun'
if name == 'jun':
    print('my name is jun')

# for
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i, j), i*j)

# function
def hello():
    print("Hello")

hello()

# class 
class Cookie:
    pass 

# object
cookie = Cookie()

print(id(cookie))
print(dir(cookie))