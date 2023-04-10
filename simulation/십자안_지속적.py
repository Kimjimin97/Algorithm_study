"""
시작시간 - 01:32
종료시간 - 02:06
"""

## 십자 모양의 지속적 폭말
## 1이상 100 이사로 구성된 격자판
"""
1) 특정 열을 선택
2) 특정 열을 선택하면 가장 위에 있는 칸을 중심으로 십자 모양 터지게 된다.
3) 터진 이후에 중력에 의해 숫자들이 아래로 떨어진다.

1) 1인 경우에는 자기 자신만 터지게 된다.
2) 2인 경우느느 4개
3) 3인 경우에는 상하좌우로 2개씩 터진다
"""


n,m = map(int, input().split())

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

command = [
    int(input()) - 1
    for _ in range(m)
]
tmp_graph = [
    [0 for _ in range(n)]
    for _ in range(n)
]

dxy = [[1,0],[-1,0],[0,1],[0,-1]]

def find_point(col):
    for row in range(n):
        if graph[row][col] != 0:
            return [row,col]
    
    return [-1,-1]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def remove(x,y):
    cnt = graph[x][y]

    for c in range(cnt):
        for k in range(4):
            nx, ny = x + dxy[k][0]*c , y + dxy[k][1]*c
            if in_range(nx, ny):
                graph[nx][ny] = 0

def drop(col):
    tmp_row = n-1
    for row in range(n-1,-1,-1):
        if graph[row][col]:
            tmp_graph[tmp_row][col] = graph[row][col]
            tmp_row -= 1

def drop_all():
    for col in range(n):
        drop(col)
    
    for i in range(n):
        for j in range(n):
            graph[i][j] = tmp_graph[i][j]
            tmp_graph[i][j] = 0
    
    
    

def simulate(c):
    x,y = find_point(c)
    if x == -1 and y == -1:
        return
    remove(x,y)
    drop_all()

for c in command:
    simulate(c)

for g in graph:
    print(*g)
