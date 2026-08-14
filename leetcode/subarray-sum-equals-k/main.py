import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        rolling_prefix_sum = 0
        prefix_sum_freq: dict[int, int] = {0: 1}
        c = 0

        # left - right = k -> right = left - k

        for idx in range(len(nums)):
            rolling_prefix_sum = nums[idx] + rolling_prefix_sum

            if rolling_prefix_sum - k in prefix_sum_freq:
                c += prefix_sum_freq[rolling_prefix_sum - k]

            prefix_sum_freq[rolling_prefix_sum] = (
                prefix_sum_freq.get(rolling_prefix_sum, 0) + 1
            )

        return c
