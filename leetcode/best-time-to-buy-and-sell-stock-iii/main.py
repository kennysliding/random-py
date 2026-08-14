import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # state machine dynamic problem
        balance_1 = float("-inf")
        max_profit_1 = 0
        balance_2 = float("-inf")
        max_profit_2 = 0

        for price in prices:
            # buy stock at this price ONLY if it has a better price
            # we use 0 - price because thats what we start with
            balance_1 = max(balance_1, 0 - price)
            # sell the first stock holding
            # e.g. sell at $7 for $2 stock = (7 + -2) = $5 profit
            max_profit_1 = max(max_profit_1, price + balance_1)

            #! this is the tricky relationship
            # instead of JUST tracking the min cost of getting the second stock
            # we build the relationship with the first stock:
            # with the profit gained from stock 1, how much max can we keep
            # max_profit_1 - price
            # we should have as much profit from stock 1 as possible,
            # while spending as little as possible in buying stock 2
            balance_2 = max(balance_2, max_profit_1 - price)

            max_profit_2 = max(max_profit_2, price + balance_2)

        return int(max_profit_2)
