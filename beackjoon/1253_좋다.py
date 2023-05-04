n = int(input())

graph = list(map(int, input().split()))

answer = 0


for num_idx, num in enumerate(graph):
    
    tmp = graph[:num_idx] + graph[num_idx + 1:]
    left = 0
    right = len(tmp) - 1


    while left < right:
        if tmp[left] + tmp[right] == num:
            answer += 1
            break

        elif tmp[left] + tmp[right] > num:
            right -= 1

        else:
            left += 1

print(answer)