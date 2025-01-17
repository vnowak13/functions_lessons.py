# def check_3_digits(number):
#     return number in range(100, 1000)

# result = check_3_digits(68)
# print(result)

# def check_3_digits(list1):
#     for n in list1:
#         if n in range(100, 1000):
#             return True
#         else:
#             return False
# result = check_3_digits([555, 99, 600])
# print(result)

# def check_3_digits(list1):

#     three_digits_list = []

#     for n in list1:
#         if n in range(100, 1000):
#             three_digits_list.append(n)
#         else:
#             pass

#     return False

# result = check_3_digits([555, 99, 600])
# print(result)

# coffee_prices = [('cappuccino', 1.5),
#                  ('espresso', 1.2),
#                  ('mocha', 1.9)]

# def most_expensive_coffee(list_of_prices):

#     highest_price = 0
#     my_most_expensive_coffee = ''

#     for coffee, price in list_of_prices:
#         if price > highest_price:
#             highest_price = price
#             my_most_expensive_coffee = coffee
#         else:
#             pass
#     return(my_most_expensive_coffee, highest_price)
# print(most_expensive_coffee(coffee_prices))

# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

def all_positives(list_of_positives):  # defines the list 
      #list has nothig in it now but leaves it open for numbers to be added later
    for n in list_of_positives:  #number in list
        if n < 0:  #determines in n is less than 0
            return False # if there is a negative it returns a false
    return True #positive returns true

list_of_positivies = [10, 5, 7, -3, 8]  #list of random numbers
# Don't call the function, you just need to define it.
result = all_positives(list_of_positivies) #give a value to make it shorter when writing the print
print(result) #prints the function


# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.
def sum_less(numbers): #defining the number
    total = 0  #starts off with zero
    for num in numbers:
        if 0 < num < 1000:  # Check if the number is between 0 and 1000
            total += num   #adds them together
    return total

# Test list of numbers
numbers = [15, -10, 500, 1000] #new list

# Calling the function with the numbers list
result = sum_less(numbers) #puts all the info in the value "result"
print(result) #prints the result



# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.
def count_even(numbers): #defines the list
    count = 0  #starting count off with zero
    for num in numbers: #number in list
        if num % 2 == 0:  # Check if the number is even
    return count

# Test list of numbers
numbers = [15, 7, 20, 25, 3, 1000] #list of random numbers/ new list

# Calling the function with the numbers list
result = count_even(numbers) #puts all the info in the value result"
print(result) #prints the result/function