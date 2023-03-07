from collections import deque
n,k = map(int, input().split())

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

r,c = map(int, input().split())
visited = [[False for _ in range(n)] for _ in range(n)]
NOT_EXIXTS = (-1,-1)
curr_cell = (r-1, c-1)

def initalize_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

## 갈 수 없는 조건만 써주기
def can_go(x,y,target_num):
    if not in_range(x,y):
        return False
    
    if visited[x][y] or graph[x][y] >= target_num:
        return False

    return True

def bfs():
    queue = deque()
    dxy = [[-1,0],[0,1],[1,0],[0,-1]]

    cur_x, cur_y = curr_cell
    queue.append([cur_x, cur_y])
    visited[cur_x][cur_y] = True

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dxy[k][0], y + dxy[k][1]
            if can_go(nx, ny, graph[cur_x][cur_y]):
                visited[nx][ny] = True
                queue.append([nx,ny])


def need_update(best_pos, new_pos):
    ## 첫 도달 가능한 위치라면
    ## update가 필요합니다.
    if best_pos == NOT_EXIXTS:
        return True

    best_x, best_y = best_pos
    new_x, new_y = new_pos

    return (graph[new_x][new_y], -new_x, -new_y) > (graph[best_x][best_y], -best_x, -best_y)


def move():
    global curr_cell
    ## visited 초기화인데 global 처리 안해줘도 된다.
    ## 왜냐하면 값 하나를 선택해서 바꿔주기 때문, 붙여주는 것이 아니라
    initalize_visited()
    
    bfs()

    best_pos = NOT_EXIXTS
    for i in range(n):
        for j in range(n):
            ##  초기 값이랑 같으면 안되는 이유?
            if not visited[i][j] or (i,j) == curr_cell:
                continue

            new_pos = (i,j)
            
            if need_update(best_pos, new_pos):
                best_pos = new_pos
    
    if best_pos == NOT_EXIXTS:
        return False
    else:
        curr_cell = best_pos
        return True
            


for _ in range(k):
    ## 움직일 수 있는 경우 - 현재 위치와 다른 경우
    is_moved = move()
    ## 움직일 수 없는 경우 - 현재 위치와 같은 경우
    if not is_moved:
        break

final_x, final_y = curr_cell
print(final_x + 1, final_y + 1 )