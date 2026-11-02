'''class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i=0;
        exist = False
        tempS1 = s1
        while i <len(s2) and tempS1 !="" :
            if s2[i] in tempS1 :
               tempS1=tempS1.replace(s2[i], "", 1)
               exist =True
               i+=1
            else :
                tempS1 = s1 
                exist =False
                i+=1
        if exist and tempS1 !="" :
            exist=False
        return exist
            
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2) - len(s1) + 1):
            tempS1 = s1

            for j in range(i, i + len(s1)):
                if s2[j] in tempS1:
                    tempS1 = tempS1.replace(s2[j], "", 1)
                else:
                    break

            if tempS1 == "":
                return True

        return False

            