class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

        heapq.heapify_max(self.maxHeap)
        heapq.heapify(self.minHeap)

    def addNum(self, num: int) -> None:
        # print(num)
        if len(self.maxHeap) + len(self.minHeap) == 0:
            heapq.heappush_max(self.maxHeap, num)
        elif len(self.maxHeap) + len(self.minHeap) % 2: # true if 1, odd # of num
            if len(self.maxHeap) > len(self.minHeap):
                heapq.heappush_max(self.maxHeap, num)
                temp = heapq.heappop_max(self.maxHeap)
                heapq.heappush(self.minHeap, temp)
            else:
                # print("hello")
                heapq.heappush(self.minHeap, num)
                temp = heapq.heappop(self.minHeap)
                heapq.heappush_max(self.maxHeap, temp)
        # print(self.maxHeap, self.minHeap, num)

    def findMedian(self) -> float:
        # print("find", self.maxHeap, self.minHeap)
        if (len(self.maxHeap) + len(self.minHeap)) % 2:
            return self.maxHeap[0]
        # print(self.maxHeap[0], self.minHeap[0], (self.maxHeap[0] + self.minHeap[0]) / 2)
        return (self.maxHeap[0] + self.minHeap[0]) / 2