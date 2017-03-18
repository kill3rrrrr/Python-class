fname = input("enter your first name: ")
lname = input("enter your last name: ")

print('hello %s %s!' % (fname, lname))

print("hello {} {}".format(fname, lname))
print("hello {0} {1}".format(fname, lname))

print("hello {1} {0}".format(fname, lname))
print("hello {0} {0} {1}".format(fname, lname))