class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        print(s2)
        if s1 in s2:
            print (s2," = ",s1)
            print("exists")
            return True
        else :
            return False
