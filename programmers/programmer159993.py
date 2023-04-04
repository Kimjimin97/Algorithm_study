"""
시작시간 - 03:35
종료시간 - 03:53

레버를 당긴 후 미로를 빠져나가는 문이 있는 칸으로 이동
## 레버로 이동
## 이후 exit으로 이동

## 레버 최단 거리 + exit의 최단 거리 ?
"""
from collections import deque
def solution(maps):
    answer = 0
    
    
    
    ## 그래프
    graph = [
        list(map(str, m))
        for m in maps
    ]
    
    n = len(graph)
    m = len(graph[0])
    
    sx, sy, ex, ey, lx, ly = -1, -1, -1, -1, -1, -1
    
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "S":
                sx, sy = i,j
            elif graph[i][j] == "E":
                ex, ey = i,j
            elif graph[i][j] == "L":
                lx, ly = i,j
                

    
    ## 방문 여부
    visited = [
        [False for _ in range(m)]
        for _ in range(n)
    ]
    
    dxy = [[1,0],[-1,0],[0,1],[0,-1]]
    
    def in_range(x,y):
        return 0 <= x and x < n and 0 <= y and y < m
    
    def can_go(x,y):
        if not in_range(x,y):
            return False
        if visited[x][y] or graph[x][y] == "X":
            return False
        return True
        
    
    def go_lever(x,y):
        queue = deque()
        queue.append([x,y,0])
        visited[x][y] = True
        
        while queue:
            x,y,cnt = queue.popleft()
            if x == lx and y == ly:
                return [x,y,cnt]
            
            for k in range(4):
                nx, ny = x + dxy[k][0], y + dxy[k][1]
                if can_go(nx, ny):
                    visited[nx][ny] = True
                    queue.append([nx, ny, cnt + 1])
            
        return [-1,-1,-1]
    
    def go_end(x,y):
        queue = deque()
        queue.append([x,y,0])
        visited[x][y] = True
        
        while queue:
            x,y,cnt = queue.popleft()
            if x == ex and y == ey:
                return cnt
            
            for k in range(4):
                nx, ny = x + dxy[k][0], y + dxy[k][1]
                if can_go(nx, ny):
                    visited[nx][ny] = True
                    queue.append([nx, ny, cnt + 1])
            
        return -1
    
    mx, my, mcnt = go_lever(sx, sy)
    
    if mx == -1:
        return -1 
    
    for i in range(n):
        for j in range(m):
            visited[i][j] = False
            
    ecnt = go_end(mx, my)
    if ecnt == -1:
        return -1
    
    answer = mcnt + ecnt
    
    return answer