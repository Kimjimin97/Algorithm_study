"""
시작시간 - 02:41
"""
from collections import deque
score = 0
# 나무는 h, 턴은 k

n,m, h, k = map(int, input().split())

## m개의 도망자의 위치, 이동 방법 d가 공백을 두고 차례로
## d가 1인 경우 좌우로 움직임, 2인 경우 상하로 움직임
## 좌우로 움직이는 사람은 항상 오른쪽을 보고, 상하로 움직이는 사람은 항상 아래를 보고 시작

graph = [
    [[] for _ in range(n)]
    for _ in range(n)
]

NONE=[-1,-1,-1]
tree = [
    [False for _ in range(n)]
    for _ in range(n)
]

dxy = [[1,0],[0,1],[0,-1],[-1,0]]


snail_graph = [
    [-1 for _ in range(n)]
    for _ in range(n)
]

rev_snail_graph = [
    [-1 for _ in range(n)]
    for _ in range(n)
]

rev_dir = [0,2,3,1]
right_dir = [3,1,0,2]




def make_snail():

    x, y = n//2, n//2
    move_num = 1
    d = 0

    while True:
        for _ in range(move_num):
            snail_graph[x][y] = right_dir[d]

            x,y = x + dxy[right_dir[d]][0], y + dxy[right_dir[d]][1]
            rev_snail_graph[x][y] = rev_dir[d]

            if x== 0 and y == 0:
                snail_graph[0][0] = 0
                rev_snail_graph[n//2][n//2] = 3
                return

        d = (d+1)%4
        if d == 2 or d == 0 :
            move_num += 1


    
    
make_snail()


catcher_x, catcher_y = n//2, n//2
runner_list = []




for mm in range(m):
    x,y,d = map(int, input().split())
    if d == 2:
        d = 0
    x -= 1
    y -= 1
    graph[x][y].append(mm)
    runner_list.append([x,y,d])

for _ in range(h):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    tree[x][y] = True




tmp_graph = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]


def in_range(x,y):
    return 0<=x and x < n and 0<= y and y <n




def initial_tmp_graph():
    global tmp_graph
    for i in range(n):
        for j in range(n):
            tmp_graph[i][j] = []

def move_runner():
    global runner_list
    global graph
    # tmp_runner_list = []
    
    initial_tmp_graph()

    for  idx, lists in enumerate(runner_list):
        x, y, d = lists

        if lists == NONE:
            continue
        
        if abs(catcher_x - x ) + abs(catcher_y - y ) > 3:
            tmp_graph[x][y].append(idx)
            runner_list[idx] = [x,y,d]
            continue

        ## 3 이하인 도망자만 움직인다.
        # d = graph[x][y]
        
        nx, ny = x +dxy[d][0], y + dxy[d][1]
        print("1번이 왜 안움직이나?", idx, nx, ny,"원래좌효",x,y)
        if not in_range(nx, ny):
            d = 3-d
           
            nx, ny = x +dxy[d][0], y + dxy[d][1]
        
        ## 움직인 좌표에 술래가 있는 경우
        if nx == catcher_x and ny == catcher_y:
            runner_list[idx] = [x,y,d]
            tmp_graph[x][y].append(idx)
        else:
            runner_list[idx] = [nx,ny,d]
            tmp_graph[nx][ny].append(idx)
    

    for i in range(n):
        for j in range(n):
            graph[i][j] = tmp_graph[i][j]
    
    
    # runner_list[:] = tmp_runner_list[:]
   

    pass

catcher_reverse = False

def move_catcher():
    global catcher_x
    global catcher_y
    global catcher_reverse

    if not catcher_reverse:
        d = snail_graph[catcher_x][catcher_y]
    else:
        d = rev_snail_graph[catcher_x][catcher_y]

    nx, ny = catcher_x + dxy[d][0], catcher_y + dxy[d][1]
    
    if nx == 0 and ny == 0:
        catcher_reverse = True

    if nx == n//2 and ny == n//2:
        catcher_reverse = False

    catcher_x, catcher_y = nx, ny

def catch(turn):
    global score
    global graph

    if not catcher_reverse:
        d = snail_graph[catcher_x][catcher_y]
    else:
        d = rev_snail_graph[catcher_x][catcher_y]
    cnt = 0

    for i in range(3):
        nx, ny = catcher_x + dxy[d][0]*i, catcher_y + dxy[d][1]*i
        if in_range(nx, ny) and not tree[nx][ny] and graph[nx][ny]:

            for num in graph[nx][ny]:
                print("tunrn",turn)
                print("잡은 사람은 누군가?", nx, ny,num)

                cnt += 1
                print(num, runner_list)
                runner_list[num] = NONE
            
            graph[nx][ny] = []
            
            
    
    score += cnt * turn
        



for turn in range(k):
    print(runner_list)
    for g in graph:
        print(g)
    print()
    move_runner()
    
    

    move_catcher()
    
    
    print(runner_list)
    for g in graph:
        print(g)
    print()
    catch(turn+1)
   

print(score)

