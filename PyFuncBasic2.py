# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, 
# from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]
def countDown(x):
    if x > 0 and x%1 == 0:
        newL = []
        for i in range(x,-1,-1):
            newL.append(i)
        return(newL)
    else:
        print("please enter a positive integer")
# test:
# print(countDown(6))

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
def PandR(list):
    if list.length == 2:
        print(list[0])
        return(list[1])
    else:
        print("Please enter a list with exactly two numbers")
# test:
# print(PandR([4,5]))

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def FplusL(list):
    return(list[0] + len(list))
# test:
# print(FplusL([3,2,6,4,9]))

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the
# original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has
# less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False
def GT2(list):
    if len(list) < 2:
        return(False)
    else:    
        l2 = []
        for e in list:
            if e > list[1]:
                l2.append(e)
        return(l2)
# test:
# print(GT2([1,3,5,1,0,9,2,3]))

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create 
# and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]
def SandV(x,y):
    if x > 0 and x%1 == 0:
        list = []
        while x > 0:
            list.append(y)
            x -= 1
        return(list)
    else:
        print("Please enter in a positive integer, a comma, and then any other number")
# test:
# print(SandV(4,8.3))