def eratosthenes(n):
    prime = [2]
    lim = int(n**0.5)
    d = [i + 1 for i in range(2,n,2)]
    while True:
        p = d[0]
        if lim < p:
            prime += d
            break
        prime.append(p)
        d = [x for x in d if x % p != 0]
    return prime
