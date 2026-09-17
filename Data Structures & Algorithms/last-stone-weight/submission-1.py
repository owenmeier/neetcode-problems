class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        stones.sort()
        while len(stones) > 1:
            print(stones)
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            elif stones[-1] > stones[-2]:
                stones[-2] = stones[-1] - stones[-2]
                stones.pop()
            stones.sort()
        if not stones:
            return 0
        return stones[0]