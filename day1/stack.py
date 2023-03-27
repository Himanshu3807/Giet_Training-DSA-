class Stack:
    def _init_(self,max_size):
        self.__max_size = max_size
        self.elements = [None] * self._max_size
        self.__top = -1
        
    def is_full(self):
        if self._top == self._max_size - 1:
            return True
        return False
        
    def is_empty(self):
        if self.__top == -1:
            return True
        return False
        
    def push(self,data):
        if self.is_full():
            print("The stack is full !!")
        else:
            self.__top += 1
            self.elements[self._top] = data
    
    def pop(self):
        if self.is_empty():
            print("The stack is empty !!")
        else:
            data = self.elements[self._top]
            self.__top -= 1
            return data
    
    def display(self):
        if self.is_empty():
            print("The stack is empty !!")
        else:
            index = self.__top
            while index >= 0:
                print(self._elements[index])
                index -= 1
                
    def get_max_size(self):
        return self.__max_size

ball_stack = Stack(4)
print("Is it empty", ball_stack.is_empty())
ball_stack.push(5)
print("Is it empty", ball_stack.is_empty())
ball_stack.push(6)
ball_stack.push(7)
ball_stack.push(8)
ball_stack.display()
print("Size of the stack", ball_stack.get_max_size())
print("The element deleted", ball_stack.pop())
print("After deleting the element")
ball_stack.display()
print("Size of the stack", ball_stack.get_max_size())
