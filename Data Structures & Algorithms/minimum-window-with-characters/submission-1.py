class Solution:

    def minWindow(self, s: str, t: str) -> str:

        listChar = list(s)

        minimum_word = ""

        for i in range(len(listChar) - 1):

            stri = ""

            if listChar[i] in t and listChar[i + 1] in t:

                stri = listChar[i] + listChar[i + 1]

                j = i + 2

                while j < len(listChar):

                    if listChar[j] in t:

                        stri += listChar[j]
                        break

                    else:
                        stri += listChar[j]
                        j += 1

                if minimum_word == "" or len(stri) < len(minimum_word):
                    minimum_word = stri

        return minimum_word