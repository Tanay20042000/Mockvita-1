x_l = int(input())
y_l = int(input())
x_w = int(input())
y_w = int(input())
f = float(input())
if x_l>=0 and x_l<100:
    if y_l>=0 and y_l<100:
        if x_w>=0 and x_w<100:
            if y_w>-500 and y_w<0:
                if f>1 and f<=15:
                    if y_l + y_w == 0:
                        a = x_l * f
                        a = int(a)
                        print("{0:.6f}".format(a))
