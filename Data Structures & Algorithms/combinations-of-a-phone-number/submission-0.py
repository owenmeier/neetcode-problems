class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        res = []
        numMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        # print(len(digits))

        def dfs(i, path):
            if i == len(digits):
                res.append("".join(path[:]))
                return

            # print(i)
            key = digits[i]

            for char in numMap[key]:
                path.append(char)
                dfs(i + 1, path)
                path.pop()
            
        dfs(0, [])
        return res
