"""
정수 사각형 최소 합
N*N 행렬이 주어졌을 때, (1,N)에서 시작하여 왼쪽 혹은 밑으로만 이동하여
"""

n = int(input())

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

dp[0][n-1] = graph[0][n-1]

for i in range(n-2, -1, -1):
    dp[0][i] = dp[0][i+1] + graph[0][i]
    

for i in range(1,n):
    dp[i][n-1] = dp[i-1][n-1] + graph[i][n-1]

for i in range(n):
    for j in range(n-1, -1,-1):
        if not dp[i][j]:
            dp[i][j] = min(dp[i-1][j],dp[i][j+1]) + graph[i][j]
    


print(dp[n-1][0])