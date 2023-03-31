"""
오답노트
set recurion
방문처리 초기화
"""

import sys

sys.setrecursionlimit(10**5)
n,m = map(int, input().split())

max_water = 0
graph = []

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

dxy = [[1,0],[0,1],[-1,0],[0,-1]]


for _ in range(n):
    lists = list(map(int, input().split()))
    max_water = max(max_water, max(lists))
    graph.append(lists)



def inital_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

def in_range(x,y):
    return 0<=x and x < n and 0<= y and y< m


def can_go(x,y,safe_water):
    if not in_range(x,y):
        return False
    
    if visited[x][y]:
        return False
    
    if graph[x][y] <= safe_water:
        return False
    
    return True
    

def dfs(x,y,safe_water):

    for k in range(4):
        nx, ny = x +dxy[k][0], y + dxy[k][1]

        if not can_go(nx, ny, safe_water):
            continue

        visited[nx][ny] = True
        dfs(nx, ny, safe_water)
    



max_safe_water = 1
max_safe_area_count = 0


def find_safe_area(safe_water):
    global max_safe_area_count
    global max_safe_water
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] > safe_water:

                dfs(i,j,safe_water)
                cnt += 1

                if cnt > max_safe_area_count:
                    max_safe_area_count = cnt
                    max_safe_water = safe_water
        

for safe_water in range(1,max_water):
    inital_visited()
    find_safe_area(safe_water)
    
print(max_safe_water, max_safe_area_count)