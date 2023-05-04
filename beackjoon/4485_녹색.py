## 녹색 옷 입은 애가 젤다지?

import heapq

dxy = [[1,0],[0,1],[-1,0],[0,-1]]
dp = []
graph = []
n = -1

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def find_min():
    heap = []
    ## 힙은 항상 최소값만 도출한다.
    heapq.heappush(heap, [graph[0][0],0,0])

    # 최초값이 매우 크기 때문에 처음에 heap에 넣지 않고, 방문할 때 넣어도 된다..
    # 그리고 이미 방문한 노드를 다시 방문해도 괜찮기 때문에 왜..?
    

    while heap:
        num, x, y = heapq.heappop(heap)


        # 힙의 연결 노드를 갱신해준다.
        for k in range(4):
            nx, ny = x + dxy[k][0], y + dxy[k][1]
            if not in_range(nx, ny):
                continue
            
            # 연결 노드 중 갱신 시킬 노드가 있다면, 갱신해준다.
            # 원래 dp 값과 dp 값에 graph 값을 더해준 것을 비교해준다.
            if dp[nx][ny] > num  + graph[nx][ny]:
                dp[nx][ny] = num + graph[nx][ny]
            
                # 힙에 넣어 줄 것인가? -> 방문 노드는 모두 넣어줘야 한다.
                # 방문한 노드는 다시 방문하면 안된다.
                # 방문노드와 방문하지 않는 노드를 어떻게 구분하느가?
                heapq.heappush(heap, [dp[nx][ny], nx, ny])
# 
    return

repeat = 0

while True:
    n = int(input())
    repeat += 1
    if n == 0:
        break
    
    graph = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    dp = [
        [float("INF")]*n
        for _ in range(n)
    ]

    find_min()
    print("Problem %d: %d" %(repeat, dp[n-1][n-1]))

