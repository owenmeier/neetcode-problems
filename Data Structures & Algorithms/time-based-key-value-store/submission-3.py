class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys.setdefault(key, []).append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # print(self.keys)
        # print(self.keys[key])
        if key not in self.keys:
            return ""

        if key in self.keys:
            left = 0
            right = len(self.keys[key]) - 1
            valid = ""

            while left <= right:
                mid = left + (right - left) // 2
                # print(left, mid, right)

                if self.keys[key][mid][1] == timestamp:
                    # print(self.keys[key][mid][0])
                    return self.keys[key][mid][0]

                elif self.keys[key][mid][1] < timestamp:
                    valid = self.keys[key][mid][0]
                    left = mid + 1
                elif self.keys[key][mid][1] > timestamp:
                    right = mid - 1
            
            return valid
