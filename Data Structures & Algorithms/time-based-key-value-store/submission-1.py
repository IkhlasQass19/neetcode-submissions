
class TimeMap:

    def __init__(self):
        self.myDict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.myDict:
            self.myDict[key] = {}

        self.myDict[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.myDict:
            return ""

        values = self.myDict[key]
        keys = list(values.keys())

        i = 0
        n = len(keys) - 1
        result = ""

        while i <= n:
            m = (i + n) // 2

            if keys[m] == timestamp:
                return values[keys[m]]

            elif keys[m] < timestamp:
                result = values[keys[m]]
                i = m + 1

            else:
                n = m - 1

        return result
