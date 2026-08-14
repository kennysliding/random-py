import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class NumArray:
    prefix_sums = []

    def __init__(self, nums: List[int]):
        self.prefix_sums = []

        # prefix sum of the first element is 0
        self.prefix_sums.append(0)

        for idx, num in enumerate(nums):
            idx = idx + 1
            self.prefix_sums.append(self.prefix_sums[idx - 1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
