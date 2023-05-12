## 세준시에는 고층 빌디이 많다.
## 가장 많은 고층 빌딩이 보이는 고층 빌딩을 찾으려고한다.

n = int(input())

lists = list(map(int, input().split()))

## 기울기 계산기
def line_cal(x,y,nx,ny):
    height = ny - y
    width = nx - x

    return height / width

answer = 0
for i in range(n):
    count = 0

    ## 왼쪽으로 이동
    left_max = 0
    left_set = []

    for j in range(i-1,-1,-1):
        lines = line_cal(i,lists[i],j,lists[j])

        if not left_set:
            left_set.append(lines)
            count += 1

        elif lines < left_set[-1]:
            # print("선택된 높이", lists[j], "최대왼쪽 높이", left_max)
            left_set.append(lines)
            count += 1

        
    # print("left",count)
    ## 오른쪽으로 이동
    right_max = 0
    right_set = []
    for j in range(i+1, n):
        lines = line_cal(i,lists[i],j,lists[j])

        if not right_set:
            right_set.append(lines)
            count += 1

        elif lines > right_set[-1]:
            right_set.append(lines)
            count += 1


    answer = max(answer, count)

print(answer)