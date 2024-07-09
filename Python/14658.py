def solve(std_x, std_y):
    count = 0
    for x,y in pos:
        if std_x <= x <= std_x + L and std_y <= y <= std_y + L:
            count += 1
    return count

N,M,L,K = map(int, input().split())
pos = [list(map(int, input().split())) for _ in range(K)]
MAX = 0

for x,_ in pos:
    for _,y in pos:
        bounced_starCount = solve(x,y)
        MAX = max(MAX, bounced_starCount)
print(K - MAX)