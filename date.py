dob = input('enter your date of birth YYYY-MM-DD')
pre = input('enter present date')
a=dob.split('-')
print(a)
b=float(a[0])+(float(a[1])/12)+(float(a[2])/365)
c=pre.split('-')
d=float(c[0])+(float(c[1])/12)+(float(c[2])/365)
e=d-b
f=(e-int(e))*12
print("{:.0f} years {:.0f}months ".format(e, f))