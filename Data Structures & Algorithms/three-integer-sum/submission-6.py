class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        i = 0
        j = i + 1
        k = len(nums) - 1

        arraay = []
        arrr = sorted(nums)

        while i < len(nums) - 2:

            while j < k:

                total = arrr[i] + arrr[j] + arrr[k]

                if total == 0:

                    row = [arrr[i], arrr[j], arrr[k]]

                    if row not in arraay:
                        arraay.append(row)

                    j += 1
                    k -= 1

                elif total < 0:
                    j += 1

                else:
                    k -= 1

            i += 1
            j = i + 1
            k = len(nums) - 1

        return arraay