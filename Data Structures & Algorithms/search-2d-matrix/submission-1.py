
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        n = len(nums)
        m = (i + n) // 2

        while i < n:
            if nums[m] > target:
                n = m
            elif nums[m] < target:
                i = m + 1
            else:
                return m

            m = (i + n) // 2

        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        n = len(matrix)
        indice = None

        while i < n:
            m = (i + n) // 2

            if target < matrix[m][0]:
                n = m
            elif target > matrix[m][-1]:
                i = m + 1
            else:
                indice = m
                break

        if indice != None and self.search(matrix[indice], target) != -1:
            return True
        else:
            return False
