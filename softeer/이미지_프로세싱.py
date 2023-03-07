import sys
# print(128*128*500)
# 완탐으로 같은위치 찾아서 바꾸기

dxy = [[1,0],[-1,0],[0,1],[0,-1]]
H,W = map(int, input().split())
graph = []


visited =[[False]*W for _ in range(H)]

for _ in range(H):
    line_graph = list(map(int, input().split()))
    graph.append(line_graph)

def in_range(a,b):
    if 0 <= a and a < H and 0 <= b and b < W:
        return True
    return False


def dfs(x,y,change, origin):
    graph[x][y] = change
    for k in range(4):
        nx,ny = x+dxy[k][0], y+dxy[k][1]
        if in_range(nx,ny) :
            if graph[nx][ny] == origin:
                # visited[nx][ny] = True
                # graph[nx][ny] = change
                dfs(nx, ny, change, origin)



command = []
Q = int(input())
for _ in range(Q):
    cx,cy,c = map(int, input().split())
    # visited =[[False]*W for _ in range(H)]
    # visited[cx-1][cy-1] = True
    # graph[x][y] = change -> 전에 change를 해주면 안된다. 왜냐면 origin이 바뀐다.
    if c != graph[cx-1][cy-1]:
        dfs(cx-1,cy-1,c, graph[cx-1][cy-1])

for g in graph:
    print(*g) 


