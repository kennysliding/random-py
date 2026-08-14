import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        current = nums[0]
        s = nums[0]

        for num in nums[1:]:
            if num != current + 1:
                break

            s += num
            current = num

        n_set = set(nums)
        while s in n_set:
            s += 1
        return s
