class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])
        for char in tokens:
            if char not in operators:
                stack.insert(0, char)
            elif char == "+":
                stack.insert(0, (int(stack.pop(0)) + int(stack.pop(0))))
            elif char == "-":
                stack.insert(0, (int(stack.pop(1)) - int(stack.pop(0))))
            elif char == "*":
                stack.insert(0, (int(stack.pop(0)) * int(stack.pop(0))))
            elif char == "/":
                stack.insert(0, (int(stack.pop(1)) / int(stack.pop(0))))
        return int(stack[0])