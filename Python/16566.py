from bisect import bisect_right

def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])
    return parent[node]

N,M,K = map(int, input().split())
cards = sorted(list(map(int, input().split()))) + [1e9]
inputCards = list(map(int, input().split()))
parent = list(range(N+1))

for card in inputCards:
    number = cards[bisect_right(cards, card)]
    root = find(number)
    number = cards[bisect_right(cards, root)]
    parent[root] = number
    print(root)