import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # running a top to bottom approach
        min_cost = [triangle[0]]

        for row in range(1, len(triangle)):
            min_cost.append([])
            print(min_cost[row - 1])
            # for every row, pick the smaller parent
            for idx, leaf in enumerate(triangle[row]):
                parents = []

                if idx - 1 >= 0:  # left parent
                    parents.append(min_cost[row - 1][idx - 1])

                if idx < len(min_cost[row - 1]):  # right parent
                    parents.append(min_cost[row - 1][idx])

                min_cost[row].append(min(parents) + leaf)

        return min(min_cost[-1])
