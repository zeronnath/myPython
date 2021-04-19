print(' ㅡㅡㅡ 책: 이것이 코딩 테스트다 ㅡㅡㅡ')

### binary search
def binary_search(array, value, left_i, right_i):
    # find mid_i
    # compare with mid_i
    # recursive call - left side array XOR right side array

    mid_i = (left_i + right_i) // 2
    print('mid_i=', mid_i)
    if array[mid_i] == value:
        return mid_i
    elif value < array[mid_i]:
        return binary_search(array, value, left_i, mid_i - 1)
    elif value > array[mid_i]:
        return binary_search(array, value, mid_i + 1, right_i)

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(binary_search(array, 5, 0, 20))


###  fast input for big data

import sys
input_data = 'asdf'
while(input_data!='000'):

    # input_data = input().rstrip()

    # in case of data size over 10 millions
    input_data = sys.stdin.readline().rstrip()
    print(input_data)