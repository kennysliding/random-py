import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 2 rows
        dp = [[0] * (len(matrix[0]) + 1) for _ in range(2)]
        max_side = 0

        for row_idx in range(len(matrix)):
            for col_idx in range(len(matrix[0])):
                if matrix[row_idx][col_idx] == "0":
                    dp[row_idx % 2][col_idx + 1] = 0
                    continue

                # check the top
                dp[row_idx % 2][col_idx + 1] = (
                    min(
                        dp[(row_idx - 1) % 2][col_idx + 1],  # top
                        dp[row_idx % 2][col_idx],  # left
                        dp[(row_idx - 1) % 2][col_idx],  # top left
                    )
                    + 1
                )

                max_side = max(dp[row_idx % 2][col_idx + 1], max_side)
        return max_side**2
