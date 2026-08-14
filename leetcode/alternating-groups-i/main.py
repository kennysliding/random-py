import heapq
import math
from collections import Counter, defaultdict, deque
from turtle import color
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        if len(colors) < 3:
            return 0

        total_count = 0

        stack = [colors[0], colors[1], colors[2]]

        for idx in range(3, len(colors) + 3):
            stack[idx % 3] = colors[idx % len(colors)]

            if (
                stack[idx % 3] != stack[(idx - 1) % 3]
                and stack[idx % 3] == stack[(idx - 2) % 3]
            ):
                total_count += 1

        return total_count
