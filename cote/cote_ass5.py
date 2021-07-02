# ### ass5-1
# def binary_search(data, search):
#     if len(data) == 1 and search == data[0]:
#         print("closest match =", data[0])
#         return True
#     if len(data) == 1 and search != data[0]:
#         print("closest match =", data[0])
#         return False
#     if len(data) == 0:
#         return False
#
#     medium = len(data) // 2
#     if search == data[medium]:
#         print("closest match =", data[medium])
#         return True
#     elif search > data[medium]:
#         return binary_search(data[medium:], search)
#     else:
#         return binary_search(data[:medium], search)
#
#
# def searchMatrix(matrix, target):
#     if len(matrix) < 1:
#         return False
#
#     row_cnt = len(matrix)
#     m = row_cnt // 2
#     middle_row = matrix[m]
#
#     if middle_row[0] <= target <= middle_row[-1]:
#         return binary_search(middle_row, target)
#     elif target > middle_row[-1]:
#         matrix_right = matrix[m + 1:]
#         return searchMatrix(matrix_right, target)
#     else:
#         matrix_left = matrix[: m]
#         return searchMatrix(matrix_left, target)
#
#
# matrix = [
#     [1, 3, 5, 7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 50]
# ]
#
# print(searchMatrix(matrix, 12))
# print(searchMatrix(matrix, 1))
# print(searchMatrix(matrix, 50))
# print(searchMatrix(matrix, 52))
# print(searchMatrix(matrix, 2))


### ass 5-4 판사
# trust array
# trusted_by array
# #
# def solution(N, trust):
#     cnt = N + 1
#     mx_trust = [[0 for i in range(cnt + 1)] for j in range(cnt + 1)]
#     length1 = len(trust)
#     for i in range(length1):
#         subject = trust[i][0]
#         object_ = trust[i][1]
#         mx_trust[subject][object_] = 1
#
#     trusted_by_all_cnt = 0
#     trust_none_cnt = 0
#     trust_none_candidates = list()
#     trusted_by_all_candidates = list()
#
#     for i in range(1, cnt):
#         for j in range(1, cnt):
#             mx_trust[i][cnt] += mx_trust[i][j]
#
#     for j in range(1, cnt):
#         for i in range(1, cnt):
#             mx_trust[cnt][j] += mx_trust[i][j]
#
#     for i in range(1, cnt):
#         if mx_trust[i][cnt] == 0:
#             trust_none_cnt += 1
#             trust_none_candidates.append(i)
#
#     for j in range(1, cnt):
#         if mx_trust[cnt][j] == N-1:
#             trusted_by_all_cnt += 1
#             trusted_by_all_candidates.append(j)
#
#     if len(trusted_by_all_candidates) == 1:
#         judge = trusted_by_all_candidates.pop()
#         if mx_trust[judge][cnt] == 0:
#             print("judge=",judge)
#             return judge
#
#     return -1
#
#
# N = 2
# trust =[[1,2]]
# print(solution(N, trust))
#
# N = 3
# trust = [[1,3],[2,3]]
# print(solution(N, trust))
#
#
# N = 3
# trust =[[1,3],[2,3],[3,1]]
# print(solution(N, trust))
#
# N = 3
# trust = [[1,2],[2,3]]
# print(solution(N, trust))
#
# N = 4
# trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# print(solution(N, trust))


### ass5-3
#
# from collections import deque
#
#
# def solution(n, edges):
#     routes = dict()
#     for e1, e2 in edges:
#         routes.setdefault(e1, []).append(e2)
#         routes.setdefault(e2, []).append(e1)
#
#     q = deque([[1, 0]])  # node number, depth
#     check = [-1] * (n + 1)
#     while q:
#         index, depth = q.popleft()
#         check[index] = depth
#         for i in routes[index]:
#             if check[i] == -1:
#                 check[i] = 0
#                 q.append([i, depth + 1])
#         depth += 1
#     return check.count(max(check))
#
#
# print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))


### ass5-2 최대공약 문자열
#
# public String gcdOfStrings4(String str1, String str2) {
#     if (str1.length() < str2.length()) {
#         return gcdOfStrings4(str2, str1);
#     }
#     if (str2.isEmpty()) {
#         return str1;
#     }
#     if (!str1.contains(str2)) {
#         return "";
#     }
#     str1 = str1.replace(str2, "");
#     return gcdOfStrings4(str2, str1);
# }

def gcdString(A, B):
    str1=A
    str2=B
    if len(str1) < len(str2) :
        return gcdString(str2, str1)
    if str2 == "":
        return str1
    if  str1.find(str2) < 0 :
        return ""

    str1 = str1.replace( str2, "")

    return gcdString(str2, str1)

print(gcdString("ababababab", "abab"))