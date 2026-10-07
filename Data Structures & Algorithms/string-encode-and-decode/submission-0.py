from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = " "
        join_str = delimiter.join(strs)
        print(join_str)
        return str(join_str)

    def decode(self, s: str) -> List[str]:
        f = s.split()
        print(f)

        if s.split()==[]:
            print('split is none')
            return [""]

        return f