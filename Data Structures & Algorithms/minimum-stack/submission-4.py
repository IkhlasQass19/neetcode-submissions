'''class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minSt = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        print('the added value is ',val)
        if not self.minSt or val <= self.minSt[-1]:
            print('the minValue added value is ',val)
            self.minSt.append(val)
        else:
            print('the minValue added value is ',val)
            self.minSt.append(self.minSt[-1])

    def pop(self) -> None:
        print('the removen value is ', self.stack[-1])
        self.stack.pop()
        self.minSt.pop()

    def top(self) -> int:
        print('the top value is ',self.stack[-1])
        return self.stack[-1]

    def getMin(self) -> int:
        print (self.minSt[-1])
        print('the  minimum value is ',self.minSt[-1])
        return self.minSt[-1]
        '''
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
