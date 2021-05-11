### 패캠 코테 ###
### ass1-1
print("\n\n### ASSIGNMENT 1-1\n")
str=''
for i in range (1,9):
    str += '*'
    if(i % 3 == 0):
        continue
    print(str)



### ass1-2
# lambda, list comprehension
### lambda
# a,b = map(int, input().split())
# print((lambda c,d: c+d)(a,b))

print("\n\n###ASSIGNMENT  1-2\n")
a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

### list comprehension
#a = [int(a[i]) + 1 for i in range(len(a))]

### lambda
a = list(map(lambda x: int(x) + 1, a))

print(a)




### ass1-3
# count elements in the list.
# 사전자료형 key:value ; data = dict()

print("\n\n### ASSIGNMENT 1-3\n")
# test case
a = ['base ball', 'basket ball', 'soccer', 'base ball', 'soccer', 'soccer',
     'basket ball', 'base ball', 'basket ball', 'soccer', 'basket ball', 'basket ball',
     'base ball', 'soccer', 'soccer', 'basket ball', 'basket ball', 'base ball', 'base ball']

# test input-data
# a = (input().split(', '))
# print(a)

sports = dict()
for sport in a :
    if sport not in sports:
        sports[sport] = 1
    else:
        sports[sport] +=1


for key,value in zip(sports.keys(), sports.values()):
    print(key, value)



### ass1-4

print("\n\n### ASSIGNMENT 1-4\n")
print(0, end=' ')
for i in range(0, 9):
    print(2**i, end=' ')
print(256, end=' ')
print(256, end=' ')
