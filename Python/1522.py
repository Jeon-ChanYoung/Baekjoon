string = input()
length = len(string)
Acount = string.count('a')
MIN = 99999
string += string

for i in range(length):
    MIN = min(MIN, string[i:i+Acount].count('b'))

print(MIN)