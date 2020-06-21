import math
c = int(input())
t = {}
collision = 0
for i in range(c):
    x,y,v = list(map(int,input().split()))
    i = math.sqrt(((x/v)**2+(y/v)**2))
    if(t.get(i) == None):
        t[i] = 1
    else:
        t[i] += 1
for keys in t:
    if(t[keys] != 1):
        collision += (t[keys]*(t[keys]-1))/2
print(int(collision))
