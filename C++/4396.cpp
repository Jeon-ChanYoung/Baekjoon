#include <iostream>
#include <vector>

using namespace std;

int N;
string* searchInfo;
string* mineInfo;

int dx[8] = {0, 1, 1, 1, 0, -1, -1, -1};
int dy[8] = {1, 1, 0, -1, -1, -1, 0, 1};

void nearbyMineCount(int x, int y) {
    int count = 0;
    for(int i=0; i<8; i++) {
        int X,Y;
        X = x+dx[i];
        Y = y+dy[i];
        if ((0 <= X && X < N) && (0 <= Y && Y < N)) {
            if (mineInfo[Y].at(X) == '*') count++;
        }
    }
    cout << count;
}

int main() {
    bool isValid = true;
    cin >> N;

    string line;
    mineInfo = new string[N];
    searchInfo = new string[N];

    for(int i=0; i<N; i++) {
        cin >> line;
        mineInfo[i] = line;
    }

    for(int i=0; i<N; i++) {
        cin >> line;
        searchInfo[i] = line;
    }

    for(int y=0; y<N; y++) {
        for(int x=0; x<N; x++) {
            if (mineInfo[y].at(x) == '*' && searchInfo[y].at(x) == 'x')
                isValid = false;
        }
    }

    for(int y=0; y<N; y++) {
        for(int x=0; x<N; x++) {
            if (searchInfo[y].at(x) == 'x') {
                if (mineInfo[y].at(x) == '.') {
                    nearbyMineCount(x,y);
                } else {
                    cout << "*";
                }
            } else {
                if (mineInfo[y].at(x) == '*' && !isValid) {
                    cout << "*";
                } else {
                    cout << ".";
                }
            }
        }
        cout << "\n";
    }
}