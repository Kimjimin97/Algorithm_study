import sys
N, M = map(int, input().split())

limit_info = []
for _ in range(N):
    limit_info.append(list(map(int, input().split())))

real_info = []
for _ in range(M):
    real_info.append(list(map(int, input().split())))


a = 0
b = 0
a_dis = limit_info[0][0]
b_dis = real_info[0][0]
over = 0



while True:
    
    if a_dis == 100 and b_dis == 100:
        break
    
    ## 속도 비교
    if real_info[b][1] - limit_info[a][1] > 0:
        over= max(over,real_info[b][1] - limit_info[a][1] )
        

    ## 거리 이동
    if a_dis < b_dis:
        a += 1
        a_dis += limit_info[a][0]
    
    elif a_dis > b_dis:
        b += 1
        b_dis += real_info[b][0]
    
    elif a_dis == b_dis:
        a += 1
        b += 1
        a_dis += limit_info[a][0]
        b_dis += real_info[b][0]

print(over)