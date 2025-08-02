#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <cassert>
using namespace std;

struct FenwickTree {
    int n;
    vector<int> bit;
    FenwickTree(int n): n(n), bit(n+1, 0) {}

    void update(int i, int delta) {
        while (i <= n) {
            bit[i] += delta;
            i += i & -i;
        }
    }

    int prefix_sum(int i) {
        int s = 0;
        while (i > 0) {
            s += bit[i];
            i -= i & -i;
        }
        return s;
    }

    int range_sum(int l, int r) {
        return prefix_sum(r) - prefix_sum(l - 1);
    }
};

int main() {
    srand(time(0));
    int n = 10;
    FenwickTree ft(n);
    vector<int> arr(n+1, 0);
    for (int t = 0; t < 20; ++t) {
        int idx = rand() % n + 1;
        int delta = rand() % 11 - 5;
        arr[idx] += delta;
        ft.update(idx, delta);
        int l = rand() % n + 1;
        int r = rand() % n + 1;
        if (l > r) swap(l, r);
        int naive_sum = 0;
        for (int i = l; i <= r; ++i) naive_sum += arr[i];
        int fenwick_sum = ft.range_sum(l, r);
        cout << "Update index " << idx << " by " << delta
             << " | Range " << l << "-" << r
             << " -> Fenwick " << fenwick_sum
             << ", Naive " << naive_sum << endl;
        assert(fenwick_sum == naive_sum);
    }
    return 0;
}
