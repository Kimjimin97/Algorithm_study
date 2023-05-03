# 링크가 잃을 수 밖에 없는 최소 금액은? 


import heapq

graph =[]
visited =[]

dxy =[[1,0],[0,1],[-1,0],[0,-1]]
N = -1

def in_range(x,y):
    return 0<= x and x < N and 0 <= y and y < N

def can_go(x,y):
    if not in_range(x,y):
        return False
    
    if visited[x][y]:
        return False
    
    return True

answer = float("INF")

def dais(x,y,num):
    heap = []
    heapq.heappush(heap, [num,x,y])
    
    while heap:
        num, x, y = heapq.heappop(heap)

        if visited[x][y]:
            continue

        visited[x][y] = True

        for k in range(4):
            nx, ny = x + dxy[k][0], y + dxy[k][1]
            if can_go(nx, ny):
                if dp[nx][ny] > graph[nx][ny] + num:
                    dp[nx][ny] = graph[nx][ny] + num
                    heapq.heappush(heap,[graph[nx][ny] + num, nx, ny])

    return



pro_num = 0
while True:
    pro_num += 1
    N = int(input())
    answer = float("INF")
    if N == 0:
        break

    graph = [
        list(map(int, input().split()))
        for _ in range(N)
    ]
    visited = [
        [False]*N
        for _ in range(N)
    ]

    dp = [
        [float("INF")]*N
        for _ in range(N)
    ]

    dais(0,0,graph[0][0])
    # for d in dp:
    #     print(d)
    # print()
    print('Problem %d: %d' %(pro_num, dp[N-1][N-1]))
    


