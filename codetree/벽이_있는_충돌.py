"""
오답 노트

1. 중간에 상태를 바꿔서 저장하면 나중에서 결과값에 영향을 미칠 수 있다.
2. 1차원 리스트에 여러 객체를 관리할 수 있다.
3. 방향설정
4. count graph 중간에 갱신해주면 안된다. marble모두 탐색하고 갱신해주어야한다.
5. marbles 초기값 갱신

"""

T = int(input())    
n = 0
m = 0


count_graph = [
    [0 for _ in range(n)]
    for _ in range(n)
]

marbles = []

dxy = [[0,1],[1,0],[-1,0],[0,-1]]

map_dir = {
    "R":0,
    "D":1,
    "L":3,
    "U":2
}

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def move_all():

    for i, marble in enumerate(marbles):
        x,y,k = marble
        nx, ny = x + dxy[k][0], y + dxy[k][1]

        if not in_range(nx, ny):
            nx, ny = x,y
            k = (3-k)
        

        count_graph[nx][ny] += 1
        marbles[i] = [nx, ny, k]


def clear_duplicate_marble():
    global marbles

    tmp = []

    for i, marble in enumerate(marbles):
        x,y,k = marble

        if count_graph[x][y] == 1:
            tmp.append(marble)

    marbles = tmp


def simulate():
    ## 여러 객체가 모두 한번씩 움직이는 것 구현

    ## count graph 갱신

    move_all()

    clear_duplicate_marble()


for _ in range(T):
    n,m = map(int, input().split())

    marbles = []

    ## 구슬의 정보 입력 받기
    for _ in range(m):
        a,b,d = map(str, input().split())
        marbles.append([int(a)-1, int(b)-1, map_dir[d]])

    
    for _ in range(2*n):

        count_graph = [
            [0 for _ in range(n)]
            for _ in range(n)
        ]

        simulate()


    print(len(marbles))