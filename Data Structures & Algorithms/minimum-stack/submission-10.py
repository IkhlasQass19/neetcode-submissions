class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minSt = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minSt[-1] if self.minSt else val)
        self.minSt.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minSt.pop()                

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minSt[-1]
        
