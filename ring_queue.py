# リングバッファでの実装

class Queue:
    def __init__(self,size: int):
        self.queue = [None for i in range(size)]
        self.size = size
        self.head = 0
        self.tail = 0

    def enqueue(self,a: int):
        if self.head == (self.tail+1)%self.size:
            print("full")
            return False
        self.queue[self.tail] = a
        self.tail = (self.tail+1)%self.size

    def dequeue(self):
        if self.head == self.tail:
            print("empty")
            return False
        a = self.queue[self.head]
        self.head = (self.head+1)%self.size
        return a

Q = 3
q=Queue(Q)
q.enqueue(1)
q.enqueue(2)
q.dequeue()

# Algo 2-1
lines=[0 for i in range(4)]
lines[0]='3'
lines[1]='1 1000000000'
lines[2]='1 1000000000'
lines[3]='2'
Q=int(lines[0])
for i in range(Q):
    l=[int(x.strip()) for x in lines[i+1].split()]
    if l[0]==1:
        q.enqueue(l[1])
    else:
        print(q.dequeue())
