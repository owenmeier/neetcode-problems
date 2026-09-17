class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) + len(self.minHeap) == 0:
            heapq.heappush_max(self.maxHeap, num)
        elif len(self.maxHeap) + len(self.minHeap) % 2:
            if len(self.maxHeap) > len(self.minHeap):
                heapq.heappush_max(self.maxHeap, num)
                temp = heapq.heappop_max(self.maxHeap)
                heapq.heappush(self.minHeap, temp)
            else:
                heapq.heappush(self.minHeap, num)
                temp = heapq.heappop(self.minHeap)
                heapq.heappush_max(self.maxHeap, temp)

    def findMedian(self) -> float:
        if (len(self.maxHeap) + len(self.minHeap)) % 2:
            return self.maxHeap[0]
        return (self.maxHeap[0] + self.minHeap[0]) / 2