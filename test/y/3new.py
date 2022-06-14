import sys
def seven(day):
    day = list(str(day))
    day = [int(v) for v in day]
    if 7 in day:
        return True
    else:
        return False

def cntseven(day):
    ans = 0
    day = list(str(day))
    day = [int(v) for v in day]
    flag = False
    hoge = [0] * len(day)
    digit = 0
    for i in range(len(day)):
        if i != 0:
            hoge[-(i+1)] = int(10**(digit-1)) + hoge[-i] * 9

        digit += 1
    
    digit = len(day)
    for i in range(len(day)):
        d = day[i]
        digit -= 1

        if flag:
            ans += int(''.join(map(str, day[i:]))) + 1
        elif i == len(day) - 1:
            if d >= 7:
                ans += 1
        else:
            if d == 7:
                flag = True
                ans += d * hoge[i]
            elif d < 7:
                ans += d * hoge[i]
            else:
                ans += (d-1) * hoge[i] + int(10**digit)

    return ans

a, b, n = map(int, input().split())
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
