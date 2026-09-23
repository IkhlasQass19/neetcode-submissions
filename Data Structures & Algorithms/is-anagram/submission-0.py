class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False;
        S_sorted_text = "".join(sorted(s));
        print(S_sorted_text)
        T_sorted_text = "".join(sorted(t));
        print(T_sorted_text)
        if(S_sorted_text==T_sorted_text) :
            return True
        else :
            return False
