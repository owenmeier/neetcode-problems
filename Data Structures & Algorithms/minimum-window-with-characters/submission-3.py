class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortest = ""
        if not t:
            return shortest
        countT = {}
        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1
        window = {}
        have = 0
        need = len(countT)
        res = [-1, -1]

        left = 0
        
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in countT and window.get(s[r]) == countT.get(s[r]):
                have += 1
            while have == need:
                if len(shortest) > len(s[left:r + 1]) or shortest == '':
                    shortest = s[left: r + 1]
                window[s[left]] -= 1
                if s[left] in countT and window.get(s[left]) < countT.get(s[left]):
                    have -= 1
                left += 1

        return shortest