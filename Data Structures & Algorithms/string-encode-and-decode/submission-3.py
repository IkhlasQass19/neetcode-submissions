from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = " /"
        join_str = delimiter.join(strs)
        print(join_str)
        return join_str

    def decode(self, s: str) -> List[str]:


        print(len(s))

        f = s.split(' /')
        print(f)

        if s.split(' /') == []:
            print('split is none')
            return [""]

        return f