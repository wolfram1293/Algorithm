def seven(day):
    day = list(str(day))
    day = [int(v) for v in day]
    if 7 in day:
        return True
    else:
        return False

def fuga(day):    
    day = list(str(day))
    day = [int(v) for v in day]
    hoge = [0] * len(day)
    digit = 0
    for i in range(len(day)):
        if i != 0:
            hoge[-(i+1)] = int(10**(digit-1)) + hoge[-i] * 9

        digit += 1
    return hoge

def cntseven(day):
    ans = 0
    hoge = fuga(day)
    day = list(str(day))
    day = [int(v) for v in day]
    flag = False
    
    digit = len(day)
    for i in range(len(day)):
        d = day[i]
        digit -= 1

        if flag:
            ans += int(''.join(map(str, day[i:]))) + 1
            break
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
day0 = n // a
hoge = fuga(day0)
ratio = hoge[0] / 10 ** (len(list(str(hoge[0]))))

day = int(n / (a + b * ratio))

point = a * (day + 1) + b * cntseven(day)
if point < n:
    print('a')
    while True:
        day += 1
        point += a
        if seven(day):
            point += b
        if point >= n:
            print(point)
            break

else:
    print('b')
    while True:
        day -= 1
        point -= a
        if seven(day):
            point -= b
        if point == n:
            break
        elif point < n:
            day += 1
            break

print(day)
