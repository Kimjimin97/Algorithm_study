"""
1) 완탐 -> O(N*K*K) -> 
문자열 슬라이싱 혹은 리스트 슬라이싱에는 길이만큼 시간복잡도가 걸린다.


1) 같은 문자열이 있을 때 문자열을 짜르고 다시 붙인다.
-> 문자열 슬라이싱에 n 만큼 시간이 걸린다.

2) 리스트로 저장한다음 리스트를 자르고 다시 붙인다
-> 리스트를 자르고 다시 붙이는데 n 만큼 시간이 걸린다.

자르지 않는 방식으로 진행해야 한다.
stack에 거꾸로 집어 넣으면 우리는 문자열 혹은 리스트를 자르지 않고
문자를 추가할 수 있다.
대신 뺄 때는 전체 문자열 길이만큼이 아니라
36자리수 만큼 빠지기 때문에 
시간 복잡도 측면에서 효율적일 수 있다.

"""
import sys

strings = list(map(str, input()))

pop_strings = list(map(str, input()))

stacks = []

for s in strings:
    # print(strings, pop_strings)
    stacks.append(s)

    while True:
        if stacks[-len(pop_strings):] == pop_strings:
            for _ in range(len(pop_strings)):
                stacks.pop()
        else:
            break

if not stacks:
    print("FRULA")
else:
    print("".join(stacks))    
        