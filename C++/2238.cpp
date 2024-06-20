#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main()
{
    int U, N, P;
    string S;
    map<int, vector<string>> info;

    cin >> U >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> S >> P;
        info[P].push_back(S);
    }

    int min_size = 10001;
    int min_key = 10001;

    for (const auto &item : info)
    {
        if (min_size > item.second.size())
        {
            min_size = item.second.size();
            min_key = item.first;
        }
    }

    cout << info[min_key][0] << " " << min_key;
}
