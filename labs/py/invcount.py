from typing import List, Tuple
import random

def count_and_sort(a: List[int]) -> Tuple[List[int], int]:
    n = len(a)
    if n <= 1:
        return a[:], 0
    m = n // 2
    left, cL = count_and_sort(a[:m])
    right, cR = count_and_sort(a[m:])
    merged = []
    i = 0
    j = 0
    cross = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            cross += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, cL + cR + cross

def inversion_count(a: List[int]) -> int:
    _, c = count_and_sort(a)
    return c

def brute_inversions(a: List[int]) -> int:
    n = len(a)
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                c += 1
    return c

if __name__ == "__main__":
    for n in [5, 10, 50, 100]:
        arr = [random.randint(0, 999) for _ in range(n)]
        fast = inversion_count(arr)
        brute = brute_inversions(arr)
        print(n, fast, brute, "OK" if fast == brute else "MISMATCH")
