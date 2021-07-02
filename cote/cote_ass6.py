# ### ass6-1
#
# def solution(n, k):
#     num1 = n
#     idx = [0]
#     answer = []
#     picked = []
#
#     def recur(idx, answer):  # basecase
#         if len(picked) == num1:
#
#             idx[0] = idx[0] + 1
#             # print(idx[0], picked)
#             if idx[0] == k:
#                 print("MATCH = ", picked)
#                 answer.extend(picked)
#                 return answer
#             return
#
#         for i in range(1, num1 + 1):
#             if i not in picked:  # 1 pick
#                 picked.append(i)
#                 recur(idx, answer)
#                 if idx[0] == k:
#                     break;
#                 picked.pop()
#
#     recur(idx, answer)
#     return answer
#
#
# n = 4
# k = 9
# print(solution(n, k))


# ### ass6-2
# def solution(N, number):
#     S = [0, {N}]
#     for i in range(2, 9):
#         temp_set = {int(str(N) * i)}
#         for i_half in range(1, i // 2 + 1):
#             for x in S[i_half]:
#                 for y in S[i - i_half]:
#                     temp_set.add(x + y)
#                     temp_set.add(x - y)
#                     temp_set.add(y - x)
#                     temp_set.add(x * y)
#                     if x != 0:
#                         temp_set.add(y // x)
#                     if y != 0:
#                         temp_set.add(x // y)
#         if number in temp_set:
#             return i
#         S.append(temp_set)
#     return -1
#
#
# print(solution(5, 12)) #4
# print(solution(2, 11)) #3


### ass6-3
# n개의 정수로 이루어진 리스트 nums와 정수 target이 주어졌을 때,
# nums에 있는 정수 4개를 합하여 target을 만들 수 있는 모든 조합을 구하시오.
# 단, 정답에는 동일한 정수 조합이 여러개 포함되어서는 안된다.
#

## 미검증
# def solution(nums, target):
#     answer_list = [0]
#     for num in nums:
#         node_list = []
#         for answer_list_elem in answer_list:
#             node_list.append(answer_list_elem + num)
#             node_list.append(answer_list_elem - num)
#         answer_tree = answer_list_elem
#     answer = answer_list.count(target)
#     return answer_list
#
# nums = [1, 0, -1, 0, -2, 2]
# target = 0
# print(solution(nums, target))

### 미검증
# def solution(numbers, target):
#     if not numbers and target == 0 :
#         return numbers
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


#
# def solution(numbers, target):
#     tree = [0]
#     for num in numbers:
#         sub_tree = []
#         for tree_num in tree:
#             sub_tree.append(tree_num + num)
#             sub_tree.append(tree_num - num)
#         tree = sub_tree
#     return tree
#
# nums = [1, 0, -1, 0, -2, 2]
# target = 0
# print(solution(nums, target))
#
#
# def solution(x):
#     numbers = x
#     left = 0
#     right = len(numbers) - 1
#     while left < right:
#         mid = (right + left) // 2
#         if numbers[mid] < numbers[mid + 1]:
#             left = mid + 1
#         else:
#             right = mid
#     return numbers[left]
#
#
# nums = [-4, -4, -2, 0, 0, 2, 4, 5, 6, 3, 2, -4, -6]
# print(solution(nums))
# nums = [-1, -1, -1, -1, 0, 1, 20, 19, 17]
# print(solution(nums))


### ass6-5 : DFS 방문 순서대로 출력
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
#
#     입력: 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
#     다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
#     입력으로 주어지는 간선은 양방향이다.
#
#     출력: V부터 방문된 점을 순서대로 출력한다.

# def solution(N, M, V, edges):
#     visit_list = [0] * (N + 1)
#     matrix = [[0] * (N + 1) for _ in range(N + 1)]
#
#     for i in range(M):
#         from_n = edges[i][0]
#         to_n = edges[i][1]
#         matrix[from_n][to_n] = matrix[to_n][from_n] = 1  # 양방향
#
#     def dfs(start):
#         print(start, end=' ')
#         visit_list[start] = 1
#
#         for i in range(1, N + 1):
#             if visit_list[i] == 0 and matrix[start][i] == 1:  # 아직 방문안했는데 방문해야할 곳
#                 dfs(i)
#
#     dfs(V)
#
#
# N, M, V = 4, 5, 1
# edges = [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]
# solution(N, M, V, edges)
# print()
#
# N, M, V = 8, 9, 1
# edges = [[1, 2], [2, 3], [2, 4], [3, 4], [4, 5], [5, 7], [5, 8], [7, 8], [1, 6]]
# solution(N, M, V, edges)
