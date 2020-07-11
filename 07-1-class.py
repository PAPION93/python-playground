# class in Python
# self, class, instance

# 선언
# class 클래스명:
#     함수
#     함수

# 예제1
class UserInfo:
    def __init__(self, name):
        self.name = name

    def user_info_p(self):
        print("Name :", self.name)

user1 = UserInfo("jun")
user1.user_info_p()

user2 = UserInfo("jin")
user2.user_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)

# ex2
# self 의 이해
class SelfTest:
    def function1(): 
        print('function1 called')
    def function2(self): 
        print('function2 called')

self_test = SelfTest()
# self_test.function1()
SelfTest.function1()
self_test.function2()

# ex3
# class value, instance value
class WareHouse:
    # class value
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1

print()
print()
user1 = WareHouse("KIM")
user2 = WareHouse("KIM2")
user3 = WareHouse("KIM3")

print(user1.__dict__)
print(user3.__dict__)
print(user2.__dict__)
print(WareHouse.__dict__)

print(user1.name)
print(user2.name)
print(user3.name)
print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)

del user1

print(user2.stock_num)




