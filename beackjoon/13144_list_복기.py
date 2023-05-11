## counting array와 투포인터

## 이 문제에서 각 구간의 시작점을 i로 잡았다고 할 때, 같은 숫자가 3개 이상
## 되지 않도록 최대로 뻗어 나갔을 때의 구간의 끝점을 j로 하여 그림을 그려보면
## 다음과 같다.

## 이러한 상황에서 유용하게 사용될 수 있는 기법이 counting array

## 각 숫자가 몇번 나왔는지 counting 해주는 배열을 추가적으로 만들어 과리
## n개의 숫자가 주어졌을 때, 구간 내에 중복되는 숫자가 전혀 없는 경우 중
## 구간의 크기를 구하는프로그램


n = int(input())


lists = list(map(int, input().split()))

count_array = [0]*100001

count_array[lists[0]] += 1
answer = 0
## 구간내에 중복되는 숫자가 전혀 없는 경우 중 가능한 최대 구간의 크기

answer = 0
j = 0
for i in range(len(lists)):

    while j + 1 < len(lists) and not count_array[lists[j+1]]:
        count_array[lists[j+1]] += 1
        j += 1
    
    
    answer += (j-i+1)
    count_array[lists[i]] -= 1

print(answer)