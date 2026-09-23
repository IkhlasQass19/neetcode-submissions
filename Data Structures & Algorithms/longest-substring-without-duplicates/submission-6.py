class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        listChar = list(s)
        '''for i in range(len(listChar)):
            while listChar[i] in stri:
                stri = stri[1:]
            stri += listChar[i]
            count = max(count, len(stri))'''
        #return count
        lista = []
        count = 0

        for i in listChar:

            if i not in lista:
                lista.append(i)

            else:
                count = max(count, len(lista))

                index = lista.index(i)
                lista = lista[index + 1:]
                lista.append(i)

        return max(count, len(lista))