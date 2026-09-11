class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def find(left, right):
            if left > right:
                return -1
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return find(left, mid - 1)
            elif nums[mid] < target:
                return find(mid + 1, right)
        
        return find(0, len(nums) - 1)