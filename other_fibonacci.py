# The fabonacci sequence displayed through a program

terms = int(input("Enter an amount of terms you'd like to display? "))

# enter the first two terms
number_1 = 0
number_2 = 1
count = 0

# is the terms valid
if terms <= 0:
   print("Please enter a positive integer")
elif terms == 1:
   print("Fibonacci sequence upto",terms,":")
   print(number_1)
else:
   print("Fibonacci sequence:")
   while count < terms:
       print(number_1)
       nth = number_1 + number_2
       # put in the updated information
       number_1 = number_2
       number_2 = nth
       count += 1
