class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minSt = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        #print('the added value is ',val)
  
        if not self.minSt or val <= self.minSt[-1]:
            #print('the minValue added value is ',val)
            self.minSt.append(val)
        else:
            #print('the minValue added value is ',val)
            self.minSt.append(self.minSt[-1])
        '''
        val = min(val, self.minSt[-1] if self.minSt else val)
        self.minSt.append(val)'''

    def pop(self) -> None:
        #print('the removen value is ', self.stack[-1])
        self.stack.pop()
        self.minSt.pop()                

    def top(self) -> int:
        #print('the top value is ',self.stack[-1])
        return self.stack[-1]

    def getMin(self) -> int:
        #print('the  minimum value is ',self.minSt[-1])
        return self.minSt[-1]
        
