## 완벽한 피자 도우를 만드는 알고리즘
"""
1. 밀가루 양이 가장 작은 위치에 밀가루 1만큼 더 넣어준다.
(가장 작은 위치가 여러개 모두 넣기)
2. 도우를 말아준다
3. 도우를 꾹 눌러준다.
4. 도우를 두 번 반으로 접어준다
5. 3의 과정만 한 번 더 진행한다.

"""


n, k = map(int, input().split())

graph = [
    [0 for _ in range(n)] 
    for _ in range(n)
]

input_lists = list(map(int, input().split()))

for i in range(n):
    graph[i][0] = input_lists[i]

def put_floor():
    min_num = 30001
    min_idx_list = []
    for i in range(n):
        min_num = min(min_num, graph[i][0])
    
    for i in range(n):
        if graph[i][0] == min_num:
            graph[i][0] += 1

def rotate(start_row ,row, col):
    tmp_graph = [
        [0 for _ in range(col)]
        for _ in range(row)
    ]
    
    store_x, store_y = start_row + row, 1
    for i in range(row):
        for j in range(col):
            ## 저장할 숫자
            num = graph[start_row+i][j]
            tmp_graph[i][j] = num
            graph[start_row+i][j] = 0

    

    for i in range(col):
        for j in range(row):
            graph[store_x + i][store_y + j] = tmp_graph[row-j-1][i]
    return


def roll():
    ## 몇번 반복 하나?
    row_up_num = 0
    col_up_num = 1
    start_row = 0

    while True:
        if col_up_num == row_up_num:
            col_up_num += 1
        
        else:
            row_up_num += 1
        
        if n - start_row - row_up_num < col_up_num:
            break
        
        rotate(start_row, row_up_num, col_up_num)
        start_row += row_up_num

def in_range(x,y):
    return 0 <= x and x < n and 0<=y and y<n

def push():
    visited = [
        [False for _ in range(n)]
        for _ in range(n)
    ]   
    dxy = [[1,0],[-1,0],[0,1],[0,-1]]

    tmp = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                visited[i][j] = True
                for k in range(4):
                    nx, ny = i + dxy[k][0], j + dxy[k][1]
                    if in_range(nx, ny) and not visited[nx][ny] and graph[nx][ny] !=0:
                        a,b = graph[i][j], graph[nx][ny]
                        d = abs(a-b)//5
                        
                        if a > b:
                            tmp[i][j] -= d
                            tmp[nx][ny] += d
                        else:
                            tmp[i][j] += d
                            tmp[nx][ny] -= d
    
    
    for i in range(n):
        for j in range(n):
            graph[i][j] += tmp[i][j]
    

def one_line():
    tmp_graph = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    tmp_row = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j]!=0:
                tmp_graph[tmp_row][0] = graph[i][j]
                tmp_row += 1
    
    for i in range(n):
        for j in range(n):
            graph[i][j] = tmp_graph[i][j]
    
def fold_two_half():
    
    

    for row in range(n//2):
        num = graph[row][0]
        graph[row][0] = 0
        graph[n-row-1][1] = num
    
   
    
    for row in range(n//2,n-n//4):
        num1 = graph[row][0]
        num2 = graph[row][1]

        graph[row][0] = 0
        graph[row][1] = 0
        graph[n//2-row-1][2] = num2
        graph[n//2-row-1][3] = num1
        
  
def cal_k():
    min_num, max_num = float("INF"), 0

    for i in range(n):
        min_num = min(graph[i][0],min_num)
        max_num = max(graph[i][0],max_num)
   
    return max_num - min_num

def simulate():
    put_floor()
    roll()
    push()
    one_line()
    fold_two_half()
    push()
    one_line()
    

for rounds in range(n*n):
    simulate()
    count = cal_k()

    if count <= k:
        print(rounds+1)
        break

# for g in graph:
#     print(g)
# print()
