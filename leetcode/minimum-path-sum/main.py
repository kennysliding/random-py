import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        min_cost_matrix = grid.copy()

        for rowIdx in range(len(grid)):
            for colIdx in range(len(grid[rowIdx])):
                if rowIdx == 0 and colIdx == 0:
                    continue

                from_values = []
                if rowIdx - 1 >= 0:  # from the top
                    from_values.append(min_cost_matrix[rowIdx - 1][colIdx])

                if colIdx - 1 >= 0:  # from the left
                    from_values.append(min_cost_matrix[rowIdx][colIdx - 1])

                from_min_value = min(from_values)
                min_cost_matrix[rowIdx][colIdx] = from_min_value + grid[rowIdx][colIdx]

        return min_cost_matrix[-1][-1]
