class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = []
        heapq.heapify(largest)

        for num in nums:
            # print(largest)
            heapq.heappush(largest, num)
            if len(largest) > k:
                heapq.heappop(largest)

        return largest[0]