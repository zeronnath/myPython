# print(' ㅡㅡㅡ 책: 이것이 코딩 테스트다 ㅡㅡㅡ')
#
# ### 7-2. binary search - find parts
#
# # 1. sort parts
# # 2. binary-search the target parts
#
#
#
# def binary_search(array, target, left, right):
#     if left > right:
#         return None
#
#     mid = (left + right) // 2
#     if array[mid] == target:
#         return array[mid]
#
#     elif target < array[mid]:
#
#             return binary_search(array, target, left, mid - 1)
#
#     elif target > array[mid]:
#
#             return binary_search(array, target, mid + 1, right)
#
#     else:
#         return None
#
# parts = [99, 54, 67, 34, 33, 22, 21, 76, 15, 25, 18, 30, 62, 1, 2, 3, 45, 88]
# n = len(parts)
# targets = [67, 33, 76, 3, 45, 25,0 , -1, 1283,20 ]
#
# # 1. sort
# parts.sort()
#
# # 2. search
# for target in targets:
#     result = binary_search(parts, target, 0, n-1)
#     if result is not None:
#         print(f'{target}: ' + 'YES')
#     else:
#         print(f'{target}: ' + 'No')
#
#
#
# print(parts)
#
# #
# #
# # def binary_search(array, value, left_i, right_i):
# #     # find mid_i
# #     # compare with mid_i
# #     # recursive call - left side array XOR right side array
# #
# #     mid_i = (left_i + right_i) // 2
# #     print('mid_i=', mid_i)
# #     if array[mid_i] == value:
# #         return mid_i
# #     elif value < array[mid_i]:
# #         return binary_search(array, value, left_i, mid_i - 1)
# #     elif value > array[mid_i]:
# #         return binary_search(array, value, mid_i + 1, right_i)
# #
# # array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# # print(binary_search(array, 5, 0, 20))
# #

a  =  (map(int, input().split()))
print (a)