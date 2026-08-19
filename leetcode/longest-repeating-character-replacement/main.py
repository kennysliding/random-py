import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # idea
        # for every alphabet
        global_max = 0

        for alphabet_idx in range(ord("A"), ord("A") + 27):
            if chr(alphabet_idx) not in s:
                continue

            start_idx = 0
            end_idx = 0
            k_idx: list[int] = []
            alphabet_max = 0

            while end_idx != len(s):
                # at every new character, we either
                # 1. if same, do nothing
                # 2. if different, change the character into the current alphabet
                # finally, extend the window and update the count

                if s[end_idx] != chr(alphabet_idx):
                    # 2.1 if we have enough k, simply replace the character
                    # 2.2. if we don't have 0k left, then move the start_idx to the closest index where we have more k to move end_idx
                    if k == 0:
                        start_idx = end_idx + 1
                    else:
                        if len(k_idx) == k:
                            start_idx = heapq.heappop(k_idx) + 1

                        heapq.heappush(k_idx, end_idx)

                # print(
                #     chr(alphabet_idx),
                #     start_idx,
                #     end_idx,
                #     s[start_idx : end_idx + 1],
                #     k_idx,
                # )
                alphabet_max = max(alphabet_max, end_idx - start_idx + 1)
                global_max = max(alphabet_max, global_max)

                end_idx += 1

        return global_max


def run_test():
    solve = Solution().characterReplacement
    tests = [(("ABAB", 2), 4), (("AABABBA", 1), 4), (("AABA", 0), 2)]

    for idx, test in enumerate(tests):
        idx += 1
        print(f"== running test {idx} ==")

        print(f"test input: {test[0]}")

        print("-- program output --")
        result = solve(*test[0])
        print("-----")

        expected = test[1]

        if result == expected:
            print(f"Test {idx} passed")
        else:
            print(f"Test {idx} failed: expected {expected}, got {result}")

        print(f"== finished test {idx} ==", end="\n")


run_test()
