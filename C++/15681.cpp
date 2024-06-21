#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> connect, currentNodeChild;
vector<int> size;

void makeTree(int currentNode, int parent) {
    for(int Node : connect[currentNode]) {
        if (Node != parent) {
            currentNodeChild[currentNode].push_back(Node);
            makeTree(Node, currentNode);
        }
    }
}

void countSubtreeNodes(int currentNode) {
    size[currentNode] = 1;
    for(int Node : currentNodeChild[currentNode]) {
        countSubtreeNodes(Node);
        size[currentNode] += size[Node];
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N,R,Q,U,V;
    cin >> N >> R >> Q;

    connect.resize(N + 1);
    currentNodeChild.resize(N + 1);
    size.resize(N + 1, 0);

    for(int i=0; i<N-1; i++) {
        cin >> U >> V;
        connect[U].push_back(V);
        connect[V].push_back(U);
    }

    makeTree(R, -1);
    countSubtreeNodes(R);

    for (int i = 0; i < Q; ++i){
        int query;
        cin >> query;
        cout << size[query] << "\n";
    }

    return 0;
}