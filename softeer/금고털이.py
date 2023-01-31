import sys

W,N = map(int, input().split())


candidate = [0]*(10**4+1)

for _ in range(N):
    a,b = map(int, input().split())
    candidate[b] += a

## 가격 높은 순부터 탐색
candidate.reverse()

w= 0
money = 0
for i in range(len(candidate)):
    if candidate[i] == 0:
        continue
    
    if w+ candidate[i] <= W:

        w += candidate[i]
        money += candidate[i]*(10000-i)
    
    else:
        money += (W-w)*(10000-i)
        break


print(money)