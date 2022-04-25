
#파이썬 내장 리스트로 구현한 Stack
class ArrayStack:
    def __init__(self):
        self.data=[]
        
    def size(self):
        return len(self.data)
        
    def isEmpty(self):
        return self.size() == 0
    
    def push(self,item):
        self.data.append(item)
        
    def pop(self):
        self.data.pop()
        
    def peek(self):
        return self.data[-1]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    