class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, cur, rem):
            
            if rem == 0:
                res.append(cur[:])
                return
            # print(rem, nums[i], cur)
            if i >= len(nums) or rem < 0:
                return
            
            cur.append(nums[i])
            dfs(i, cur, rem - nums[i])
            cur.pop()
            dfs(i + 1, cur, rem)

        dfs(0, [], target)
        return res
            