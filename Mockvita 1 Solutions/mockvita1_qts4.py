n = int(input())
a = input()
a = a.split(" ")
r1 = int(a[0])
r2 = int(a[1])
target = int(input())
if n>=5 and n<=100:
    if r1>=500 and r1<=5000:
        if r2>=500 and r2<=5000:
            if target>=0 and target<90000000:
                res1 = []
                res2 = []
                mon = 0
                fin = 0
                month = [31,28,31,30,31,30,31,31,30,31,30,31]
                for j in range(12):
                    for k in range(1,month[j]+1):
                        res1.append((6-(j+1))**2 + abs(k-15))
                    res2.append(res1)
                    res1 = []
                for i in range(n + 1):
                    for j in res2:
                        for k in j:
                            if k>=n:
                                t = n-i
                                mon += (i*r1) + (t*r2)
                            else:
                                h = n-i
                                t = k-h
                                if t<=0:
                                    mon += k*r2
                                else:
                                    mon += (t*r1) + (h*r2)
                        fin += mon
                        mon = 0
                    if(fin >= target):
                        print(i)
                        break
                    else:
                        fin = 0
                else:
                    print(n)
