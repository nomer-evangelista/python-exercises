# 1. Identify the data type of the following values: 
print(type(99.9))
# float
print(type("False"))
# string
print(type(False))
# boolean
print(type('0'))
# string
print(type(0))
# integer
print(type(True))
# boolean
print(type('True'))
# string
print(type([{}]))
# list
print(type({'a': []}))
# dictionary

# 2. What data type would best represent the following?

# A term or phrase typed into a search box
# string

# Whether or not a user is logged in
# boolean

# A discount amount to apply to a user's shopping cart
# float

# Whether or not a coupon code is valid
# boolean

# An email address typed into a registration form
# string

# The price of a product
# float

# The email addresses collected from a registration form
# list

# Information about applicants to Codeup's data science program
# dictionary

# 3. For each of the following code blocks:
# Read the expression and predict the evaluated results
# Execute the expression in a Python REPL. 

print('1' + 2)
# 1 - is a string type and 2 - is an integer type. 

print(6 % 4)
# 2 -- remainder of 2

print(type(6 % 4))
# integer type 

type(type(6 % 4))
# type

'3 + 4 is ' + 3 + 4
# '3 + 4 is' - string type and 3 + 4 is an integer type

0 < 0
# False --> zero is not less than zero

'False' == False
# False --> False string type is not equal to False boolean type 

True == 'True'
# False --> True string type is not equal to True boolean type 

5 >= -5
# True --> five is not greater than or equal to -5

True or "42" 
# True --> True and string type are True 

6 % 5
# 1 --> remainder of 1

5 < 4 and 1 == 1
# False --> 5 is not less than 4 but 1 is equal to 1

'codeup' == 'codeup' and 'codeup' == 'Codeup'
# False --> string type codeup is equal to codeup 
# but codeup is not equal to Codeup

4 >= 0 and 1 !== '1'
# invalid systax where !== not an expression

6 % 3 == 0
# True --> 6 % 3 have a 0 remainder is equal to zero

5 % 2 != 0
# True --> 5 % 2 have a remainder of 1 is not equal zero

[1] + 2
# error --> [1] is list and 2 is an integer cannot concatenate

[1] + [2]
# [1, 2]

[1] * 2
# [1, 1]

[1] * [2]
# error can't multiply non-integer of list type

[] + [] == []
# True --> empty list bracket + empty list bracket equals empty list bracket

{} + {}
# error --> unsupported operation, cannot add two dictionary

# 4. You have rented some movies for your kids:
# The Little Mermaid for 3 days
# Brother Bear for 5 days
# Hercules for 1 day
# If the daily fee to rent a movie is 3 dollars, 
# how much will you have to pay?

movie_rent = 3
little_mermaid = 3 * movie_rent
brother_bear = 5 * movie_rent
hercules = 1 * movie_rent

print('The cost for renting The Little Mermaid is : $', little_mermaid) 
print('The cost for renting Brother Bear is : $', brother_bear)
print('The cost for renting Hercules is : $', hercules)

# 5. Suppose you're working as a contractor for 3 companies: 
# Google, Amazon and Facebook.
# They pay you the following hourly rates:
# Google: 400 dollars
# Amazon: 380 dollars
# Facebook: 350 dollars
# This week you worked: 10 hours for Facebook, 6 hours for Google, and 4 hours for Amazon.
# How much will you receive in payment for this week?

google = 400
amazon = 380
facebook = 350
pay_hours = (google * 6) + (amazon * 4) + (facebook * 10)

print('pay for work hours', pay_hours)

# 6. A student can be enrolled in a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.

class_not_full = True
class_schedule = True
schedule_no_conflict = class_not_full and class_schedule
print('class is not full and schedule does not conclict: ') 
print(schedule_no_conflict)

# 7. A product offer can be applied only if a customer 
# buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

buys_2_items = True
offer_time = True
premium_member = True

product_available = buys_2_items and offer_time and premium_member
print(product_available)

# 8.  Use the following code to follow the instructions below:
# username = 'codeup'
# password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the 
# following conditions:
# The password must be at least 5 characters
# The username must be no more than 20 characters
# The password must not be the same as the username
# Bonus Neither the username or password can start nor end with whitespace
username = 'codeup'
password = 'notastrongpassword'

password_length = len(password) <= 5
print('password length is: ', password_length)

username_length = len(username) <= 20
print('username length is: ', username_length)

password.strip()
print('password is: ', password)
username.strip()
print('username is: ', username)

username_password = password_length != username_length 
print('username is not the same with password: ', username_password)












































































