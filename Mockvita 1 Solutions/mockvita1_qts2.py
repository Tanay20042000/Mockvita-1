def is_prime(b):
    count = 0
    for j in range(2,b):
        if b%j == 0:
            count += 1
    if count == 0:
        return b

a = input()
a = a.split(" ")
s = int(a[0])
t = int(a[1])
if s>=2 and s<=t and s<=100:
    if t-s >= 35:
        prime = []
        for k in range(s,t+1):
            if is_prime(k):
                prime.append(k)
        new_list = []
        for h in prime:
            for g in prime:
                if h != g:
                    e = str(h)+str(g)
                    if int(e) not in new_list:
                        new_list.append(int(e))
        new_prime = []
        for l in new_list:
            if is_prime(l):
                new_prime.append(l)
        smallest = min(new_prime)
        largest = max(new_prime)
        p = len(new_prime)
        total = 0
        while total < p:
            if total == p-1:
                print(smallest)
            nth = smallest + largest
            smallest = largest
            largest = nth
            total += 1
