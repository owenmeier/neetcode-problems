class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        left = 0
        right = 1
        window = set()
        window.add(s[0])
        largest = 0

        while right < len(s):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            largest = max(largest, len(window))
            right += 1
            
        
        return largest