import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0

        if word1 == "" or word2 == "":
            return max([len(word1), len(word2)])  # delete/only

        dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]

        # fill the top and right edge
        for col_idx in range(len(dp)):
            dp[col_idx][0] = col_idx
        for row_idx in range(len(dp[0])):
            dp[0][row_idx] = row_idx

        # start to run dp
        for col_idx in range(1, len(dp)):
            for row_idx in range(1, len(dp[0])):
                if word1[row_idx - 1] == word2[col_idx - 1]:
                    dp[col_idx][row_idx] = dp[col_idx - 1][row_idx - 1]
                    continue

                dp[col_idx][row_idx] = (
                    min(
                        dp[col_idx - 1][row_idx - 1],  # replace
                        dp[col_idx - 1][row_idx],  # insert
                        dp[col_idx][row_idx - 1],  # delete
                    )
                    + 1
                )

        return dp[-1][-1]
