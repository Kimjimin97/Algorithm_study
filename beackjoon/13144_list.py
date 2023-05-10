n = int(input())

nums = list(map(int, input().split()))

j = 0

dp = [0]*n

path = [False]*(1000001)
count = 1
ㅂ

for i in range(n):
    # path[nums[i]] = True
    while j + 1 < n :
        if path[nums[j+1]]:
            break
        
        else:
            path[nums[j+1]] = True
            count += 1
            j += 1
    
    if count <= 0:
        count = 1
        dp[i] = count
        path[nums[i]] = False
        continue

    dp[i] = count
    count -= 1
    path[nums[i]] = False
        
print(sum(dp))
