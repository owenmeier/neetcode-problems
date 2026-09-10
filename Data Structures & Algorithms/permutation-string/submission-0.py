class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        chars = {}
        target = {}
        for i in range(len(s1)):
            target[s1[i]] = target.get(s1[i], 0) + 1
            chars[s2[i]] = chars.get(s2[i], 0) + 1
        left = 0
        for right in range(len(s1), len(s2)):
            if chars == target:
                return True

            chars[s2[right]] = chars.get(s2[right], 0) + 1

            chars[s2[left]] -= 1
            if chars[s2[left]] <= 0:
                del chars[s2[left]]
            left += 1
        return chars == target