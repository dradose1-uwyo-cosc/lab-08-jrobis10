# Jayden Robison
# UWYO COSC 1010
# November 5, 2024
# Lab 08
# Lab Section: 10
# Sources, people worked with, help given to: Fisher Brown
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

num = input('enter integer or a float')
def convertToNumber(num):
    isNeg = False
    if num[0] == "-":
        isNeg = True
        num = num.replace("-"," ")
    if "." in num:
        nums = num.split(".")
        if len(nums) == 2 and nums[0].isdigit() and nums[1].isdigit():
            if isNeg: 
                return -1*float(num)
            else: 
                return float(num)
    elif num.isdigit():
        if isNeg:
            return -1*int(num)
        else: 
            return int(num)
    else: 
        return False


print(convertToNumber(num))



print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m,b,xl,xu):
     y_values = []
for x in range(xl,xu+1):
        y = m*x + b
        y_values.append(y)
        return y_values





while True: 
    m = input('enter slope "m"')
    
    m = convert(m)
    
    
    b = input('enter intercept "b": ')
    
    b = convert(b)
    
    
    xl = input('enter lower bound "xl": ')
    
    xl = convert(xl)
    
    
    xu = input('enter upper bound "xu": ')
    
    xu = convert(xu)


   





print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
