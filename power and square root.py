base = int(input("Enter Base : "))
exponent = int(input("Enter Exponent : "))

val = pow(base, exponent)
val2 = base ** exponent

print("The ", exponent, " power of ", base, " is : ", val)
print(val2)

#Square root of any number

from math import sqrt

num1 = int(input("Enter the number : "))

sq_rt = sqrt(num1)

print("The square root of that number is ", sq_rt)
