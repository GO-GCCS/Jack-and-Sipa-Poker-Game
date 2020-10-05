some_random_global_variable = 50
# now i want to modify tbis in a function

# asimple sqrt function

def sqrt(number):
    """
    docstring
    """
    return number*number
#now to store the sqrt in a our global variable
some_random_global_variable = sqrt(some_random_global_variable)
print(some_random_global_variable)

