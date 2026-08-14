import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def _print_range(self, start: int, end: int) -> str:
        if start != end:
            return f"{start}->{end}"
        else:
            return str(start)

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        start = nums[0]
        end = nums[0]

        output: list[str] = []

        for idx, num in enumerate(nums):
            if idx == 0:
                continue

            if num - nums[idx - 1] == 1:
                end = num
                continue

            # flush the previous range
            output.append(self._print_range(start, end))

            # start from this number
            start = num
            end = num

        # flush the last range
        output.append(self._print_range(start, end))

        return output
