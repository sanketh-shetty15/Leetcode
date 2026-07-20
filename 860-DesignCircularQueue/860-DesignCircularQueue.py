# Last updated: 20/07/2026, 18:38:12
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue=[0]*k
        self.f=0
        self.r=0
        self.k=k


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.r%self.k]=value
        self.r+=1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.f=self.f+1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.f%self.k]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.r-1)%self.k]
        

    def isEmpty(self) -> bool:
        return self.f==self.r

    def isFull(self) -> bool:
        return self.r==self.f+self.k