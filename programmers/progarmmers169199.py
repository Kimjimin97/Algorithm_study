"""
시작시간 - 10:18
종료시간 - 10:54 
in_range 항상 먼저 해주기
"""
## 시작 위치에서 목표 위치까지 최소 몇번만에 도달할 수 있는지
## 게임판 위의 장애물이나 맨 끝에 부딪힐 때까지 미끄러져 이동하는 것을 한번의 이동
## "R" - 로봇의  위치
## "D" - 장애물의 위치
from collections import deque

def solution(board):
    
    graph = [
        list(map(str, b))
        for b in board
    ]
    
    n,m = len(graph), len(graph[0])
    visited = [
        [False for _ in range(m)]
        for _ in range(n)
    ]
    
    dxy = [[1,0],[0,1],[0,-1],[-1,0]]
    answer = -1
    
    
    def in_range(x,y):
        return 0<= x and x<n and 0 <= y and y < m
    
    ## 마지막까지 이동할 수 있는 좌표를 반환한다.
    def move(x,y,k):
        while True:
            nx, ny = x + dxy[k][0], y + dxy[k][1]
            if not in_range(nx,ny) or graph[nx][ny] == "D":
                return [x,y]
            x,y = nx, ny
            
            
    
    def bfs(x,y):
        nonlocal answer
        queue = deque()
        visited[x][y] = True
        queue.append([x,y,0])

        while queue:
            x,y,cnt = queue.popleft()
            
            if graph[x][y] == "G":
    
                answer = cnt
                break
                
            for k in range(4):
                nx, ny = move(x,y,k)
                
                if visited[nx][ny]:
                    continue
                    
                visited[nx][ny] = True
                queue.append([nx,ny,cnt+1])
        
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "R":
                bfs(i,j)
                break
    
    
  
    
    return answer