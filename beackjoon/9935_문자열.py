import sys

strings = list(map(str, sys.stdin.readline().strip()))
pop_string = list(map(str, sys.stdin.readline().strip()))

# stack에 집어 넣는다.
# 끝글자가 같으며
stack = []

for s in strings:


    stack.append(s)
    
    if stack[-1] == pop_string[-1] and len(stack) >= len(pop_string):
        if stack[-len(pop_string):] == pop_string:
            for _ in range(len(pop_string)):
                stack.pop()

    


if not stack:
    print("FRULA")
else:
    print("".join(stack))