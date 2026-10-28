
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = 0
        stackTemp = []
        output = [0] * len(temperatures)

        while i < len(temperatures):
            if stackTemp and temperatures[i] > temperatures[stackTemp[-1]]:
                k = stackTemp.pop()
                output[k] = i - k
            else:
                stackTemp.append(i)
                i += 1

        return output
