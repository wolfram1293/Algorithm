import time
import matplotlib.pyplot as plt
def seven(day):
    day = list(str(day))
    day = [int(v) for v in day]
    if 7 in day:
        return True
    else:
        return False

x = [i for i in range(1,8)]
y = []
for i in x:
    time_sta = time.perf_counter()

    n = int(10**i)
    cnt = 0

    for i in range(n+1):
        if seven(i):
            cnt += 1

    time_end = time.perf_counter()
    d = time_end- time_sta
    y.append(d)
    print(d)

print(y)
'''
plt.figure()
plt.plot(x, y)
plt.show()
'''