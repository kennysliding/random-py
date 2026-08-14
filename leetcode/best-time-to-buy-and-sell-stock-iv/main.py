import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        # state machine dynamic problem
        balances = [float("-inf")] * k
        max_profits = [0.0] * k

        for price in prices:
            for k_idx in range(k):
                if k_idx == 0:
                    balances[k_idx] = max(balances[k_idx], 0 - price)
                else:
                    balances[k_idx] = max(
                        balances[k_idx], max_profits[k_idx - 1] - price
                    )
                max_profits[k_idx] = max(max_profits[k_idx], price + balances[k_idx])

        for profit_idx in range(len(max_profits) - 1, -1, -1):
            if max_profits[profit_idx] != float("-inf"):
                return int(max_profits[profit_idx])

        return 0
