class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i], ((target - position[i]) / speed[i])])
        cars.sort(reverse=True, key=lambda x: x[0])

        stack = []
        for spot, time in cars:
            # print(spot, time)
            stack.append(time)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)