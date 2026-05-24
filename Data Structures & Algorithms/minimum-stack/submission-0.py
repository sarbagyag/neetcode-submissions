class MinStack:

    def __init__(self):
        self.min=float('inf')
        self.stack=[]
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min=val
        else:
            self.stack.append(val-self.min)
            if val<self.min:
                self.min=val

    def pop(self) -> None:
        if not self.stack:
            return
        
        pop=self.stack.pop() #pop pani garne ani top value analyze garna store pani garne
        if pop<0:
            self.min=self.min-pop #pop vaneko difference 

    def top(self) -> int:
        if not self.stack:
            return
        
        top=self.stack[-1]

        if top>0:
            return top+self.min
        else:
            return self.min
        

    def getMin(self) -> int:
        return self.min
        
