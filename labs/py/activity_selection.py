from typing import List, Tuple

def activity_selection(activities: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    # Sort by finish time
    activities.sort(key=lambda x: x[1])
    selected = []
    last_finish = float('-inf')
    for start, finish in activities:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish
    return selected

if __name__ == "__main__":
    # Example activities: (start, finish)
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
    chosen = activity_selection(activities)
    print("Selected activities:", chosen)
