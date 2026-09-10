class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opener = ['(', '[', '{']
        for char in s:
            if char in opener:
                stack.insert(0, char)
            else:
                if not stack:
                    return False
                lastOpen = stack.pop(0)
                if char == ')' and lastOpen == '(':
                    continue
                elif char == ']' and lastOpen == '[':
                    continue
                elif char == '}' and lastOpen == '{':
                    continue
                else:
                    return False
            

        return len(stack) == 0