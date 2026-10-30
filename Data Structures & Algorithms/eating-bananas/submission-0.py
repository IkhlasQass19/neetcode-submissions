
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, maxPiles = 1, max(piles)
        res = maxPiles

        while start <= maxPiles:
            midle = (start + maxPiles) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / midle)

            if totalTime <= h:
                res = midle
                maxPiles = midle - 1
            else:
                start = midle + 1

        return res
