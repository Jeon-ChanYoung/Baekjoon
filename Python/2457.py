import sys;input=sys.stdin.readline

N = int(input())
dates = [list(map(int, input().split())) for _ in range(N)]

for date in dates:
    if date[0] < 3:
        date[0] = 3
        date[1] = 1
    if date[2] == 12:
        date[3] = 1

dates.sort()

start = [3,1]
end = [3,1]
count = 0

for date in dates:
    startDay = date[:2]
    endDay = date[2:]

    if start < startDay:
        start = end
        count += 1
        if start < startDay:
            break
    if end < endDay:
        end = endDay

if start < [11, 31]:
    count += 1

if dates[0][:2] > [3,1] or end < [12, 1]:
    count = 0

print(count)
    