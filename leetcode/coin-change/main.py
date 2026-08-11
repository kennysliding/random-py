import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom up approach
        # 0 = $0 with 0 coin
        number_of_coins = [0]

        for i in range(1, amount + 1):
            min_number = None

            has_coin = False
            for coin in coins:
                if i - coin >= 0 and number_of_coins[i - coin] != -1:
                    has_coin = True
                    if not min_number:
                        min_number = number_of_coins[i - coin] + 1
                        continue
                    min_number = min(min_number, number_of_coins[i - coin] + 1)

            if not has_coin:
                number_of_coins.append(-1)
                continue

            number_of_coins.append(min_number)

        return number_of_coins[-1]
