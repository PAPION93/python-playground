# 파이썬 함수식 및  람다
# 함수 정의방법
# def name(parameter):
#   code

# 호출
# name(parameter)

def hello(world):
    print("hello ", world)

hello("world")

# return
def hello_return(val):
    return val

str = hello_return(9)
print(str)

# 다중 리턴
def return_multi(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300

    return y1, y2, y3

x, y, z = return_multi(10)
print(x,y,z)

# args, *kwargs
def args_func(*args):
    # for t in args:
    #     print(t, end=' ')
    for i,v in enumerate(args):
        print(i, v, end=' ')
    print()

args_func('kim')
args_func('kim', 'park')

# kwargs
def kwargs_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

kwargs_func(name1="kim", name2="son")

# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20,)
example_mul(10, 20, 'park', 'kim', age1=24, age2=26)

# 중첩함수(클로저)
def nested_func(num):
    def func_in_func(num):
        print('>>>', num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)

# 
def func_nul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300

    return y1, y2, y3

print(func_nul3(5))
print()
print()
# 람다식 예제
# 람자식 : 메모리절약, 가도성 향상, 간결 코드
# 함수는 객체 생성 -> 리소스 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화
def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10
print(var_func)
print(type(var_func))

lambda_mul_10 = lambda num: num * 10
print(lambda_mul_10(10))

def func_final(x, y, func):
    print(x * y * func(10))

func_final(10,10,lambda_mul_10)






