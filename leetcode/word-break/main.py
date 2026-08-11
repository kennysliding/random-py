import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ss: list[str] = [s]
        searched: set[str] = {s}

        while ss:
            next_s = ss.pop()
            for word in wordDict:
                if next_s == word:
                    return True

                if next_s.startswith(word):
                    sliced_s = next_s[len(word) :]

                    if sliced_s not in searched:
                        ss.append(sliced_s)
                        searched.add(sliced_s)
        return False
