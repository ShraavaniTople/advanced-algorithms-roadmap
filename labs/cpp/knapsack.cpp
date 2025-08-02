#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

pair<int, vector<int>> knapsack_bottom_up(const vector<int>& W, const vector<int>& V, int C) {
    int n = (int)W.size();
    vector<vector<int>> dp(n+1, vector<int>(C+1, 0));
    for (int i = 1; i <= n; ++i) {
        int w = W[i-1], v = V[i-1];
        for (int c = 0; c <= C; ++c) {
            int skip = dp[i-1][c];
            int take = (w <= c) ? v + dp[i-1][c-w] : INT_MIN/4;
            dp[i][c] = max(skip, take);
        }
    }
    vector<int> chosen;
    int c = C;
    for (int i = n; i >= 1; --i) {
        if (dp[i][c] != dp[i-1][c]) {
            chosen.push_back(i-1);
            c -= W[i-1];
        }
    }
    reverse(chosen.begin(), chosen.end());
    return {dp[n][C], chosen};
}

int main() {
    vector<int> W = {3, 2, 5, 7};
    vector<int> V = {4, 3, 8, 10};
    int C = 10;
    auto res = knapsack_bottom_up(W, V, C);
    cout << res.first << "\n";
    for (int idx : res.second) cout << idx << " ";
    cout << "\n";
    return 0;
}
