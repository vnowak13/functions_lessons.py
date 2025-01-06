# functions are ways to wrap your code into reuseble units
# place () after the function name to invoke it

# def happy_birthday(name, age): # this is how you define the function # name is the parameter, place holder for future information
#     #position of the parameter does matter
#     print(f"Happy Birthday to {name}!")
#     print(f"You are {age} years old!")
#     print("Hapy Birthday to you!")

# happy_birthday("Sis", 20) # this is how you call/invoke the function # sis is the arguement, what goes inside the value
# happy_birthday("Angela", 30)
# happy_birthday("Victoria", 40) 

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("BroCode", 42.50, "01/01")

#return = statment used to end a function and send a result back to the caller

# def add(x, y):
#     z = x + y
#     return z

# def subtract(x , y):
#     z = x - y
#     return z

# def multiply(x , y):
#     z = x * y
#     return 

# def divide(x, y):
#     z = x / y
#     return z

# print(add(1, 2))
# print(subtract(1, 2))
# print(multiply(1, 2))
# print(divide(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("bro", "code")