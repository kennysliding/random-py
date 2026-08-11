import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        players = [0, 0]  # alice and bob
        turn = 0

        remaining_piles = piles.copy()

        for _ in range(len(piles) - 1):
            head_pile = remaining_piles[0]
            tail_pile = remaining_piles[-1]

            print(remaining_piles, head_pile, tail_pile)

            # take the largest from head/tail
            if head_pile >= tail_pile:
                players[turn] += head_pile
                remaining_piles = remaining_piles[1:]
                turn = (turn + 1) % 2
                continue

            if tail_pile > head_pile:
                players[turn] += tail_pile
                remaining_piles = remaining_piles[:-1]
                turn = (turn + 1) % 2
                continue

        # the last pile to the player
        players[turn] += remaining_piles[0]

        print(players)
        return players[0] > players[1]
