# 반복문 실습

print("while")
v1 = 1
while v1 < 11:
    print(v1)
    v1 += 1

print()
print("for")
for v2 in range(10):
    print(v2)

# 1 ~ 100 sum
sum1 = 0
cnt1 = 1
while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print(sum1)
print(sum(range(1, 101)))
print(sum(range(1, 101, 2)))

# list loop
# iterable : ragne, reversed, enumerate, filter, map, zip
names = ["Kim", "Son", "Park"]
for name in names:
    print("Your name is", name)

word = "dreams"
for s in word:
    print(s)

my_info = {
    "name" : "Jun",
    "age" : "292",
    "city": "NY"
}

for key in my_info:
    print(key)

for key in my_info.keys():
    print("Key:", key)

for value in my_info.values():
    print("value:", value)

for item in my_info.items():
    print("item:", item)

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())

# break
# for else
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in nums:
    print(num)
    if num == 11:
        print("found", num)
        break
else:
    print("Not found 11")

print()
print()
# continue
it = ['1', 2, 5, True, 5.4, complex(4)]
for v in it:
    if type(v) is float:
        print("found float")
        continue
    print(type(v))

