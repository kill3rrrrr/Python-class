a1 = input('enter the marks of 1 subject')
a2 = input('enter the marks of 2 subject')
a3 = input('enter the marks of 3 subject')
a4 = input('enter the marks of 4 subject')
a5 = input('enter the marks of 5 subject')
total = float(a1) + float(a2) + float(a3) + float(a4) + float(a5)
per = (total / 500) * 100
print('total = {}'.format(total))
print('percentage = {:.3f}%'.format(per))