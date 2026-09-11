class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def isValid(k):
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            return time <= h


        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            if isValid(mid):
                right = mid
            elif not isValid(mid):
                left = mid + 1
            
        
        return left