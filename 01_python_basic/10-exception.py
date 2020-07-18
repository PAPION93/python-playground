# 파이썬 예외 처리

# SyntaxError
# print('Test)

# NameError
a = 10
b = 15
# print(c)

# ZeroDivisionError
# print(10 / 0)

# IndexError
x = [1,2,3]
# print(x[3])

# KeyError
dic = {'name': 'kim'}
# print(dec['age'])
print(dic.get('hobby'))

# AttributeError : 모듈, 클래스에 잘못된 속덩 사용시 예외
import time
# print(time.month())

# ValueError
x = [1, 5, 9]
# x.remove(10)

# FileNotFoundError
# f = open('text.txt', 'r')

# TypeError
x = [1,2]
y = (1,2)
z = 'test'
# print(x + y)

# 예외처리
# try 에러가능성 있는 코드 실행, except 에러명1, 2, else 에러 미발생시, finally 항상

# ex1
name = ['Kim', 'Lee']
try:
    z = 'Son'
    x = name.index(z)
    print('{} found int! in name' .format(z, x+1))
except ValueError:
    print('Not found! ValueError')
else:
    print('OK! else!')
finally:
    print('Finally')


# ex
try:
    print('try')
finally:
    print('finally')

# ex
try:
    print('try')
except ValueError as error:
    print('ValueError', error)
except IndexError:
    print('IndexError')
except Exception:
    print('Exception')
finally:
    print('finally')

# ex
# raise
try:
    a = 'Kim'
    if a == 'Kim':
        print('Ok')
    else:
        raise ValueError
except ValueError:
    print('error Value')
except Exception as f:
    print(f)
else:
    print("OK")