"""
시작시간 - 08:48
"""
## n*n 격자 꼬리잡기 놀이 진행

## 3명 이상이 한팀이 됩니다. 
## 모든 사람들은 자산의 앞 사람의 허리를 잡고 움직이여한다.
## 맨 앞에 있는 사람을 머리 사람
## 맨 뒤에 있는 사람을 꼬리 사람

## 주어진 이동 선을 따라서만 이동

"""
1. 먼저 각 팀은 머리 사람을 따라서 한칸 이동
2. 공이 던지기, 4n 라운드
3. 공이 던져지는 경우 해당 선에 사람이 있으면 최초에 만나게 되는 사람만이 점수 획득 (머리 사람 시작 k번째 사람 k^2)
4. 공을 획득한 사람은 머리사람과 꼬리 사람이 바뀐다. 즉 방향이 바뀐자.
 
4-1. 1라운드가 끝난 후
4-2. 모든 팀 1칸 이동
머리사람 찾기,상하좌우 4번 이동선 찾기


4-3. 공 발사 2라운드


"""
from collections import deque
n,m,k = map(int,input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
## right, up, left, down
dxy =[[0,1],[-1,0],[0,-1],[1,0]]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

start_people = []
road = [[] for _ in range(m)]
tmp_end = []
score = 0
match_start_end = dict()



def in_range(x,y):
    return 0<= x and x < n and 0 <= y and y < n


## 꼬리사람 찾기
def find_people(team,sx,sy,hx, hy):
    x, y = sx, sy
    road[team].append([x,y])
    cnt = 0
    while True:
        for k in range(4):
            ## 4 방향 중 길이 있는지 체크 
            nx, ny = x + dxy[k][0], y + dxy[k][1]
            if in_range(nx, ny) and (graph[nx][ny] == 2 or graph[nx][ny] == 3):

                if len(road[team]) == 1:
                    if graph[nx][ny] == 2:
                        road[team].append([nx, ny])
                        road[team].append([x,y])
                    else:
                        continue


                ## 방문했던 길이면 다른 길 찾아보기
                if len(road[team]) >= 2:
                    if road[team][-2][0] == nx and road[team][-2][1] == ny:
                        continue
                
                if graph[nx][ny] == 3:
                    graph[x][y] = graph[nx][ny]
                    graph[nx][ny] = 4
                    match_start_end[(hx,hy)] = (x,y)
                    return 

                ## 처음 방문한 일이면 road에 저장
                road[team].append([nx, ny])

                ## 숫자 바꿔 주기
                graph[x][y] = graph[nx][ny]


                x,y = nx, ny
                break
 
## 머리 사람 x,y => nx, ny로 이동
def head_go(team,x,y):

    for k in range(4):
        nx, ny = x + dxy[k][0], y + dxy[k][1]
        if in_range(nx, ny) and (graph[nx][ny] == 4 or graph[nx][ny] == 3):
            road[team].append([nx,ny])
            return nx, ny
    


def move_one_step():
    global road
    global match_start_end
    road = [[] for _ in range(m)]
    

    for team,sp in enumerate(start_people):
        x, y = sp
        ## 머리 사람 이동
        
        head_x, head_y = head_go(team,x,y)
        find_people(team,x,y, head_x, head_y)
        graph[head_x][head_y] = 1
    
    for g in road:
        print(g)
    print()
 
    

def can_go(x, y):
    if not in_range(x,y):
        return False
    if visited[x][y]:
        return False

    if graph[x][y] == 0 or graph[x][y] == 3:
        return False
    
    return True

## 머리 사람 찾기
def find_k(sx,sy):
    x,y =sx,sy
    queue = deque()
    queue.append([x,y,0])
    visited[x][y] = True

    while queue:
        x,y, cnt = queue.popleft()
        
        if graph[x][y] == 1:

            return [x,y,cnt+1]

        for k in range(4):
            nx, ny = x + dxy[k][0], y + dxy[k][1]
            if can_go(nx, ny):

                if sx==x and sy == y:
                    if graph[nx][ny] != 2:
                        continue

                visited[nx][ny] = True
                queue.append([nx, ny, cnt+ 1])

    return [-1,-1, 0]

def reverse(x,y):
    ex, ey = match_start_end[(x,y)] 
    del match_start_end[(x,y)]
    match_start_end[(ex,ey)] = (x,y)
    graph[x][y], graph[ex][ey] = 3, 1

    


def inital_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    
def strike_one(x,y,d):
    global score
    
    
    inital_visited()
    for i in range(n):
        nx, ny = x + dxy[d][0]*i , y + dxy[d][1]*i

        if graph[nx][ny] != 0 and graph[nx][ny] != 4:
            hx, hy, score_now = find_k(nx, ny)


            if score_now == 0:
                return

            
            score += (score_now)**2
            reverse(hx,hy)
          
            return

 
def strike(rounds):
    
    (rounds%(4*n))//n
    ## right, up, left, down
    direct = rounds%(4*n)
    if direct < n:
        d = 0
        sx = (rounds%(4*n))% n
        sy =0

    elif direct < 2*n:
        d = 1
        sx = n-1
        sy = (rounds%(4*n))% n

    elif direct < 3*n :
        d = 2
        sx = (rounds%(4*n))% n
        sy = n-1

    elif direct < 4*n:
        d = 3
        sx = 0
        sy = (rounds%(4*n))% n

    strike_one(sx, sy, d)

   

def simulate(rounds):
    global start_people
    global match_start_end
    
    move_one_step()
    
 
    strike(rounds)
    start_people = list(match_start_end.keys())
    match_start_end = dict()
    
   
    


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            start_people.append([i, j])

for rounds in range(k):
    simulate(rounds)


print(score)