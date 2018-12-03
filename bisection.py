#eq 2x^2 - 5x + 3
# guess...
x1 = 0
x2 = 1.3

y1 = 2*x1**2 - 5*x1 + 3
y2 = 2*x2**2 - 5*x2 + 3

if (y1 * y2 > 0 ): # checking if they have the same sign
    exit

for i in range(1, 101):
    xh = (x1 + x2)/2 # mean point
    yh = 2*xh**2 - 5*xh + 3
    y1 = 2*x1**2 - 5*x1 + 3
    #y2 = 2*x2**2 - 5*x2 + 3
    # .
    if (abs(y1) < 1e-6):
        break
    elif y1 * yh < 0: # if the root is in the first half
        x2 = xh
    else:
        x1 = xh
print('sol {:2f}'.format(x1))
