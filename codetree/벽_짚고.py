import sys
n = int(input())
start_x, start_y = map(int, input().split())

graph = [
    list(map(str, input()))
    for _ in range(n)
]


visited = [
    [
    [False for _ in range(4)]
    for _ in range(n)
    ]
    for _ in range(n)
]

curr_x, curr_y, direction = start_x - 1, start_y -1,0

dxy = [[0,1],[1,0],[0,-1],[-1,0]]

t = 1
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def simulate():
    global curr_x, curr_y, direction, t

    if visited[curr_x][curr_y][direction]:
        print(-1)
        sys.exit(0)

    visited[curr_x][curr_y][direction] = True
    ## 현재 방향으로 이동시킨다. 
    ## 무조건 이동하는 것이 아니라 임시로 nx, ny 에 이동시키다.
    nx, ny = curr_x + dxy[direction][0], curr_y + dxy[direction][1]


    ## 이동 방향이 범위 밖이라면 탈출
    ## 이때 단일 객체를 이동시켜야 while문에서 걸릴 수 있다.
    if not in_range(nx, ny):
        curr_x, curr_y = nx, ny
        return
    
    ## 임시좌표가 벽이라면?
    ## 방향을 바꿔준다.
    ## 벽을 마주친 이후에는 두 가지 경우만 발생한다.
    ## 벽인 경우, 벽이 아닌 경우
    ## 벽인 경우는 다시 좌표를 움지기이고, 벽이 아닌 경우는 오른쪽 벽을 확인해줘야 한다.
    ## 이동은 항상 벽이 아닌 경우에만 이동해준다.
    if graph[nx][ny] == "#":
        direction = (direction-1+4)%4

    ## 벽이 아닌 경우는 항상 이동시켜주어야 한다.
    ## 벽이 아닌 경우는 항상 두가지 경우에 봉착한다.
    ## 벽 오른쪽에 벽이 있는 경우, 오른쪽에 벽이 없는 경우
    ## 오른쪽에 벽이 있는 경우는 한칸이동
    ## 오른쪽에 벽이 없는 경우는 벽이 없는 쪽으로 이동한다.
    else:
        rk = (direction+ 1+4) %4

        rx, ry = nx + dxy[rk][0], ny + dxy[rk][1]

        if graph[rx][ry] == "#":
            
            curr_x, curr_y = nx, ny
            t += 1
        
        else:
            
            curr_x, curr_y = rx, ry
            t += 2
            direction = rk
               


while in_range(curr_x, curr_y):
    simulate()

print(t)


