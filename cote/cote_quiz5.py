
### Q6
# def factorial(num):
#     if num > 1:
#         print(num , " * ", end="" )
#         return num * factorial(num-1)
#     else:
#         print(1)
#         return 1
#
# print(factorial(5))

# ### Q4
# def binary_search(data, search):
#     if len(data) == 1 and search == data[0]:
#         print("a=", data[0])
#         return True
#     if len(data) == 1 and search != data[0]:
#         print ("a=", data[0])
#         return False
#     if len(data) == 0:
#         return False
#
#     medium = len(data) // 2
#     if search == data[medium]:
#         print("a=", data[medium])
#         return True
#     elif search > data[medium]:
#             return binary_search(data[medium:], search)
#     else:
#         return binary_search(data[:medium],search)
#
# print(binary_search([1,2, 4,5,6,7,9,11],6))

### Q9 Quick Sort
def quicksort(data_list):
    if len(data_list) <= 1:
        return data_list
    pivot = data_list[0]
    left = [item for item in data_list[1:] if pivot > item]
    right = [item for item in data_list[1:] if pivot <= item]

    return quicksort(left) +  [pivot] + quicksort(right)

data_list = [50,90,1,14,8,21,65]
print(quicksort(data_list))