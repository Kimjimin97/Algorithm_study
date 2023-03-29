## 우선순위 :가장큰수, 상하자우
## 종료조건 : 움직이 없을 때 까지

n,r,c = map(int, input().split())

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxy = [[-1, 0],[1,0],[0,-1],[0,1]]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

max_x, max_y = (r-1, c-1)
now_x, now_y = (r-1, c-1)

while True:
    ## 상하좌우 탐색, 큰 수 이동
    # if not can_continue():
    #     break
   
    x,y = now_x, now_y
    max_num = graph[x][y]
    print(max_num, end = " ")

    for k in range(4):
        nx, ny = x +dxy[k][0], y +dxy[k][1]
        if in_range(nx, ny) and graph[nx][ny]  > max_num:
            max_x, max_y = nx, ny
            break
    
    if max_x == x and max_y == y:
        break
    
    else:
        now_x, now_y  = max_x, max_y
    