print(' ㅡㅡㅡ practice hard !! ㅡㅡ build your skills !! ㅡㅡㅡ')

### 책: 이것이 코딩 테스트다

#  구현: 115p  Royal Knight

# in each location on the chessboard, validate whether
# a move is within the boundary
# for the 8 moves of the knight.
# 2->1 or 1->2
# 2 kinds of moves x 4 directions. = 8 kinds of moves

# interpret numeric coordinate into chessboard coordinate x->a~h, y->1~8
# x, y = map(int, input().split())
# nx = ny = 0
# count =0
#
# moves = [[2, 1], [2, -1], [-2, 1], [-2, -1],
#          [1, 2], [1, -2], [-1, 2], [-1, -2]]
#
# for i in range(len(moves)):
#     nx = x+ moves[i][0]
#     ny = y+moves[i][1]
#     if 1 <=  nx  <= 8 and 1 <= ny <= 8:
#         count +=1
# print('count=',count)




# ***** :  시분초 모든경우수 24x60x60 < 10만 연산 이하, 2초 내에.

###  count '3' in time
# h = int( input())
# c = 0
#
# for m in range(h+1):
#     for j in range(60):
#         for i in range(60):
#             if '3' in str(m)+str(j)+str(i):
#                 c+=1

#
# for m in range(n+1):
#     for l in range(6):
#         for k in range(10):
#             for j in range(6):
#                 for i in range(10):
#                     if i == 3:
#                         c += 1
#                 if j == 3:
#                     c += 1
#             if k == 3:
#                 c += 1
#         if l == 3:
#             c += 1
#     if n == 3:
#         c += 1
# print(c)

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


### minmal number of coins to compose an amount
#
# n = input()
# count=0
# remainder=int(n)
# coins = [500, 100, 50, 10]
# while(remainder>1):
#     for coin in coins:
#         q = remainder // coin
#         if q > 0:
#             count += q
#             remainder %= coin
#             break
#
#     print('remainder=', remainder)
# print('count=', count)
