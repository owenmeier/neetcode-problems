class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)
        maxCount = 1

        if not nums:
            return 0
        
        cur = nums[0]
        i = 1
        count = 1
        while i < len(nums):
            if nums[i] == cur:
                i += 1
                continue
            if nums[i] > cur + 1:
                maxCount = max(count, maxCount)
                count = 1
            elif nums[i] == cur + 1:
                count += 1
                maxCount = max(count, maxCount)
            cur = nums[i]
            i += 1
        return maxCount