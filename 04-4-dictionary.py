# 딕셔너리, 집합 자료형

# Dictionary : like json 순서, 중복 없음
# init
a = {'name': 'Jun', 'ph': '01012341234', 'birth':930802}
b = {0: 'hello python'}
c = {'arr' : [1, 2, 3, 4, 5]}

print(type(a))

print(a['name'])
print(a.get('address'))
print(c['arr'][1:3])

a['address'] = 'daegu'
print(a)

a['rank'] = [1, 2, 3]
a['rank2'] = (1, 2, 3)
print(a)

print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))
print(1 in b)
print(1 not in b)

# 집합(Sets) 중복 불가
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)

t = tuple(b)
print(t)

l = list(b)
print(l)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print()
print()
print(s1.intersection(s2))
print(s1 & s2)

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

print()
print()
# 추가 & 제거
s3 = set([7, 8, 9, 10])
s3.add(7)
print(s3)