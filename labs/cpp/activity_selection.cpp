#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<pair<int,int>> activity_selection(vector<pair<int,int>> a) {
    sort(a.begin(), a.end(), [](const auto& x, const auto& y){ return x.second < y.second; });
    vector<pair<int,int>> chosen;
    int last_finish = numeric_limits<int>::min();
    for (auto [s, f] : a) {
        if (s >= last_finish) {
            chosen.push_back({s, f});
            last_finish = f;
        }
    }
    return chosen;
}

int main() {
    vector<pair<int,int>> acts = {{1,4}, {3,5}, {0,6}, {5,7}, {8,9}, {5,9}};
    auto chosen = activity_selection(acts);
    cout << "Selected activities:\n";
    for (auto [s,f] : chosen) cout << "(" << s << "," << f << ") ";
    cout << "\n";
    return 0;
}
