"""
시작시간 - 07:33
종료시간 - 07:59
"""


n, m, sx, sy = map(int, input().split())
sx -= 1
sy -= 1

graph = [
    [0 for _ in range(n)]
    for _ in range(n)
]

tmp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

dxy = [[1,0],[-1,0],[0,1],[0,-1]]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def plus(x,y,t):
    for k in range(4):
        nx, ny = x + 2**(t-1)*dxy[k][0], y + 2**(t-1)*dxy[k][1]
        if not in_range(nx, ny) or visited[nx][ny]:
            continue
    
        tmp[nx][ny] += 1
        visited[nx][ny] = True

cnt = 1
def simulate(t):
    global cnt
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                plus(i,j,t)
    
    for i in range(n):
        for j in range(n):
            if tmp[i][j] == 1:
                graph[i][j] += 1
                cnt += 1
                
    
    for i in range(n):
        for j in range(n):
            tmp[i][j] = 0

visited[sx][sy] = True
graph[sx][sy] += 1
for t in range(1,m+1):
    simulate(t)

print(cnt)