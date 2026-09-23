class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0  
        s.strip()
        print(s)
        s2 = re.sub(r'[^a-zA-Z0-9]', '', s)
        s3=s2.lower()
        arrayChar =list(s3)
        print(s2)
        j=len(arrayChar)-1
        while (i<len(arrayChar) and j>0 ) :
            if arrayChar[i]!=arrayChar[j] :
                return False
            i+= 1
            j -= 1
        return True