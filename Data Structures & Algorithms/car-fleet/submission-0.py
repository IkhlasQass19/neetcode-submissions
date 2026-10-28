
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        time = []
        i = 0
        fleets = 0
        maxTime = 0

        cars = sorted(zip(position, speed), reverse=True)

        while i < n:
            pos, spd = cars[i]
            t = (target - pos) / spd
            time.append(t)

            if t > maxTime:
                fleets += 1
                maxTime = t

            i += 1

        return fleets
