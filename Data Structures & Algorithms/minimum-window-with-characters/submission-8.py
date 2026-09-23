'''class Solution:
    def minWindow(self, s: str, t: str) -> str:
        listChar = list(s)
        stri=""
        minimum_word=""
        for i in range(len(listChar)-1):
            if listChar[i] in t and listChar[i+1] in t:
                print(listChar[i],listChar[i+1])
                stri =listChar[i]+listChar[i+1]
                print('stri:',stri)
                j=i+2
                while j< len(listChar) :
                    if listChar[j] in t :
                        print('listChar[j]', listChar[j])
                        stri +=listChar[j]
                        break
                    else :
                        stri +=listChar[j]
                        j+=1
                print('output stri',stri)
                if (len(minimum_word) >len(stri)  and j<len(listChar)) or minimum_word =="" :
                    minimum_word=stri
                    stri=""
        return minimum_word'''
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        count_t = Counter(t)
        window = {}

        have = 0
        need = len(count_t)

        left = 0
        min_len = float("inf")
        min_start = 0

        for right in range(len(s)):
            char = s[right]

            window[char] = window.get(char, 0) + 1

            if char in count_t and window[char] == count_t[char]:
                have += 1

            # Try to shrink the window
            while have == need:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[min_start:min_start + min_len]