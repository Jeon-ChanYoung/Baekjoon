#include <iostream>

using namespace std;

int main() {
    int b,w,square,MAX,temp;
    cin >> b >> w;

    MAX = 0;
    square = 1;
    if (b == 0 && w == 0) {
        cout << "Impossible";
        return 0;
    }
    
    while (square < 200) {
        temp = square * square;

        if (square % 2 == 0) {
            if (b >= temp/2 && w >= temp/2) {
                MAX = max(MAX, square);
            }
        } else {
            if ((b >= temp/2 + 1 && w >= temp/2) || (b >= temp/2 && w >= temp/2 + 1)) {
                MAX = max(MAX, square);
            }
        }
        square++;
    }
    cout << MAX;
}