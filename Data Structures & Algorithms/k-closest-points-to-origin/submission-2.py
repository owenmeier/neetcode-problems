class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        smallest = []
        heapq.heapify_max(smallest)

        for x, y in points:
            dist = math.hypot(x, y)
            # print(dist)
            heapq.heappush_max(smallest, (dist, x, y))
            # print(smallest)
            if len(smallest) > k:
                heapq.heappop_max(smallest)

        points = [(item[1], item[2]) for item in smallest]

        return points