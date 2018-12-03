x = 2

for i in range(0, 100):
    xnew = x - ((2*x**2 - 5*x + 3)/(4*x - 5)) # newton-rhapshons method
    if (abs(xnew - x) < 0.0000001):
        break
    x = xnew
print('iteration {} ; sol: {:2f}'.format(i+1, xnew))

# now let's try a more higher degree equation
# eq: x^2 + cos^2x - 4x:
# f'(x) = 2x - sen(x) cos(x) -4
# f'(x) = 2(x - sen(x) cos(x) - 2)

x = 10
from math import sin, cos
for i in range(0, 100):
    xnew = x - ((x**2 - cos(x)**2 - 4*x)/(2*(x - cos(x) * sin(x) - 2))) # newton-rhapshons method
    if (abs(xnew - x) < 0.0000001):
        break
    x = xnew
print('iteration {} ; sol: {:2f}'.format(i+1, xnew))
