sum_odd_squared = sum([n ** 2 for n in range(1, 2000, 2)])  # Your list comprehension inside the sum here
print(sum_odd_squared)
# The exercise says to get the sum of the first 1000 odd numbers squared
# The first 1000 odd numbers are in range from 1 to 2000 so the answer is 1333333000
# The result you got (166666500) is the sum of the first 500 odd numbers (from 1 to 1000)
# If I change the number 2000 in the range to 1000 I will get the same answer as yours
