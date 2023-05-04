# 세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다.
# 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단칸에 말이 놓여있다.

# 알파벳은 지금까지 지나온 모든 칸에 적여 있는 알파벳과는 달라야 한다. 
# 같은 알파벳이 적힌 칸을 두번 지날 수 없다.


## 최대 26개의 길 밖에 갈 수 없고, 

n, m = map(int, input().split())

graph = [
    list(map(str, input()))
    for _ in range(n)
]

dxy =[[1,0],[0,1],[-1,0],[0,-1]]

alpha_visited = [False]*91



visited = [[False]*m
           for _ in range(n)]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

path = set()

max_answer = 0

def dfs(n,x,y):
    global max_answer
    max_answer = max(max_answer, n)

    for k in range(4):
        nx, ny = x + dxy[k][0], y + dxy[k][1]
        if not in_range(nx, ny):
            continue
        if visited[nx][ny]:
            continue
        if alpha_visited[ord(graph[nx][ny])]:
            continue

        visited[nx][ny] = True
        alpha_visited[ord(graph[nx][ny])] = True
        dfs(n+1, nx, ny)
        visited[nx][ny] = False
        alpha_visited[ord(graph[nx][ny])] = False


    return

visited[0][0] = True

alpha_visited[ord(graph[0][0])] = True
dfs(1,0,0)

print(max_answer)

# print(ord("A"),ord("Z"))