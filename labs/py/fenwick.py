from typing import List
import random

class FenwickTree:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def prefix_sum(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l: int, r: int) -> int:
        return self.prefix_sum(r) - self.prefix_sum(l - 1)

if __name__ == "__main__":
    n = 10
    ft = FenwickTree(n)
    arr = [0] * (n + 1)
    for _ in range(20):
        idx = random.randint(1, n)
        delta = random.randint(-5, 5)
        arr[idx] += delta
        ft.update(idx, delta)
        # test range sum
        l, r = sorted((random.randint(1, n), random.randint(1, n)))
        naive_sum = sum(arr[l:r+1])
        fenwick_sum = ft.range_sum(l, r)
        print(f"Update index {idx} by {delta} | Range {l}-{r} -> Fenwick {fenwick_sum}, Naive {naive_sum}")
        assert fenwick_sum == naive_sum
