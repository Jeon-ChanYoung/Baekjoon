#include <iostream>
#include <map>

using namespace std;
int year, month, day;
map<int, int> monthEnd;

int isLeapYear() {
    if (month != 2) return 0;
    if (year % 4 == 0 && year % 100 != 0) return 1;
    if (year % 400 == 0) return 1;
    return 0;
}

bool isValid() {
    if (1 > month || month > 12) return false;
    if (1 > day || day > monthEnd[month] + isLeapYear()) return false;
    return true;
}

int main() {
    monthEnd = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}

    while (true) {
        cin >> day >> month >> year;
        if (day == 0 && month == 0 && year == 0) break;

        if (isValid()) {
            cout << "Valid" << endl;
        } else {
            cout << "Invalid" << endl;
        }
    }
}