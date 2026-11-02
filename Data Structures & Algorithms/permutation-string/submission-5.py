
class Solution:
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

        return exist
