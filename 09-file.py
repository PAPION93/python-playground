# 파일 읽기, 쓰기

# ex1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
f.close()

print("========================")

# ex2
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print("========================")

# ex3 
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())

print("========================")

# ex4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()
    print(">", content)

print("========================")

# ex5 
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end='####')
        line = f.readline()

print()
print("========================")
print()

# ex6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end= ' ***** ')

print()
print("========================")
print()

score = []
with open('./resource/score.txt')  as f:
    for line in f:
        score.append(int(line))
    print(score)

print('aver : {:6.3}'.format(sum(score)/len(score)))

# 파일 쓰기
with open('./resource/test1.txt', 'w') as f:
    f.write('hello\n')

with open('./resource/test1.txt', 'a') as f:
    f.write('hello2\n')


# ex
print()
from random import randint
with open('./resource/test2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write("\n")


# ex
# writelines : list -> file
with open('./resource/test3.txt', 'w') as f:
    list = ['1\n', '2\n', '3']
    f.writelines(list)

# like file log
with open('./resource/test4.txt', 'w') as f:
    print('test1', file=f)