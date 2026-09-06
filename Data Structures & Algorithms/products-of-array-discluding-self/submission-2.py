class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftArr = []
        leftArr.append(1)
        i = 1
        while i < len(nums):
            leftArr.append(leftArr[i - 1] * nums[i - 1])
            i += 1

        nums.reverse()
        rightArr = []
        rightArr.append(1)
        i = 1
        while i < len(nums):
            rightArr.append(rightArr[i - 1] * nums[i - 1])
            i += 1

        rightArr.reverse()
        
        res = []
        i = 0
        while i < len(nums):
            res.append(leftArr[i] * rightArr[i])
            i += 1
        return res
            

        