from collections import deque

def search(word):
    Q = deque()
    visit = [False] * (len(word)+1)

    if word[0] in c1:
        visit[0] = True
        Q.append(1)
    if word[:2] in c2:
        visit[0] = True
        visit[1] = True
        Q.append(2)
    
    while Q:
        index = Q.popleft()
        if index == len(word):
            print("YES")
            return
        elif index > len(word):
            continue
        
        if not visit[index] and word[index] in c1:
            visit[index] = True
            Q.append(index+1)
        if not visit[index+1] and word[index : index+2] in c2:
            visit[index] = True
            visit[index+1] = True
            Q.append(index+2)
    print("NO")

c1 = {'h', 'b', 'c', 'n', 'o', 'f', 'p', 's', 'k', 'v', 'y', 'i', 'w', 'u'}

c2 = {"ba", "ca" , "ga", "la", "na", "pa", "ra", "ta", "db", "nb", "pb", "rb", "sb", "tb", "yb", "ac",
	 "sc", "tc", "cd", "gd", "md", "nd", "pd", "be", "ce", "fe", "ge", "he", "ne", "re", "se", "te",
	 "xe", "cf", "hf", "rf", "ag", "hg", "mg", "rg", "sg", "bh", "rh", "th", "bi", "li", "ni", "si",
	 "ti", "bk", "al", "cl", "fl", "tl", "am", "cm", "fm", "pm", "sm", "tm", "cn", "in", "mn", "rn",
	 "sn", "zn", "co", "ho", "mo", "no", "po", "np", "ar", "br", "cr", "er", "fr", "ir", "kr", "lr",
	 "pr", "sr", "zr", "as", "cs", "ds", "es", "hs", "os", "at", "mt", "pt", "au", "cu", "eu", "lu",
	 "pu", "ru", "lv", "dy"}

for _ in range(int(input())):
    word = input()
    search(word)

