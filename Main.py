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
       
return "Stack is Empty."
print("\tExecution Begins:")
s= int(input("Enter the size of the stack:"))
str = Stack(s)
while(1):
ch = int(input("1. Push\n2. Pop \n3. Peek \n4. Display \n5. Exit\n Enter
your Choice:"))
if ch == 1 :
a = int(input("Enter the value you want to push: "))
str.push(a)
elif ch == 2 :
print("The Popped Element from the stack is ",str.pop())
elif ch == 3 :
print ("Top of Stack:",str.peek())
elif ch == 4 :
str.display()
elif ch == 5:
break
else :
print("Enter a valid choice")
print("\tEnd of Execution.")
