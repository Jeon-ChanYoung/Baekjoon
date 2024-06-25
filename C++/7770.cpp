#include <iostream>

using namespace std;

int main() {
    int N, H = 0;
    cin >> N;

    for(int i=1; i<10e9; i++) {
        N -= (i*i + (i-1)*(i-1));
        if (N < 0)  {
            cout << H;
            break;
        }
        H += 1;
    }
}