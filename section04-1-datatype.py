import math

# data type
v_str1 = "string"
v_bool = True
v_bool = False
v_float = 10.3

v_dict = {
    "name" : "Jun",
    "age" : 28
}

v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {3, 5, 7}


# print type
print(type(v_list))
print(type(v_tuple))
print(type(v_set))

int1 = 39
int2 = 989
bitInt1 = 99999999999999999
bitInt2 = 77777777777777777

f1 = 1.234
f2 = .6
f3 = 10.

print(int1 * int2)
print(f1 ** f2)
print(type(int1 + f1), int1 + f1)

# 형변환
print(int(int1 + f1))

y = 100
y += 100
print('y = %d' % y)

print(abs(-7))
n, m = divmod(100, 8)
print(n, m)

print(math.ceil(5.1))
print(math.floor(5.1))