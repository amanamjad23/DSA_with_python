class Stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
        return item
    def pop(self):
        return self.items.pop
    def is_empty(self):
        return self.items==[]
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items            

mystack=Stack()
print(mystack.push("A"))
print(mystack.push("B"))
print(mystack.push("C"))
print(mystack.push("D"))
print(mystack.peek())