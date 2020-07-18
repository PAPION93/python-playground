# string datatype
# 문자열 연산 및 슬라이싱

str1 = 'Hello'
str2 = "I am a boy."

print(len(str1), len(str2))

escape_str1 = "Do you have \"Money\"?"
print(escape_str1)

# raw string
raw_str1 = r'C:\Programs\Test\Bin'
print(raw_str1)

# string operate
str_oper1 = '*'
str_oper2 = 'abc'
str_oper3 = 'def'
print(str_oper2 + str_oper3)
print('a' in str_oper2)
print('d' in str_oper2)
print('d' not in str_oper2)

# string 형변환
print(str(77) + 'a')

# string func
a = 'hello'
b = 'bye'

print(a.islower())
print(a.endswith('o'))
print(a.capitalize())
print(a.replace('hello', 'hi'))
print(list(reversed(b)))

# slicing
print(a[0:3])
print(a[0:len(a)])
print(a[:])
print(a[0:5:2])
print(b[1:-1])
