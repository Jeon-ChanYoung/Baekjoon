H,W = map(int, input().split())
heights = list(map(int, input().split()))
volume = 0

temp = 0
max_height = 0
for height in heights:
    if max_height <= height:
        max_height = height
        volume += temp
        temp = 0
    else:
        temp += max_height - height

temp = 0
max_height = 0
for height in heights[::-1]:
    if max_height < height: # <=이 아닌 이유 : 위 코드와 중복 계산 방지 ex. [4, 3, 4]
        max_height = height
        volume += temp
        temp = 0
    else: 
        temp += max_height - height

print(volume)