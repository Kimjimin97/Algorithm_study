import sys
from collections import deque

n = int(input())
graph = []
blocks = []


for _ in range(n):
    graph.append(list(map(int, input())))

visited = [[False]*n for _ in range(n)]
dxy = [[1,0],[0,1],[-1,0],[0,-1]]

def in_graph(a1,b1):
    if 0<= a1 and a1 < n and 0 <= b1 and b1 < n:
        return True
    return False

def bfs(a,b):
    queue = deque()
    visited[a][b] = True
    queue.append([a,b])
    block = 1

    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx, ny = x+dxy[k][0], y+dxy[k][1]
            if in_graph(nx, ny) and not visited[nx][ny] and graph[nx][ny] != 0 :
                visited[nx][ny] = True
                queue.append([nx,ny])
                block += 1
    
    blocks.append(block)

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            bfs(i,j)


print(len(blocks))
blocks.sort()
for bl in blocks:
    print(bl)