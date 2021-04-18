print(' ㅡㅡㅡ 책: 이것이 코딩 테스트다 ㅡㅡㅡ')

### iceframe: count ices
### DFS search - recursive

def dfs(i):
    h = len(iceframe[0])
    v = len(iceframe)

    x = i[0]
    y = i[1]

    # exit code: check neighbors
    if not (-1 < x < h and -1 < y < v):  # out of scope: return
        return False
    if visited[y][x]:  # visited: return
        return False

    # process : if neighbor is ice
    if iceframe[y][x] == 0:
        visited[y][x] = True

        # check neighbors
        dfs([x + 1, y])
        dfs([x - 1, y])
        dfs([x, y + 1])
        dfs([x, y - 1])
    return True

# set variables
# 0,0 ~ n-1, n-1
iceframe = [
    [0, 0, 1, 0, 1],
    [1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 1, 1],
]
h = len(iceframe[0])
v = len(iceframe)
visited = [[False] * 5 for i in range(5)]
cnt = 0

# logic : check all icespots. if it is an ice and not visited, do DFS.
for i in range(v):
    for j in range(h):
        if iceframe[i][j] == 0 and not visited[i][j]:
            if dfs([j, i]):
                cnt += 1

# output
print('cnt=', cnt)
print(visited)
