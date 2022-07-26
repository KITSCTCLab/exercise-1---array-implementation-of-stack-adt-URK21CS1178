class Stack:
   def __init__(self,s):
    self.size = s
    self.lst = [None]*s
    self.top = -1
   def isFull(self) :
     if self.top == (self.size - 1) :
        return 1
     else :
        return 0
   def isEmpty(self) :
     if self.top == -1 :
        return 1
     else :
        return 0
   def push(self,a):
     if self.isFull() !=1:
        self.top+=1
        self.lst[self.top]=a
        print("Element Sucessfully Added to the stack.")
      else:
        print("Stack is Full.")
        print("Cannot Push an element..")
   def pop(self):
     if self.isEmpty()!=1:
        t=self.lst[self.top]
        del self.lst[self.top]
        self.top-=1
        return t
     else:
        return "Stack is Empty\nCannot Pop an element..."
   def peek(self):
     if self.isEmpty()!=1:
        return self.lst[self.top]
     else:
       print("Stack is Empty.")
   def display(self):
     if self.isEmpty()!=1:
        for i in range(0,self.top+1):
           print(self.lst[i])
     else:
       
# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
