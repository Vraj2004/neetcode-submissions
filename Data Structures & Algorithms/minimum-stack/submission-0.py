class MinStack:

    # [1] -> [1, 2]
    def __init__(self):
        self.stack = []
        self.curr_min = []     

    def push(self, val: int) -> None:
        if not self.curr_min or val < self.curr_min[-1]:
            self.curr_min.append(val)
        else:
            self.curr_min.append(self.curr_min[-1])
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.curr_min.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.curr_min[-1]
        
