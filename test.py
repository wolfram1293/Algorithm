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

    a, b, n = 1,1,int(10**i)
    point = 0
    day = 0

    while True:
        point += a
        if seven(day):
            point += b
        if point >= n:
            break

        day += 1

    time_end = time.perf_counter()
    d = time_end- time_sta
    y.append(d)
    print(d)

plt.figure()
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y)
plt.show()