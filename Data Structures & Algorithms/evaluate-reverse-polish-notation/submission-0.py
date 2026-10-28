
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        rpnStack = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                num2 = rpnStack.pop()
                num1 = rpnStack.pop()

                match token:
                    case '+':
                        res = num1 + num2
                    case '-':
                        res = num1 - num2
                    case '*':
                        res = num1 * num2
                    case '/':
                        res = int(num1 / num2)

                rpnStack.append(res)
            else:
                rpnStack.append(int(token))

        return rpnStack[0]
