class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            map.setdefault("".join(sorted(word)), []).append(word)
        return list(map.values())