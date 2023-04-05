"""
시작시간 - 11 : 16

"""

# 0이상 9 이하의 숫자로만 이루어진 N*M 행렬 모양의 건물에 총 Q 번의 바람이 분다.
#  바람이 괸장이 특이해서 특정 직사각형 영역의 경계에 있는 숫자들을 시계 방향으로 한 칸씩 
# 직사각형 내 영역에 있는 값들을 각각 자신의 위치를 기준으로 자신과 인접한 원소들과 평균 값으로 변한다.

# 순차적으로 일어나는 것이 아니라 동시에 일어난다.

## q 방향이 부는 횟수
n, m , q = map(int, input().split())

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]


new_tmp = [
    [False for _ in range(m)]
    for _ in range(n)
]

r1,c1,r2,c2 = -1,-1,-1,-1
def rotate():
    ## 오른쪽
    global r1
    global r2
    global c1
    global c2
    tmp1 = graph[r1][c2]

    ## c2~c1+1
    for col in range(c2, c1, -1):
        graph[r1][col] = graph[r1][col-1]
    
  
    ## r2~r1+2
    ## 아래
    tmp2 = graph[r2][c2]
    for row in range(r2, r1+1, -1):
        graph[row][c2] = graph[row-1][c2]
    
    

    ## 왼쪽
    ## c1~c2-2
    tmp3 = graph[r2][c1]
    for col in range(c1, c2-1):
        graph[r2][col] = graph[r2][col+1]
    
    
    
    ## r1~r2+2
    tmp4 = graph[r1][c1] 
    for row in range(r1, r2-1):
        graph[row][c1] = graph[row+1][c1]
    
    

    graph[r1+1][c2] = tmp1
    graph[r2][c2-1] =tmp2
    graph[r2-1][c1] = tmp3

dxy = [[1,0],[-1,0],[0,1],[0,-1]]

def in_range(x,y):
    return 0<= x and x < n and 0<=y and y <m

def avera(x,y):
    s = graph[x][y]
    cnt = 1
    for k in range(4):
        nx, ny = x + dxy[k][0], y + dxy[k][1]
        if in_range(nx, ny):
            s += graph[nx][ny]
            cnt += 1
    
    new_tmp[x][y] = s//cnt

def sums():
    global r1
    global r2
    global c1
    global c2
    for i in range(r2-r1+1):
        for j in range(c2-c1+1):
            avera(r1+i,c1+j)
    

def simulate():
    global r1
    global r2
    global c1
    global c2
    rotate()
    
    sums()
    for i in range(r2-r1+1):
        for j in range(c2-c1+1):
            graph[r1+i][c1+j] = new_tmp[r1+i][c1+j]
            # new_tmp[i][j] = 0


for _ in range(q):
    r1,c1,r2,c2 = map(int, input().split())
    r1,c1,r2,c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
    simulate()

for g in graph:
    print(*g)


def rotate(start_row, start_col, end_row, end_col):
    tmp = graph[start_row][start_col]

    for row in range(start_row, end_row):
        graph[row]