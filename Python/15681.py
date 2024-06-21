import sys;input=sys.stdin.readline

def makeTree(currentNode, parent):
    for Node in connect[currentNode]:
        if Node != parent:
            currentNodeChild[currentNode].append(Node)
            makeTree(Node, currentNode)

def countSubtreeNodes(currentNode):
    size[currentNode] = 1
    for Node in currentNodeChild[currentNode]:
        countSubtreeNodes(Node)
        size[currentNode] += size[Node]

N,R,Q = map(int, input().split())
connect = [[] for _ in range(N+1)]
currentNodeChild = [[] for _ in range(N+1)]
size = [0] * (N+1)

for _ in range(N-1):
    U,V = map(int, input().split())
    connect[U].append(V)
    connect[V].append(U)

makeTree(R, -1)
countSubtreeNodes(R)

for _ in range(Q):
    print(size[int(input())])