import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        s = ""

        for i in range(min_len):
            s += word1[i]
            s += word2[i]

        s += word1[min_len:]
        s += word2[min_len:]

        return s
