from typing import List, Tuple

def knapsack_bottom_up(weights: List[int], values: List[int], C: int) -> Tuple[int, List[int]]:
    n = len(weights)
    dp = [[0]*(C+1) for _ in range(n+1)]
    for i in range(1, n+1):
        w = weights[i-1]
        v = values[i-1]
        for c in range(C+1):
            skip = dp[i-1][c]
            take = -10**18
            if w <= c:
                take = v + dp[i-1][c-w]
            dp[i][c] = take if take > skip else skip
    chosen = []
    c = C
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i-1][c]:
            chosen.append(i-1)
            c -= weights[i-1]
    chosen.reverse()
    return dp[n][C], chosen

def knapsack_top_down(weights: List[int], values: List[int], C: int) -> Tuple[int, List[int]]:
    from functools import lru_cache
    n = len(weights)
    @lru_cache(maxsize=None)
    def f(i: int, c: int) -> int:
        if i == n or c == 0:
            return 0
        skip = f(i+1, c)
        take = -10**18
        if weights[i] <= c:
            take = values[i] + f(i+1, c - weights[i])
        return take if take > skip else skip
    chosen = []
    c = C
    i = 0
    while i < n and c >= 0:
        skip = f(i+1, c)
        take = -10**18
        if weights[i] <= c:
            take = values[i] + f(i+1, c - weights[i])
        if take >= skip:
            chosen.append(i)
            c -= weights[i]
            i += 1
        else:
            i += 1
    return f(0, C), chosen

if __name__ == "__main__":
    W = [3, 2, 5, 7]
    V = [4, 3, 8, 10]
    C = 10
    best, items = knapsack_bottom_up(W, V, C)
    print("bottom_up", best, items)
    best2, items2 = knapsack_top_down(W, V, C)
    print("top_down", best2, items2)
