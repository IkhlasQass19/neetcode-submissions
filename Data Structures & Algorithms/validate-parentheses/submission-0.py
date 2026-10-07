class Solution:
    def isValid(self, s: str) -> bool:
        valid=True
        array=list(s)
        stack = [] 
        for i in range(len(s))  :
            if s[i]=='(' or s[i]=='{' or  s[i]=='[' :
                stack.append(s[i])
            elif (
                (s[i] == ')' and stack[-1] == '(') or
                (s[i] == '}' and stack[-1] == '{') or
                (s[i] == ']' and stack[-1] == '[')
            ):
                stack.pop()
        # isEmpty
        isEmpty = not bool(stack)
        print("isEmpty: ", isEmpty)
        return isEmpty


