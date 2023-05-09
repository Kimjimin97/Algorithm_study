"""
문제의 포인트!!
격자 탐색에서 최소비용을 구하는 문제
다익스트라를 활용해서 최소비용을 효율적으로 구할 수 있다.
"""

"""
오른쪽 아래 칸까지 이동해야 한다.
동굴의 각 칸마다 도둑루피가 있는데, 이칸을 지나면 해당 도둑 루피의 크기만큼
소지금을 잃게 된다.

링크는 잃는 금액을 최소화 하여 동굴 건너편까지 이동해야 하며, 한번에 상하좌우 1칸씩 이동할 수 잇다.

1) 완탐 -> O(4^n*n) -> 4가지 방향의 백트레킹은  4가지 방향에 대한 모든 경우를 고려해야 하기 때문에 다음과 같은 시간복잡도를 가지낟.
-> 시간이 오래 걸린다.

2) dp -> O(N*N) -> dp로 풀려면 왼쪽 혹은 밑으로 이동 조건이 필요하다. 
-> 문제에 적합하지 않다.

3) 그래프 탐색 -> O(N*N log(N*N)) -> 다익스트라(비용) 
"""

"""
다익스트라 힙을 이용한다.

1) dp 격자를 만든다.
2) 한 장소를 방문하면, 이동가능한 노드를 추가한다.
3) 더 효율적인 거리가 나왔을 때, 갱신해 주고, 힙에 추가한다.
4) 모든 노드를 방문할 때까지 반복한다.
"""
import heapq

n = -1
graph = []
dp = []

dxy = [[1,0],[-1,0],[0,1],[0,-1]]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(num, x,y):
    if dp[x][y] <= num:
        return False
    return True

def find_min_cost():
    heap = []
    heapq.heappush(heap,[graph[0][0],0,0])

    while heap:
        num, x, y = heapq.heappop(heap)

        for k in range(4):
            nx, ny = x + dxy[k][0], y + dxy[k][1]
            if not in_range(nx, ny):
                continue

            if not can_go(num + graph[nx][ny], nx, ny):
                continue

            dp[nx][ny] = num + graph[nx][ny]
            heapq.heappush(heap, [dp[nx][ny],nx,ny])
        
    return

count = 0
while True:
    n = int(input())
    count += 1
    
    if n == 0:
        break

    graph = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    dp = [[float("INF")]*n for _ in range(n)]
    find_min_cost()
    print("Problem %d: %d" %(count,dp[n-1][n-1]))



