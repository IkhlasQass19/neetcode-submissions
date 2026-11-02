
'''class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        start = 0
        exist = False
        tempS1 = s1

        while i < len(s2) and tempS1 != "":
            if s2[i] in tempS1:
                tempS1 = tempS1.replace(s2[i], "", 1)
                exist = True
                i += 1
            else:
                start += 1
                i = start
                tempS1 = s1
                exist = False

        if exist and tempS1 != "":
            exist = False

        return exist'''
# Using sliding window

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count = {}

        for c in s1:
            count[c] = count.get(c, 0) + 1

        i = 0
        left = 0
        remaining = len(s1)

        while i < len(s2):
            c = s2[i]

            if count.get(c, 0) > 0:
                remaining -= 1

            count[c] = count.get(c, 0) - 1
            i += 1

            if i - left > len(s1):
                old = s2[left]

                if count[old] >= 0:
                    remaining += 1

                count[old] += 1
                left += 1

            if remaining == 0:
                return True

        return False

