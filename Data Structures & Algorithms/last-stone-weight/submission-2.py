class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        
        while len(stones) > 1:
            print(stones)
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            print(x, y)

            if x == y:
                continue
            else:
                heapq.heappush_max(stones, x - y)
        
        if not stones:
            return 0
        return stones[0]