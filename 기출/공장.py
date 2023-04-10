"""
갯수 상관 없다.
순서만 중요하다.

"""
max_num = 100000

prv = [0]*max_num
nxt = [0]*max_num
head = [0]*max_num
tail = [0]*max_num

box_info = [0]*max_num
def make_factory(command):
    n,m = command[0], command[1]
    co = command[3:]
    # m개의 벨트와 n개의 선물로 이루어진 공장을 세운다.
    # 선물을 주어진 순서대로 m번 벨트까지 올려준다.
    # (고유 번호와 무게가 적혀있다.)
    # 번호는 상자마다 다르지만, 무게가 동일한 상자가 있을 수 있다.
    
    # n개의 벨트
    # m개의 선물
    belt_num = 0
    boxes = [[ [] for _ in range(m)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            boxes[i][j] = (cnt ,command[cnt])
            cnt += 1
    
    for g in boxes:
        print(g)
    print(g)
    

        


    
    return

def put():
    # 산타가 원하는 상자의 최대 무게인 w_max
    # w_max 이하라면 하차 진행
    # 그렇지 않으면 맨뒤로 보낸다.
    # 벨트에 있던 상자가 빠지면 한칸씩 앞으로 내려와야한다
    return

def remove():
    # 산타가 제거하기를 원하는 고유 번호 r_id가 주어진다.
    # 
    return

def check():
    # 산타가 확인하기를 원하는 고유의 번호 f_id
    # 해당 고유 번호에 해당하는 상자가 놓여있는 벨트가 있다면
    # 해당 상자 위에 있는 모든 상자를 전부 앞으로 가져온다
    # 가져올 시 순서는 그래로
    return

def broke():
    # 고장이 발생한 벨트의 번호
    # 바로 오른쪽 벨트부터 순서대로 보며 
    # 아직 고장이 나지 않은 최초의 벨트 위로
    # 
    return

q = int(input())

for _ in range(q):
    command = list(map(int, input().split()))
    c = command[0]
    if c == 100:
        make_factory(command)