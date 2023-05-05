## 도현이는 집 n개가 수직선 위에 있다.
# 최대한 많은 곳에서 와이파이를 사용에 

# 한집에는 공유기 하나만 설치,
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 설치

# 첫째 줄에 집의 개수와 공유기 개수
# 하나 이상의 빈 칸을 사이에 두고 주어진다.

n, c = map(int, input().split())

street = []

for _ in range(n):
    street.append(int(input()))

street.sort()

left = 1
right = street[-1] - street[0]

def check_dis(mid):
    put = 1
    last_check = 0
    
    for now_idx in range(1,len(street)):
        if street[now_idx] - street[last_check] >= mid:
            put += 1
            last_check = now_idx
    
    return put
        
        

    
answer = 0

while left <= right:

    # mid의 값은 인접한 두 공유기 사이의 거리를 최대로 하는 거리이다.
    mid = (left + right) // 2
    
    print(left, mid, right)
    put = check_dis(mid)
    # 놓을 수 있는 공유기가 크거나 같으면
    print("put", put)
    if put == c:
        answer = max(answer, mid)
        left = mid + 1

    # mid 값을 늘려야 한다면
    ## 공유기가 적게 설치됨, mid 값을 줄여야함
    elif put < c :
        right = mid - 1
    
        
    
    # 공유기를 너무 많이 설치했으면, 간격을 넓혀야해
    else:
        left = mid + 1
    

print(answer)
        
        


    
