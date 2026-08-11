import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        path_counts = obstacleGrid.copy()

        for rowIdx in range(len(obstacleGrid)):
            for colIdx in range(len(obstacleGrid[rowIdx])):
                if rowIdx == 0 and colIdx == 0:
                    if obstacleGrid[rowIdx][colIdx] == 1:
                        return 0
                    path_counts[0][0] = 1
                    continue

                # for obstacle
                if obstacleGrid[rowIdx][colIdx] == 1:
                    path_counts[rowIdx][colIdx] = 0
                    continue

                from_count = 0
                if rowIdx - 1 >= 0:  # from the top
                    from_count += path_counts[rowIdx - 1][colIdx]

                if colIdx - 1 >= 0:  # from the left
                    from_count += path_counts[rowIdx][colIdx - 1]

                path_counts[rowIdx][colIdx] = from_count

        return path_counts[-1][-1]
