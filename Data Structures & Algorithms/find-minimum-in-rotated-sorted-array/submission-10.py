class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = math.inf
        left = 0
        right = len(nums) - 1

        while left <= right:
            low = min(low, nums[left], nums[right])
            left += 1
            right -= 1
        return low