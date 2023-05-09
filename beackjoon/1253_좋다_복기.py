"""
2개를 선택해서 합을 만들 수 있는 숫자를 도출하기
"""

"""
1) 완탐 -> O(NC2*N) -> ndl 2000개 이기 때문에 시간 초과가 난다. 
-> 1억 이상의 시간

2) dp -> 불가능 원하는 state값을 찾아야 하기 때문이다.
-> dp는 주로 최대 최소문제에 사용된다.

3) 투포인터 -> O(N*N)-> 우리는 2개의 포인터를 관리하면 두 수의 합을 정의할 수 있다.
-> 정렬을 시키면 두 포인터의 움직임을 관리할 수 잇다.
-> 원하는 수가 8일 때 l,r 합이 8보다 크면 r 인덱스를 줄여준다.
-> 8 보다 작으면 l 인덱스 값을 증가시킨다.

"""

n = int(input())

lists = list(map(int, input().split()))


answer = 0

lists.sort()

for i in range(len(lists)):
    num = lists[i]
    left = 0
    right = len(lists)-1

    while left < right:
       
        now_num = lists[left] + lists[right]

        if left == i:
            left += 1
            continue

        elif right == i:
            right -= 1
            continue

        if now_num < num:
            left += 1
        
        elif now_num == num:
            answer += 1
            break

        elif now_num > num:
            right -= 1

print(answer)