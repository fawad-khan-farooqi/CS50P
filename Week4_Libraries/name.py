# import sys
import sys

# Index Error can be handled with try and except statement like below
# try:
#    print("my name is", sys.argv[1])
# except IndexError:
#     print("Too less arguments")

# But we want to also handle the case, where the user gives more than one argument

# check for errors
if len(sys.argv) > 2:
    sys.exit("Too many arguments")
elif len(sys.argv) < 2:
    sys.exit("Too less arguments")

# print the result, if no errors
print("My name is", sys.argv[1]) # sys.argv[0] = file name

# Note: if we want to pass more than one word and want to store it in sys.argv[1], 
# then we have to enclosed it in the double quotes,

