def calculation(string):
    if len(string) == 0:
        return

    if string == S:
        print(1)
        exit()
    
    if string[-1] == "A":
        calculation(string[:-1])

    if string[0] == "B":
        calculation(string[1:][::-1])

S = input()
T = input()
calculation(T)
print(0)