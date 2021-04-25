print(' ㅡㅡㅡ practice hard !! ㅡㅡ build your skills !! ㅡㅡㅡ')


### 책: 이것이 코딩 테스트다

### recursive : factorial

def iterative_factorial(n):
    s=1
    for i in range(n, 0, -1):
        s = s * i
        print(f'{i} * ', end='')
    print()
    return s


def recursive_factorial(n):
    if n == 1:
        print(1)
        return 1

    print(f'{n} * ', end='')
    return n * recursive_factorial(n - 1)

while True :

    n = input() # input a number -> output factorial of the number
    if  n=='a' :
        break
    print(recursive_factorial(int(n)))
    print(iterative_factorial(int(n)))

