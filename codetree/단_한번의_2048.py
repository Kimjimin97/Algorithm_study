"""
2개씩 비교하는데 한번만 비교하는 것 tip!
-> keep 이용

tmp_graph만 갱신해주면 된다.

회전 i,j 반대로 잘 되었는지 확인
"""

graph = [
    list(map(int, input().split()))
    for _ in range(4)
]

tmp_graph = []

command  = list(map(str, input().split()))

## 중력이 작용
## 결과 얻기
## 같은 숫자가 만들어지면 두 숫자가 합쳐지게 된다.
n = 4
new_graph = [
        [-1 for _ in range(n)]
        for _ in range(n)
    ]


map_dir = {
    "D":0,
    "R":1,
    "U":2,
    "L":3

}

def rotate():
    ## new graph 갱신이 필요 없는 이유 
    ## 모든 숫자가 바뀌기 때문이다.

    for i in range(n):
        for j in range(n):
            new_graph[i][j] = graph[n-j-1][i]
    
    for i in range(n):
        for j in range(n):
            graph[i][j] = new_graph[i][j]



def drop_col(col):

    tmp_row = n - 1
    keep = -1


    ## keep을 기준으로 생각하기

    for row in range(n-1, -1, -1):
        if graph[row][col] == 0:
            continue
        
        elif keep == -1:
            keep = graph[row][col]
        
        else:
            if graph[row][col] == keep:
                tmp_graph[tmp_row][col] = keep*2
                tmp_row -= 1
                keep = -1
                continue
            
            else:
                tmp_graph[tmp_row][col] = keep
                keep = graph[row][col]
                tmp_row -= 1
    
    if keep != -1:
        tmp_graph[tmp_row][col] = keep
    




def drop():
    global tmp_graph
    tmp_graph = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    for col in range(n):
        drop_col(col)
    

    for i in range(n):
        for j in range(n):
            graph[i][j] = tmp_graph[i][j]
    



for m in command:
    k = map_dir[m]
    for _ in range(k):
        rotate()

    drop()

       
    for _ in range((4-k)%4):
        rotate()
    
for g in graph:
    print(*g)


