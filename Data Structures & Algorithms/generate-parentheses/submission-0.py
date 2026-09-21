class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur, openN, closeN):
            if len(cur) == 2 * n and openN == closeN:
                res.append("".join(cur))
                return

            if openN < n:
                cur.append("(")
                dfs(cur, openN + 1, closeN)
                cur.pop()
            if closeN < openN:
                cur.append(")")
                dfs(cur, openN, closeN + 1)
                cur.pop()

        dfs([], 0, 0)
        return res