import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def numSub(self, s: str) -> int:
        current_len = 0
        total_s = 0
        mod_v = 10**9 + 7

        for c in s:
            if c == "1":
                # for 1111 > add 1111, 111, 11, 1 > 4
                # for len = 4, add 4
                current_len += 1
                total_s += current_len % mod_v

            if c == "0":
                current_len = 0

        return total_s % mod_v
