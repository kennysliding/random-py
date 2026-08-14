import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # kadane's algorithm
        current_max = 0
        # global_max = 0
        total_profit = 0

        for idx in range(1, len(prices)):
            difference = prices[idx] - prices[idx - 1]

            if current_max + difference > current_max:
                current_max = current_max + difference  # extend and keep holding
                continue

            # if it's smaller, i.e. we are starting to lose the profit, we sell
            total_profit += current_max
            current_max = 0

        # if we are holding at the end, sell all of it
        total_profit += current_max

        return total_profit
