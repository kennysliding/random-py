import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        start_idx = 0
        max_length = 0

        mask = [0] * 26

        for idx in range(len(s)):
            mask[ord(s[idx]) - 97] += 1

            while mask[ord(s[idx]) - 97] > 2:
                mask[ord(s[start_idx]) - 97] -= 1
                start_idx += 1

            # print(mask)
            max_length = max(max_length, idx - start_idx + 1)

        return max_length
