#include <iostream>
#include <vector>
#include <ctime>
using namespace std;

int main() {
    time_t now = time(0);
    cout << "C++ environment check" << endl;
    cout << "Current date and time: " << ctime(&now);

    vector<int> arr = {2, 4, 1, 3, 5};
    int inversions = 0;
    for (size_t i = 0; i < arr.size(); ++i) {
        for (size_t j = i + 1; j < arr.size(); ++j) {
            if (arr[i] > arr[j]) inversions++;
        }
    }
    cout << "Sample array: ";
    for (int x : arr) cout << x << " ";
    cout << "\nInversion count: " << inversions << endl;

    return 0;
}
