"""
도현이는 언제 어디서나 와이파를 즐기기 위해서 집에 공유기 c개를 설치

최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에

한 집에는 공유기를 하나만 설치할 수 있고

가장 인접한 두 공유기 사이의 거리를 가능한 크게 설치

"""
n, c = map(int, input().split())

dis = []

for _ in range(n):
    dis.append(int(input()))

left = 0
right = 1000000000

dis.sort()
def check_count(mid):
    count = 1
    last_pick = 0

    for i in range(1, len(dis)):
        diff = dis[i] - dis[last_pick]
        
        ## 만약에 설정해둔 mid 값보다 두 집 사이의 거리가 크다면,
        if diff >= mid:
            count += 1
            last_pick = i

    return count

answer = 0
while left <= right:
    
    mid = (left + right)//2

    count = check_count(mid)
    
    if count >= c:
        left = mid + 1
        answer = max(answer, mid)
    
    elif count < c:
        right = mid - 1


print(answer)