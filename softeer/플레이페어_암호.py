from string import ascii_uppercase

alpha = list(ascii_uppercase)
visited = [False]*(len(alpha))

message = str(input())
key = list(map(str, input()))
graph = [[""]*5 for _ in range(5)]
pointer = -1
pointer2 = 0

end_point = False
location_dict = dict()

## 직접 넣는 방법 이럴 필요는 없을 듯! -> 행,열, 숫자를 기준으로 다시 짜보기
for i in range(5):
    for j in range(5):
        if pointer < len(key):
            while True: 
                pointer += 1
                if pointer == len(key):
                    end_point = True
                    break

                if pointer < len(key) and not visited[ord(key[pointer])- ord("A")]:
                    visited[ord(key[pointer] )- ord("A")] = True
                    graph[i][j] = key[pointer]
                    location_dict[key[pointer]]  = (i,j)
                    break
                

        if end_point:
            while True:
                if pointer2 >= len(alpha):
                    break
                if not visited[pointer2] and pointer2 != ord("J")-ord("A"):
                    visited[pointer2] = True
                    graph[i][j] = chr(pointer2+ord("A"))
                    location_dict[chr(pointer2+ord("A"))] = (i,j)
                    break
                pointer2 += 1




## 두개로 자르기

before_m = ""
new_message = []
i = 0
while i < len(message):
    if i == len(message) -1:
        new_message.append(message[i])
        new_message.append("X")
        break

    if message[i] != message[i+1]:
        new_message.append(message[i])
        new_message.append(message[i+1])
        i += 2
    else:
        new_message.append(message[i])
        if message[i] == "X":
            new_message.append("Q")
        else:
            new_message.append("X")
        i += 1

result_message = ""

## 암호화하기
for i in range(0,len(new_message),2):
    x1,y1,x2,y2 = location_dict[new_message[i]][0] ,location_dict[new_message[i]][1] ,location_dict[new_message[i+1]][0] ,location_dict[new_message[i+1]][1] 
    if x1 == x2:
        result_message += graph[x1][(y1+1)%5] 
        result_message += graph[x2][(y2+1)%5]
    
    elif y1 == y2:
        result_message += graph[(x1+1)%5][y1] 
        result_message += graph[(x2+1)%5][y2]

    else:
        result_message += graph[x1][y2]
        result_message += graph[x2][y1]

print(result_message)