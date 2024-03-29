# 配列を用いたヒープの実装 iに対して親(i-1)//2,左の子2i+1, 右の子2i+2となる
# 追加削除ともにO(log n)
# 最小ヒープ
class minHeap:
    def __init__(self):
        self.list=[]

    def heappush(self,a: int):
        self.list.append(a)
        index = len(self.list) - 1
        while 1:
            parent = (index-1) // 2
            if index == 0:
                break
            if self.list[index] < self.list[parent]:
                self.list[index],self.list[parent] = self.list[parent],self.list[index]
                index = parent
            else: 
                break         

    def heappop(self):
        a = self.list[0]
        self.list[0] = self.list.pop()
        parent = 0        
        while 1:
            c1 = 2*parent + 1
            c2 = 2*parent + 2
            if c2 >= len(self.list):
                c = c1
            else:
                if self.list[c1] > self.list[c2]:
                    c = c2
                else:
                    c = c1
            if c >= len(self.list):
                break
                
            if self.list[c] < self.list[parent]:
                self.list[c],self.list[parent] = self.list[parent],self.list[c]
                parent = c
            else:
                break
        return a

heap = minHeap()
heap.heappush(5)
heap.heappush(3)
heap.heappush(4)
heap.heappop()


# 最大ヒープ
class maxHeap:
    def __init__(self):
        self.list=[]

    def heappush(self,a: int):
        self.list.append(a)
        index = len(self.list) - 1
        while 1:
            parent = (index-1) // 2
            if index == 0:
                break
            if self.list[index] > self.list[parent]:
                self.list[index],self.list[parent] = self.list[parent],self.list[index]
                index = parent
            else: 
                break         

    def heappop(self):
        a = self.list[0]
        self.list[0] = self.list.pop()
        parent = 0        
        while 1:
            c1 = 2*parent + 1
            c2 = 2*parent + 2
            if c2 >= len(self.list):
                c = c1
            else:
                if self.list[c1] < self.list[c2]:
                    c = c2
                else:
                    c = c1
            if c >= len(self.list):
                break
                
            if self.list[c] > self.list[parent]:
                self.list[c],self.list[parent] = self.list[parent],self.list[c]
                parent = c
            else:
                break
        return a


heap2 = maxHeap()
heap2.heappush(5)
heap2.heappush(3)
heap2.heappush(4)
heap2.heappop()

# Algo 2-2
lines=[0 for i in range(6)]
lines[0] = '5'
lines[1] = '1 5'
lines[2] = '1 3'
lines[3] = '2'
lines[4] = '1 4'
lines[5] = '2'
Q = int(lines[0])
heap3 = maxHeap()
for i in range(Q):
    l = [int(x.strip()) for x in lines[i+1].split()]
    if l[0] == 1:
        heap3.heappush(l[1])
    else:
        print(heap3.heappop())
