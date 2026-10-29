
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        n = len(nums)
        m = int(n / 2)

        while i < n:
            if nums[m] > target:
                n = m
                m = (i + n) // 2

            elif nums[m] < target:
                i = m + 1
                m = (i + n) // 2

            else:
                return m

        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = [row[0] for row in matrix]
        indice = None

        for i in range(0, len(res)):
            if res[i] <= target and (i == len(res)-1 or res[i+1] > target):
                indice = i
                break

        if indice != None and self.search(matrix[indice], target) != -1:
            return True
        else:
            return False
