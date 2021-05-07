print(' ㅡㅡㅡ 책: 이것이 코딩 테스트다 ㅡㅡㅡ')

#### DFS 

### DFS search - recursive
#
# def DFS_recursive(graph, current_node, visited):
#
#     visited[current_node] = True
#     print(current_node, end=' -> ' )
#
#     # recursive call to not visited neighbor nodes
#     for neighbor_node in graph[current_node]:
#         if not visited[neighbor_node] :
#             DFS(graph, neighbor_node, visited)
#
# graph = [
#     [],     #node index 0
#     [2,3,8],#node index 1
#     [1,7],  #node index 2
#     [1,4,5],#node index 3
#     [3,5],  #node index 4
#     [3,4],  #node index 5
#     [7],    #node index 6
#     [2,6,8],#node index 7
#     [1,7]   #node index 8
# ]
#
# start_node = 1
# visited = [False]*9
# DFS_recursive(graph, start_node, visited)



### DFS stack - iterative

stack = list()
visited = [False] * 9 #  ignore index 0; use 1~8 for node 1~8
visited[0] = True
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

all_visited = False

i=1
visited[i]=True
stack.append(i)
last_node = 1
print(i, ' -> ', end='')

while not all_visited:

    for neighbor_node in graph[last_node]:
        all_neighbors_visited = True
        if not visited[neighbor_node]:
            stack.append(neighbor_node)
            visited[neighbor_node]=True
            print(neighbor_node, ' -> ', end='')
            last_node = neighbor_node
            all_neighbors_visited = False
            break

    if all_neighbors_visited :
        stack.pop()
        last_node = stack[len(stack)-1]

    ### check all_visited
    all_visited = True
    for v in visited:
        if not v:
            all_visited = False
