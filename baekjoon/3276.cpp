#include <iostream>

using namespace std;

int main() {
    int N, col = 1, row = 1;
    cin >> N;
    
    while (col * row < N) {
        if (col * row < N) col ++;
        if (col * row < N) row ++;
    } 

    cout << col << " " << row;
}