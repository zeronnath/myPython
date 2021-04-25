print(' ㅡㅡㅡ 책: 이것이 코딩 테스트다 ㅡㅡㅡ')

### Fibonacci Sequence - Recursive & Memoization

def fibonacci(x):
    if x ==1 or x ==2 :
        return 1

    if d[x] != 0:
        return d[x]
    d[x] = fibonacci(x-2) + fibonacci(x-1)
    return d[x]

d = [0] * 100
print(fibonacci(36))



### Fibonacci Sequence - Iterative

def fibo(x):

    fibo_dptable[1] = 1
    fibo_dptable[2] = 1

    if x == 1 or x==2:
        return 1

    for i in range (3, x+1):
        fibo_dptable[i] = fibo_dptable[i-2]+fibo_dptable[i-1]

    return fibo_dptable[x]


fibo_dptable = [0]*100
print(fibo(99))
