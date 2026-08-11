import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        # base cases
        # 1/f = 1
        # 2/f = 2
        # 3/f = ([n - 1]) + ([n - 2])
        memo: list[int] = [1, 2]

        for _ in range(2, n):
            # maintain only 2 elements
            memo.append(memo[0] + memo[1])
            memo.pop(0)

        print(memo[-1])
        return memo[-1]
