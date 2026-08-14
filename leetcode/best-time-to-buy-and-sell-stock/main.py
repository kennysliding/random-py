import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # kadane's algorithm
        current_max = 0
        global_max = 0

        for i in range(1, len(prices)):
            difference = prices[i] - prices[i - 1]

            current_max = max(0, current_max + difference)
            global_max = max(global_max, current_max)

        return global_max
