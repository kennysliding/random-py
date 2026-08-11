import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest_len = []

        for idx, num in enumerate(nums):
            if idx == 0:
                longest_len.append(1)
                continue

            # iterate the slice to extend the max
            max_len = 1  # self
            for i in range(0, idx):
                if nums[i] < num:
                    max_len = max(longest_len[i] + 1, max_len)

            longest_len.append(max_len)

        return max(longest_len)
