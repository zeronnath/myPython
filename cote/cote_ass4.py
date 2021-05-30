

# ### ass4-2 오른차순 N개의 정수, countUniques
# def countUniques(a):
#     cnt = 0
#     v = None
#     for i in range (len(a)) :
#         if( a[i] != v):
#             cnt += 1
#             v = a[i]
#     return cnt
#
# print(countUniques( [-1, 1, 1, 1, 1, 4, 4, 4, 4, 10, 14, 14] ))  # 5
# print(countUniques( [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] ))  # 2
#
#
# ### ass4-3 주어진 모든 문자열의 앞의 몇개의 문자가 일치하는지 출력하라

# def solution (items) :
#     tmp = items[0]
#     idx=0
#     for j in range (1, len(items)):
#         for i in range(0, len(tmp)):
#             check = tmp[0:i+1]
#             if items[j].find(check) >= 0:
#                 idx = i+1
#             else:
#                 break
#         tmp = tmp[0:idx]
#
#     return len(tmp)
#
# print(solution(['abced', 'abce', 'abcehg', 'abcefwqw', 'abcedfg']))  # 3
#
# print(solution(['dabcd', 'dadbce', 'dabchg', 'dabcfwqw', 'dabcdfg']))  # 0


# ### ass4-4 자연수 중, 각 자리수를 제곱한 것을 더하는 과정을 반복했을 때 1으로 끝나는 수를 '행복한 수'라고 한다.
# '행복한 수'가 아닌 경우 이 과정이 1에 도달하지 못하고 같은 수열이 반복되는 무한 루프에 빠지게 된다.
# 자연수를 입력받았을 때 '행복한 수'인지 판별하는 알고리즘을 작성하라.
#
# '행복한 수'를 찾는 과정의 예
#
#   19이 행복한 수인지 확인하는 과정
#   1^2 + 9^2 = 82
#   8^2 + 2^2 = 68
#   6^2 + 8^2 = 100
#   1^2 + 0^2 + 0^2 = 1 --> True
#
# def get_digit_cnt(num):
#     cnt = 1
#     if (num // 10 == 0):
#         return 1
#     else:
#         while num // (10 ** cnt) > 0:
#             cnt += 1
#
#     return cnt
#
#
# def solution(num):
#     nums = list()
#     nums.append(num)
#
#     while(True):
#
#         result = 0
#         digit_cnt = get_digit_cnt(num)
#         array = [0] * digit_cnt
#
#         for i in range(0, digit_cnt):
#             if i == 0:
#                 array[0] = (num % 10) ** 2
#             else:
#                 array[i] = ((num // (10 ** i)) % 10)** 2
#             result += array[i]
#
#         print(result, end='\n')
#
#         if (result == 1):
#             return True
#
#         for i in range(len(nums)):
#             if result == nums[i]:
#                 return False
#         nums.append(result)
#         num = result
#
#
#     return False
#
# print(solution(19))
# print(solution(7))
# print(solution(91))
# print(solution(10))

## ass4-1  PriorityQueue
# Min Heap 자료구조를 이용하면 최대값을 O(logN)의 시간복잡도로 찾을 수 있다.
# Min Heap을 이용하면 우선순위 값이 낮은 자료를 먼저 출력하는 Priority Queue를 구현할 수 있다.
import heapq
from multiprocessing import heap


class PriorityQueue:

    def __init__(self):
        self.ls = list()
        self.heap_ = []
        self.dict_ = dict()

    def is_empty(self):
        if len(self.heap_) == 0:
            return True
        else:
            return False

    def put(self, data):
        key, value = data[0], data[1]
        self.dict_[key] = value
        heapq.heappush(self.heap_, key)



    def get(self):
        if not self.is_empty():
            key = heapq.heappop(self.heap_)
            value = self.dict_[key]
            return value

    def peek(self):
        if not self.is_empty():
            return self.dict_[self.heap_[0]]


pq = PriorityQueue()

print(pq.is_empty())
print("pq.heap_ = ",pq.heap_)
pq.put((0, 'a'))
pq.put((5, 'b'))
pq.put((2, 'c'))
pq.put((1, 'd'))
pq.put((3, 'e'))
pq.put((4, 'f'))
print("pq.heap_ = ",pq.heap_)

print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.peek())
print(pq.peek())

print(pq.get())
print(pq.peek())
print(pq.get())
print(pq.peek())
print(pq.get())