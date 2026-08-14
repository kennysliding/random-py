import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ss: set[tuple[str, int, int]] = {
            # shape of ss
            # (current_s, next_s1_idx, next_s2_idx)
            (s3, 0, 0)
        }

        while ss:
            (current_s, next_s1_idx, next_s2_idx) = ss.pop()

            # base case
            if current_s == "" and next_s1_idx == len(s1) and next_s2_idx == len(s2):
                return True

            # compare with s1
            if next_s1_idx < len(s1) and current_s.startswith(s1[next_s1_idx]):
                ss.add((current_s[1:], next_s1_idx + 1, next_s2_idx))

            if next_s2_idx < len(s2) and current_s.startswith(s2[next_s2_idx]):
                ss.add((current_s[1:], next_s1_idx, next_s2_idx + 1))

        # if no more next_s to compare
        return False
