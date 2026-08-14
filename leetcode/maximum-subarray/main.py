import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        global_max = nums[0]

        for num in nums[1:]:
            current_max = max(num, current_max + num)
            global_max = max(global_max, current_max)

        return global_max
