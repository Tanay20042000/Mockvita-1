t = int(input())
if t>=1 and t<=100:
    a = []
    for i in range(t):
        n = int(input())
        a.append(n)
    for j in a:
        if j>=1 and j<=5000:
            sum1 = 0
            count = 0
            while sum1<j:
                count += 1
                sum1 += count
            print(count)
