class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = []
        high = 0
        i = 0
        while i < len(height):
            high = max(high, height[i])
            prefix.append(high)
            i += 1
        high = 0
        i -= 1
        while i >= 0:
            high = max(high, height[i])
            suffix.append(high)
            i -= 1
        suffix.reverse()
        total = 0
        for i in range(len(height)):
            total += min(prefix[i], suffix[i]) - height[i]
        return total