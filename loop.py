# Create a list of numbers upto 10
square=[x**2 for x in range(10)]
print('square', square)

# you can create list using existing list
numbers = [1,2,3,4,5,6,7,8,9,10]
even_number=[x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x %2 !=0]
print('numbers', numbers)
print(even_number)
print(odd_numbers)