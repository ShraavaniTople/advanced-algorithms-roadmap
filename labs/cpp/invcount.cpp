#include <iostream>
#include <vector>
using namespace std;

long long merge_count(vector<int>& a, int l, int r, vector<int>& tmp) {
    if (r - l <= 1) return 0;
    int m = l + (r - l) / 2;
    long long c = 0;
    c += merge_count(a, l, m, tmp);
    c += merge_count(a, m, r, tmp);
    int i = l, j = m, k = l;
    while (i < m && j < r) {
        if (a[i] <= a[j]) tmp[k++] = a[i++];
        else {
            tmp[k++] = a[j++];
            c += m - i;
        }
    }
    while (i < m) tmp[k++] = a[i++];
    while (j < r) tmp[k++] = a[j++];
    for (int t = l; t < r; ++t) a[t] = tmp[t];
    return c;
}

long long inversion_count(vector<int> a) {
    vector<int> tmp(a.size());
    return merge_count(a, 0, (int)a.size(), tmp);
}

int main() {
    vector<int> arr = {2, 4, 1, 3, 5};
    cout << inversion_count(arr) << "\n";
    return 0;
}
