print(' ㅡㅡㅡ 책: 이것이 코딩 테스트다 ㅡㅡㅡ')

#### DFS

from collections import deque

def BFS(graph, v, visited):

    queue = deque()

    visited[v] = True
    queue.append(v)
    print(v, '->')

    while queue:
        current_node = queue.popleft()

        # queue not visited neighbors
        for neighbor_node in graph[current_node]:
            if not visited[neighbor_node] :
                queue.append(neighbor_node)
                visited[neighbor_node]=True
                print(neighbor_node, '->')

    return


graph = [
    [],     #node index 0
    [2,3,8],#node index 1
    [1,7],  #node index 2
    [1,4,5],#node index 3
    [3,5],  #node index 4
    [3,4],  #node index 5
    [7],    #node index 6
    [2,6,8],#node index 7
    [1,7]   #node index 8
]

visited = [False] * 9
visited[0] = True
v =1
BFS(graph, v, visited)
