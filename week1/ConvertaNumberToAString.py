"""
Description
We need a function that can transform a 
string into a number. What ways of achieving 
this do you know?

Note: Don't worry, all inputs will be 
strings, and every string is a perfectly 
valid representation of an integral number.

Examples
"1234" --> 1234
"605"  --> 605
"1405" --> 1405
"-7" --> -7
"""

def string_to_number(s):
    return int(s)

# another clever solution
def string_to_number(s):
    # Checking if it's float type
    if "." in s:
        s = float(s)
        return s
    
    # Checking if it's complex type
    elif "j" in s:
        s = complex(s)
        return s
    
    # In python we have 3 number data types, so if the last 2 cheking is false
    # the number must be int data type
    else:
        s = int(s)
        return s

    # Not necessary
    return 0