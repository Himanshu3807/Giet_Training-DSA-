class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.elements = [None] * self.max_size
        self._rear = -1
        self._front = 0
    def is_full(self):
        if self._rear == self.max_size - 1:
            return True
        return False
    def is_empty(self):
        if self._front > self._rear:
            return True
        return False
    def enqueue(self, data):
        if self.is_full():
            print("Queue is full!!!")
        else:
            self._rear += 1
            self.elements[self._rear] = data
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!!!")
        else:
            data = self.elements[self._front]
            self._front += 1
            return data
    def display(self):
        for index in range(self._front, self._rear+1):
            print(self.elements[index])
    def get_max_size(self):
        return self.max_size        
queue1 = Queue(10)
print("Is it full", queue1.is_full())
print("Is it empty", queue1.is_empty())
queue1.enqueue(100)
queue1.display()
queue1.enqueue(200)
queue1.enqueue(300)
queue1.enqueue(400)
queue1.enqueue(500)
queue1.display()
print("Element deleted", queue1.dequeue())
queue1.display()
