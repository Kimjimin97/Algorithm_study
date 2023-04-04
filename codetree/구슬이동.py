"""
시작시간 - 08:10
종료시간 - 9:00
"""
## m개의 구슬이 n*n 격자 안에 놓여져 있고, 
## 격자는 벽에 둘러싸여 있다
## 각 구슬은 일정 속도를 갖고 정해진 방향으로 움직인다.
## 속도와 방향
## 부딪히면 움직이는 방향이 반대로 뒤집혀 동일한 속도로 움직이는 것을 반복

## 매 초마다 구슬들을 움직이게 되고, 움직이고 난 후에 같은 위치에 여러개 가능

## 만약 동일한 위치에 구슬이 k개 이하라면 문제 없이 그 다음 과정을 진행
## 동일한 위치에 k개가 넘는 구슬이 같은 칸에 위치하게 된다면, 우선순쉬가 높은 k개만 살아남고 나머지 구슬들은 사라진다.



## 우선순위 (구슬의 속도, 구슬의 번호)

## 소멸은 충돌 즉시 일어난다.

"""
1, 구슬을 움직인다. -> tmp
2. tmp -> graph로 옮기고 k 개가 넘어가면 제거해준다.
"""

n,m,t,k = map(int, input().split())

dxy = [[0,1],[1,0],[-1,0],[0,-1]]

dir_map = {
    "R":0,
    "D":1,
    "U":2,
    "L":3
}

graph = [
    [[] for _ in range(n)]
    for _ in range(n)
]

tmp = [
    [[] for _ in range(n)]
    for _ in range(n)
]

for num in range(m):
    x,y,d,v = map(str, input().split())
    x,y,d,v = int(x)-1, int(y)-1, dir_map[d],int(v)
    graph[x][y].append([v,num,d])

def in_range(x,y):
    return 0<= x and x < n and 0<= y and y < n

def move(x,y,g):
    vv, num,d = g

    go = 0

    while go < vv:
        nx, ny = x + dxy[d][0], y + dxy[d][1]
        if not in_range(nx, ny):
            d = (3-d)
            nx, ny = x + dxy[d][0], y + dxy[d][1]

        x,y = nx, ny    
        go += 1
    
    tmp[x][y].append([vv,num,d])
    return 
        
        
def remove(x,y):
    global tmp
    live = []
    balls = tmp[x][y]
    balls = sorted(balls, key = lambda x : (-x[0],-x[1]))

    tmp[x][y] = balls[:k]
    
    return


def simulate():
    global graph
    ## tmp에 모든 구슬 옮기기
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                for g in graph[i][j]:
                    move(i,j,g)
    
    ## 제거해주기
    for i in range(n):
        for j in range(n):
            if len(tmp[i][j]) > k:
                remove(i,j)
            graph[i][j] = tmp[i][j]
            tmp[i][j] = []
    
    # for g in graph:
    #     print(g)
    # print()
    
    
# for g in graph:
#     print(g)
# print()

for _ in range(t):
    simulate()

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(graph[i][j])

print(answer)
        