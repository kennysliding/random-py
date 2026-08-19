import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Only track rows that actually have reservations (n can be up to 10^9,
        # so we can't allocate an array of size n).
        # bits 7..0 represent seats 2..9 (seat 2 -> bit 0, ..., seat 9 -> bit 7)
        rows = defaultdict(int)

        for row, col in reservedSeats:
            if col == 1 or col == 10:
                continue
            rows[row] |= 1 << (col - 2)

        left_mask = 0b00001111  # seats 2,3,4,5
        middle_mask = 0b00111100  # seats 4,5,6,7
        right_mask = 0b11110000  # seats 6,7,8,9

        # Fully empty rows each fit 2 families
        total_families = 2 * (n - len(rows))

        for mask in rows.values():
            if (
                (mask & left_mask) == 0
                or (mask & middle_mask) == 0
                or (mask & right_mask) == 0
            ):
                total_families += 1

        return total_families


def run_test():
    solve = Solution().maxNumberOfFamilies
    tests = [
        ((3, [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]), 4),
        ((4, [[4, 3], [1, 4], [4, 6], [1, 7]]), 4),
        ((4, [[2, 10], [3, 1], [1, 2], [2, 2], [3, 5], [4, 1], [4, 9], [2, 7]]), 3),
    ]

    for idx, test in enumerate(tests):
        idx += 1
        print(f"== running test {idx} ==")

        print(f"test input: {test[0]}")

        print("-- program output --")
        result = solve(*test[0])
        print("-----")

        expected = test[1]

        if result == expected:
            print(f"Test {idx} passed")
        else:
            print(f"Test {idx} failed: expected {expected}, got {result}")

        print(f"== finished test {idx} ==", end="\n")


run_test()
