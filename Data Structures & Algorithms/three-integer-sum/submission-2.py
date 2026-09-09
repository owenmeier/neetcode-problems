class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        nums = sorted(nums)
        print(nums)

        for i in range(len(nums)):
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right]
                # print(target, nums[left], nums[right], sum)
                if sum == target:
                    results.add(tuple([-target, nums[left], nums[right]]))
                    left += 1
                    right -= 1
                    continue
                if sum < target:
                    left += 1
                if sum > target:
                    right -= 1
        return list(results)