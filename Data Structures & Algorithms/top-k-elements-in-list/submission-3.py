class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        arr = []
        for key, v in seen.items():
            arr.append([v, key])
        arr.sort(reverse = True)
        res = []
        index = 0
        while index < k:
            res.append(arr[index][1])
            index += 1
        return res