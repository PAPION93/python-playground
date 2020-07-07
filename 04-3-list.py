# 리스트, 튜블 

a = []
b = list()
c = [1, 2, 3 ,4]
d = [10, 100, 'a', 'b', 'c']
e = [10, 100, ['a', 'b', 'c']]

#indexing
print(d[2])
print(d[-2])
print(e[2][1])

# slicing
print(d[0:3])

# 연산
print(c + d)
print(c * 3)

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)

del c[1]
print(c)

y = [5, 4, 2, 3]
print(y)

y.append(9)
print(y)

y.sort()
print(y)    

y.reverse()
print(y)

y.insert(2, 1)
print(y)

y.remove(2)
print(y)

y.pop()
print(y)

# extend
x = [1,2,3]
y.extend(x)
print(y)


# tuple (수정 삭제가 불가능한 list)
a = ()
b = (1, )
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

# del error

print(c[2])
print(d[2][2])
print(d[2][0:2])

print(c + d)
print(c * 3)

# tuple func
z = (5, 1, 2, 4, 3)
print(z)
print(3 in z)
print(z.index(3))
print(z.count(1))