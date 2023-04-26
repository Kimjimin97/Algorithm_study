## 배낭 채우기
## n개의 보석의 정보가 주어졌을 때, 
## 보석을 적절하게 골라 무게의 함이 m을 넘지 않도록 하면서 가치의 합이 최대가 되도록 하는 프로그램

n,m = map(int, input().split())

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [-1]*(m+1)

dp[0] = 0

for w, v in graph:
    for num in range(m, -1, -1):
        
        if num >= w:
            if dp[num-w] == -1:
                continue
            
            dp[num] = max(dp[num], dp[num-w]+v)


print(max(dp))
        
        
