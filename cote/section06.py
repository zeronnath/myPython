# 함수 and lambda
# def func(param)"
#    code

# 함수 선언 위치 중요.

# 다중리턴 함수
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    return y1, y2


v1, v2 = func_mul(100)
print(type(v1), v1, v2)


# 매개변수갯수 불특정
def func_args(*args):
    for i, v in enumerate(args):
        print(i, v)


func_args('kim', 'park', 'son')


# 사전형 매개변수갯수 불특정
def func_kwargs(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


func_kwargs(first='kim', second='park', third='son')


# 가변인자 혼합
def func_complex(v1, v2, *args, **kwargs):
    print(v1, v2, args, kwargs)


func_complex(10, 20)
func_complex(100, 200, 'kim', 'park', first='theOne', second='theTwo')


# 중첩함수(클로저) nested function: 선언줄임, 메모리절약
def nested_func(num):
    def func_in_func(num):
        print('>>>', num)

    print('in func')
    func_in_func(num + 10000)


nested_func(10000)


# 람다: 메모리절약, 가독성향상, 코드줄임.
# 함수는 객체 생성 -> 메모리 할당 소모
# 람다는 즉시 실행(heap 초기화) -> 메모리 초기화

# 일반 함수 -> 변수 할당, 메모리 할당
def mul_10(num: int) -> int:
    return num * 10


var_func = mul_10
print(type(var_func), var_func)


# 람다 함수 -> 메모리 절약
def func_final(x, y, func):
    print('>>>', 10 * 10 * func(10))
    return 10 * 10 * func(10)+1
print(func_final(10, 10, lambda x: x * 1000))

lambda_func = lambda num: 2 ** num
print(lambda_func(10))