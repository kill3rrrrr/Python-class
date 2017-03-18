s = input('enter the equation in the form of y = mx + c  ')
b = s.split('+')
print('c = {}'.format(b[1]))
c = b[0].split('=')
z=c[1].replace('x', ' ')

print('m = {}'.format(z))

