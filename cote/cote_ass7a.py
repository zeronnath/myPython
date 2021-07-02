### ass7-4
# 2개의 단어 beginWord와 endWord, 그리고 여러개의 단어 wordList가 주어졌을 때,
# beginWord에서 endWord로 변환하기 위해 필요한 가장 적은 변환 횟수를 구하시오.
#
#     변환 조건
#         단어는 wordList에 있는 단어로만 변환할 수 있다.
#         단어를 변환할 때에는 한번에 하나씩의 문자만 바꿀 수 있다.
#
#     문제 조건
#         endWord로의 변환이 불가한 경우에는 0을 출력하시오.
#         문제에 등장하는 모든 단어의 길이는 같으며, 알파벳 소문자로만 이루어져 있다.
#         wordList에는 겹치는 단어가 없다.
#         beginWord와 endWord는 같은 단어로 주어지지 않는다.
#
# ### 예시 입력1
#
# 입력:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# 출력: 5
#
# 설명: 가장 짧은 변환 방법은 "hit" -> "hot" -> "dot" -> "dog" -> "cog"이다.
#
# ### 예시 입력2
#
# 입력:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# 출력: 0
#
# 설명: endWord인 "cog"가 wordList에 없으므로, endWord로 변환할 수 있는 방법이 없다.
#
# def is_right(s1, s2):
#     s_size = len(s1)
#     cnt = 0
#     for i in range(s_size):
#         if s1[i] != s2[i]:
#             cnt += 1
#     return True if cnt == 1 else False
#
#
# def solution(begin: str, target: str, words: list):
#     answer = 0
#     temp = 0
#     is_visited: list = []
#     graph_row: list = [0] * len(words)
#     v: list = []
#
#     for i in range(0, len(words)):
#         is_visited.append([0] * len(words))
#
#     for i in range(0, len(words)):
#         if is_right(begin, words[i]):
#             v.insert(0, i)
#             if words[i] == target:
#                 return 1
#
#     while v:
#         # store the front value of the queue
#         front = v[0]
#         v.pop(0)
#         temp += 1
#
#         # in case of meeting the target node, store the temp at answer and end the search
#         if words[front] == target:
#             answer = temp
#             break
#
#         # among the front, store into the queue the unvisited meeting the requirement and check visitness
#         for i in range(0, len(words)):
#             if is_right(words[i], words[front]) \
#                     and is_visited[i][front] == 0 \
#                     and is_visited[front][i] == 0:
#                 v.insert(0, i)
#                 is_visited[i][front] = 1
#                 is_visited[front][i] = 1
#
#     return answer
#
#
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
# print(solution(beginWord, endWord, wordList))

### ass7-1
# def solution(numbers):
#     numbers.sort(key=lambda x: (str(x)*3), reverse=True)
#     answer = ''.join(str(s) for s in numbers)
#     return str(int(answer))
#
# numbers = [6,10,2]
# print(solution(numbers))
#
# numbers = [3,30,34,5,9]
# print(solution(numbers))


### ass7-2
# 여러 개의 구간이 리스트 intervals로 주어졌을 때, 겹치는 구간을 모두 병합하여 출력하시오.
#
# 입력 예시1
#
# 입력: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 출력: [[1,6],[8,10],[15,18]]
# 설명: 구간 [1,3]와 [2,6]이 겹치므로, [1,6]으로 병합하였다.
#
# 입력 예시 2
#
# 입력: intervals = [[1,4],[4,5]]
# 출력: [[1,5]]
# 설명: 구간 [1,4]와 [4,5]는 겹치는 것으로 간주한다.
from typing import List


def solution(intervals: List[List[int]]) -> List[List[int]]:
    merged = []

    # Sort before checking overlaps
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    for arr in sorted_intervals:
        # in case that arr's start is in the interval
        if merged and arr[0] <= merged[-1][1]:
            # update merged's end with the later-end one between arr's end and merged's end
            merged[-1][1] = max(merged[-1][1], arr[1])
        else:
            merged += [arr]

    return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(solution(intervals))
intervals = [[1, 4], [4, 5]]
print(solution(intervals))
