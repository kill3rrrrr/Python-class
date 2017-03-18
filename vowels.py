s = input('enter a string: ')

#count the number of vowels
print("No. of a in the string: %s" % s.count('a'))
print('No. of e is the string: %s' % s.count('e'))
print("No. of i in the string: %s" % s.count('i'))
print('No. of o is the string: %s' % s.count('o'))
print("No. of u in the string: %s" % s.count('u'))

# calculate Percentage oof vowels
total_vowels = s.count('a') + s.count('e') + s.count('i') + s.count('u') + s.count('o')
percentage = (float(total_vowels) / len(s)) * 100
print('percentage of vowels in the string is: %s' % percentage)