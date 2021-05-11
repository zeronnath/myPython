### ds ass1-1
def odd_even(a: int, b: int):
    #a, b = map(int, input().split())
    c = a ** 2
    d = b ** 2
    str = ''
    if (c + d) % 2 != 0:
        str = '홀수'
    else:
        str = '짝수'
    print(f"{c} + {d} = {str}")

odd_even(3,5)

### ds ass1-2

class Person( ):
    name='n'
    age=0
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name, self.age)
    pass

class Child(Person) :
    def play(self):
        print('{} is playing ' .format(self.name ) )
person = Person('Liam', 21)
person.show()
kid = Child('Olivia','8')
kid.show()
kid.play()
print(dir(kid))