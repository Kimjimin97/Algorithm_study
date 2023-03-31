## 1차원 폭발 게임
## n개의 폭탄이 쌓여있다.

## M개 이상 연속으로 같은 숫자가 적혀있는 폭탄을 제거

## 중력에 의해 위에 있던 폭탄들을 밑으로 떨어지게 된다.

n,m = map(int, input().split())


bombs = []
new_bombs = []

for _ in range(n):
    bombs.append(int(input()))


## 격자 안에서 터지고 떨어지고, start , end point를 관리해서
## 만약에 연속된 숫자가 m개 이상인 경우 새로운 리스트에 추가하지 않는다.
## 그렇지 않은 경우만 새로운 리스트에 추가해준다.

def find_end_idx(start_idx, curr_num):
    
    for end_idx in range(start_idx+1 , len(bombs)):
        if bombs[end_idx] != curr_num:
            return end_idx - 1
    
    return len(bombs) - 1

    ## 반례가 없는지 생각해 보기
    """
    바로 다른 경우
    end_idx != start_idx + 1

    return end_idx == start_idx

    """    


def pop():
    global bombs
    start_idx = 0

    ## 계속 진행할지 체크 플래그
    continue_flag = False
    new_bombs = []
    cnt = 0

    while start_idx < len(bombs):
        end_idx = find_end_idx(start_idx, bombs[start_idx])

        cnt = end_idx - start_idx + 1
        if cnt < m:
            ## new_bombs를 업데이트 해준다. 
            new_bombs += [bombs[start_idx]] * (end_idx - start_idx + 1)
        
        else:
            continue_flag = True

        start_idx = end_idx + 1
    
    bombs = new_bombs

    return continue_flag


    """
    인덱스 관리 반례 생각하기
    start_idx == n-1 일때,
    함수 find_end_idx의 for문은 돌지 않는다.

    """



while True:
    ## 다음 배열 초기화
    can_continue = pop()
    if not can_continue:
        break

print(len(bombs))

for b in bombs:
    print(b)