#import numpty
from abc import ABCMeta, abstractmethod

class Queue(metaclass=ABCMeta):
    @abstractmethod
    def enqueue(self, item):
        pass
    @abstractmethod
    def dequeue(self):
        pass
    @abstractmethod
    def front(self):
        pass
    @abstractmethod
    def isEmpty(self):
        pass
    @abstractmethod
    def isFull(self):
        pass
        
class QueueCircular(Queue):
    def __init__(self, queueSize):
        self.size = queueSize
        self.data = [None] * self.size
        self.deq = 0
        self.length = 0
        
    def enqueue(self, item):
        if self.isFull():
            return
        else:
            self.data[(self.deq + self.length) % self.size] = item
            self.length += 1
    
    def dequeue(self):
        if self.isEmpty():
            return
        else:
            temp = self.data[self.deq]
            self.data[self.deq] = None
            self.deq = (self.deq + 1) % self.size
            self.length -= 1
            return temp
    
    def front(self):
        if self.isEmpty():
            return
        else:
            return self.data[self.deq]
        
    def isEmpty(self):
        return self.length == 0
        
    def isFull(self):
        return self.length == self.size
        
q = QueueCircular(5)
q.enqueue("A")
print(q.front())
print(q.dequeue())

print("Queue three:")
q = QueueCircular(5)
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print("Queue full 5:")
q = QueueCircular(5)
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")
q.enqueue("E")
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print("Go circular:")
q = QueueCircular(5)
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")
q.enqueue("E")
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue("F")
q.enqueue("G")
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print("Really big:")
size = 1000
q = QueueCircular(size)
for i in range(1, size + 1):
    q.enqueue(i)
for i in range(1, size + 1 - 3):
    q.dequeue()
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())