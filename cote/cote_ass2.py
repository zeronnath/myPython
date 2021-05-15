### cote ass2-1

import csv
f =  open('a.csv', 'r')
try:

    s = 0
    contents =  csv.reader(f, delimiter=',')# quoting=csv.QUOTE_NONNUMERIC)
    for row in contents:
        for r in row:
            s +=int(r)
    print(s)
finally:
    f.close()


### cote ass2-4

# class Foo:
#     bar = 'A'
#     def __init__(self):
#         self.bar = 'B'
#
#     class Bar:
#         bar = 'C'
#         def __init__(self):
#             self.bar = 'D'
# print (Foo.bar)
# print (Foo().bar)
# print (Foo().Bar.bar)
# print (Foo.Bar().bar)

# print(Foo.bar)  # A 출력
# print(Foo().bar)  # B 출력
# print(Foo.Bar.bar)  # C 출력
# print(Foo.Bar().bar)  # D 출력

#
# ### cote ass 2-2
#
# class Median:
#     listA = list()
#
#     def __init__(self):
#         pass
#
#     def get_item(self, item):
#         self.listA.append(item)
#
#     def clear(self):
#         self.listA.clear()
#
#     def show_result(self):
#         self.listA.sort()
#         print(self.listA)
#
#         size = len(self.listA)
#         if size % 2 == 0 :
#             print("median = " , (self.listA[size//2-1] + self.listA[size//2]) / 2 )
#         else:
#             print("median = " , self.listA[size//2])
#
#
#
#
# median = Median()
# for x in range(10):
#     median.get_item(x)
# median.show_result()
#
# median.clear()
# for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
#     median.get_item(x)
# median.show_result()

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' cannot speak.')

    def move(self):
        print(self.name + ' cannot move.')


class Dog(Animal):
    def move(self):
        print(self.name + ' moves like a jagger.')


class Retriever(Dog):
    def speak(self):
        print(self.name + ' is smart enough to speak.')

dog = Dog('Nancy')
dog.speak()
dog.move()

super_dog = Retriever('Michael')
super_dog.speak()
super_dog.move()

# 출력
# Nancy cannot speak.
# Nancy moves like a jagger.
# Michael is smart enough to speak.
# Michael moves like a jagger.

