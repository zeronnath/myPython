### traveller's [x, y]
# n = int(input())
# course = input().split()
# x=1
# y=1
# for i in range(len(course)):
#     move = course[i]
#     if move == 'L':
#         if x > 1:
#             x -=1
#     elif move == 'R':
#         if x<n:
#             x +=1
#     elif move == 'U':
#         if y>1:
#             y -=1
#     else:
#         if y<n:
#             y+=1
#     print(x, y)
# print('goal = ' ,x,y)



# # until n = 1
# # repeat one of the followings
# # 1. n /= k
# # 2. n -= 1

# n, k = map(int, input().split())
# target= count= 0
#
# while(n>=k):
#     # count of "n-=1" operations to reach the target, which enables "n /= k"
#     target = n//k * k
#     count += n - target
#
#     n //=k
#     count+=1
#     print('1 count=',count)
#
# # target < k
# if n>1:
#     count += target - 1
#
# #print('f count=',count)
