import time
def seven(day):
    day = list(str(day))
    day = [int(v) for v in day]
    if 7 in day:
        return True
    else:
        return False

def cntseven(day):
    ans = 0
    i = 0
    while True:
        if day == 0:
            break
        remainder = day % 10
        if remainder >= 7:
            ans += 1
        day = (day - remainder) / 10
        ans += (10 ** i) *day
        i += 1
    
    return ans


time_sta = time.time()

a, b, n = 1,1,int(10**7)
point = 0
day = 0

day1 = n // a

while True:
    point += a
    if seven(day):
        point += b
    if point >= n:
        break

    day += 1

print(day)
time_end = time.time()
d = time_end- time_sta
print(d)