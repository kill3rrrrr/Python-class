names = ['John Doe', 'Jane Doe', 'Jonny Tuck']
#Change the first name in the list
names[0]
print('name now: ', names)

# Append some moew names
names.append('Molly Mormon')
names.append('Joe Bloggs')
print('names finally: ', names)
print('Last name in the list: %s' % names[-1])

#you can join the list using str.join() method
joined_name= '/n'.join(names)
print('\nList of names:')
print(joined_name)