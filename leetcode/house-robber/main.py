import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # base case
        memo: list[int] = [
            nums[0],  # first house > rob/no rob > max value is rob
            max(nums[0], nums[1]),  # second house > the max of the first two house
        ]

        # starting from the third house
        for idx, value in enumerate(nums):
            if idx == 0 or idx == 1:
                continue
            second_last_house_value = memo[idx - 2]
            last_house_value = memo[idx - 1]

            # if we rob it, i.e. we cannot rob the last one
            rob_value = second_last_house_value + value

            # if we skip it, then we will continue with the value from the last house
            skip_value = last_house_value
            # take the bigger one
            memo.append(max(rob_value, skip_value))

        return memo[-1]
