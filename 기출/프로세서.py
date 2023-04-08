"""
시작시간 - 03:11
멕시노스 가로 세로 n*n개의 cell
1개의 cell에슷 1개의 (core) 혹은 1개의 (전선)이 올 수 있다.
맥시노스의 가장 자리에는 전원이 흐르고 있다.

core과 전원을 연결하는 전선은 직선으로만 설치 가능
교차 엑스

가장자리에 위치한 core는 전원이 들어와있다.
최대한 많은 core에 전원을 연결하였을 경우, 전선 길이의 합
여러 방법이 있는 경우는 전선 길이의 합이 최소가 되는 값

한칸
"""


T = int(input())
graph = []
dxy = [[1,0],[-1,0],[0,1],[0,-1]]
visited = []
min_line_cnt = float("INF")
max_light_cnt = 0
def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

flag = False
def dfs(core_num, cnt,light_cnt):
    ## core의 연결 방향을 정한다.
    global min_line_cnt
    global max_light_cnt
    global flag


    if core_num == len(core_lists):
        if light_cnt == len(core_lists):
            flag = True
        if max_light_cnt < light_cnt:
            max_light_cnt = light_cnt
            min_line_cnt = cnt
        elif max_light_cnt == light_cnt:
            min_line_cnt = min(min_line_cnt , cnt)
    
        return

    sx,sy = core_lists[core_num]

    
    for k in range(4):
        x, y = sx, sy
        ncnt = 0
        visited_list = []
        while True:
            x, y = x + dxy[k][0], y + dxy[k][1]
            if not in_range(x,y):
                dfs(core_num+1, cnt + ncnt, light_cnt + 1) 
                break
            
            if visited[x][y] or graph[x][y] == 1:
                break
            
            visited[x][y] = True
            ncnt += 1
            visited_list.append([x,y])
        
        for vx, vy in visited_list:
            visited[vx][vy] = False
    
    if not flag:
        dfs(core_num+1, cnt, light_cnt)

    
    ## 다음 core를 정한다.
    return


for round in range(T):
    n = int(input())

    graph = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    core_lists = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                core_lists.append([i,j])

    visited = [
        [False for _ in range(n)]
        for _ in range(n)
    ]
    min_line_cnt = float("INF")
    max_light_cnt = 0
    flag= False
    dfs(0,0,0)

    # print(min_line_cnt)

    print("#%d %d" %(round, min_line_cnt))