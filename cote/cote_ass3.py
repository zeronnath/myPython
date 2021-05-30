# ### ass3-1 : Linked Queue Implementation  ###
#
# class Node:
#     def __init__(self, data, prev=None, next=None):
#         self.data = data
#         self.prev = prev
#         self.next = next
#
#
# class LinkedQueue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#
#     def is_empty(self):
#         if self.front is None:
#             return (True)
#         else:
#             return (False)
#
#     def put(self, data):
#         new_node = Node(data)
#         if self.front is None:
#             self.front = new_node
#             self.rear = new_node
#         else:
#             new_node.prev = self.rear
#             self.rear.next = new_node
#             self.rear = new_node
#
#     def get(self):
#         if (self.front is None):
#             return None
#         else:
#             result = (self.front.data)
#
#             if(self.front.next is not None):
#                 next_ = self.front.next
#                 next_.prev = None
#                 temp = self.front
#                 self.front = next_
#                 temp.next = None
#                 temp.prev = None
#             else:
#                 self.front = None
#                 self.tail = None
#
#             return result
#
#     def peek(self):
#         if (self.front is None):
#             return (None)
#         else:
#             return (self.front.data)
#
#
# queue = LinkedQueue()
#
#
# ###Test code
# queue = LinkedQueue()
#
# print(queue.is_empty())
# for i in range(10):
#     queue.put(i)
# print(queue.is_empty())
#
# for _ in range(11):
#     print(queue.get(), end=' ')
# print()
#
# for i in range(20):
#     queue.put(i)
# print(queue.is_empty())
#
# for _ in range(5):
#     print(queue.peek(), end=' ')
# print()
#
# for _ in range(21):
#     print(queue.get(), end=' ')
# print()
# print(queue.is_empty())

#
# ### ass3-2 : stack
# class Stack:
#     def __init__(self):
#         self.list = list()
#
#     def push(self, data):
#         self.list.append(data)
#
#     def pop(self):
#         return self.list.pop()
#
#
# class Calculator:
#     def __init__(self):
#         self.stack = Stack()
#
#     def calculate(self, string):
#         args = string.split()
#         result = 0
#         op = ''
#
#         for i in range(0, len(args)):
#
#             if (i == 0):
#                 self.stack.push(args[i])
#             elif (int(i) % 2 == 1):
#                 self.stack.push(args[i])
#             elif (i % 2 == 0):
#                 op = args[i]
#                 b = self.stack.pop()
#                 a = self.stack.pop()
#                 result = 0
#                 if (op == '+'):
#                     result = int(a) + int(b)
#                 elif (op == '-'):
#                     result = int(a) - int(b)
#                 elif (op == '*'):
#                     result = int(a) * int(b)
#                 elif (op == '/'):
#                     result = int(a) / int(b)
#                 self.stack.push(result)
#
#         return self.stack.pop()
#
#
# # Test code
# calc = Calculator()
# print(calc.calculate('10 5 + 2 * 3 /'))
# print(calc.calculate('4 6 * 2 / 2 +'))
# print(calc.calculate('2 5 + 3 * 6 - 5 * '))


### ass-3-4 : chained hashtable

def hash_func(key):
    return ord(key[0]) % 10


class HashTable:
    def __init__(self):
        self.table = [None] * 10

    def set(self, key, value):
        self.table[hash_func(key)] = value

    def get(self, key):
        return self.table[hash_func(key)]


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None


class ChainedHashTable(HashTable):


    def set(self, key, value):
        node = Node(key, value)
        hash = hash_func(key)
        if (self.table[hash] is None):
            self.table[hash] = node
        else:
            curnode = self.table[hash]
            if (curnode.key == key):
                node.data = value
            else:
                while (curnode.next):
                    curnode = curnode.next
                    if (curnode.key == key):
                        curnode.data = value
                        return
                curnode.next = node


    def get(self, key):
        hash = hash_func(key)
        if (self.table[hash] is not None) :
            node = self.table[hash]

            while node.key != key:
                node = node.next
            if (node is not None and node.key == key):
                return node.data


# Test code
if True:
    ht = ChainedHashTable()
    ht.set('hello', 1)
    ht.set('hello2', 2)
    ht.set('hello3', 3)
    ht.set('hello4', 4)

    print(ht.get('hello'), end=' ')
    print(ht.get('hello2'), end=' ')
    print(ht.get('hello3'), end=' ')
    print(ht.get('hello4'), end=' ')
    print()

    ht.set('hello2', 5)

    print(ht.get('hello'), end=' ')
    print(ht.get('hello2'), end=' ')
    print(ht.get('hello3'), end=' ')
    print(ht.get('hello4'), end=' ')

if True:
    ht = ChainedHashTable()
    ht.set('hello', 111)
    ht.set('hello2', 2)
    ht.set('hello2', 22)
    ht.set('hello3', 300)
    ht.set('hello4', 4444)
    ht.set('hello5', 50000)

    print()
    print(ht.get('hello'), end=' ')
    print(ht.get('hello2'), end=' ')
    print(ht.get('hello3'), end=' ')
    print(ht.get('hello4'), end=' ')
    print(ht.get('hello5'), end=' ')
    print()

    ht.set('hello2', 999)
    print(ht.get('hello'), end=' ')
    print(ht.get('hello2'), end=' ')
    print(ht.get('hello3'), end=' ')
    print(ht.get('hello4'), end=' ')
    print(ht.get('hello5'), end=' ')
    print()


### cote quiz 4 ###
str = 'FastCampus'
print(str[3:-1])