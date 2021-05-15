print("hello temp.py")

### data = dict()

key_list = {'apple', 'apple'}
value_list = {5, 3}
mapping = {}
for key, value in zip(key_list, value_list):
    mapping[key] = value

k_list = mapping.keys()
v_list = mapping.values()
dict_b = dict()
for k, v in zip(k_list, v_list):
    dict_b[k] = v
    print(k, v)

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

dict_c = dict()
dict_c['a'] = 1
k_list = dict_c.keys()
v_list = dict_c.values()
for k, v in zip(k_list, v_list):
    dict_c[k] = v

for v in dict_c:
    print(v)

dict_c['a'] = 2
dict_c['b'] = 3
k_list = dict_c.keys()
v_list = dict_c.values()
for k, v in zip(k_list, v_list):
    dict_c[k] = v

for k, v in zip(dict_c, dict_c.values()):
    print(k, v)

### default dict

from collections import defaultdict

dict_d = defaultdict(list)
dict_d['a'] = {'soccer', 'football'}

for k, v in zip(dict_d, dict_d.values()):
    print(k, v)

####### 람다
a = [0, 1, 2, 3, 4]
b =  lambda x: x * x
c = list()
for elem in a:
    print(elem)
    print(b)
    c.append(b(elem))
print(c)

####
d = [10,11,13,13]
print(d[::2])

#
print()
print()
print()
print()

print("adf"*3)


### **kwargs:가변 키밸류 인자수; *args 가변 인자수,
def f1(n1, n2=0, n3=0):
    s = n1+n2+n3
    return s
data = {
    'n2':20,
    'n3':35,
}
print (f1(2,**data))

