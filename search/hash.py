# オープンアドレスキャッシュ
class hash:
    def __init__(self, Nin=10**9 + 7):
        self.N = Nin
        self.table=['']*Nin

    def push(self, x):
        n = x % self.N
        if self.table[n] == '':
            self.table[n] = x
        else:
            self.table.append(x)
    
    def search(self, x):
        n = x % self.N
        if self.table[n] == x:
            print('found')
        elif self.table[n] == '':
            print('not found')
        else:
            N2 = len(self.table)
            if N2 == self.N:
                print('not found')
            else:
                for j in range(self.N, N2):
                    if self.table[j] == x:
                        print('found')
                        break
                    elif j == N2-1:
                        print('not found')

hash1 = hash()
hash1.push(1)
hash1.search(1)
hash1.search(2)