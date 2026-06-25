import sys

# check for errors
if len(sys.argv) < 2:
    sys.exit("Too less arguments")
# command line arguments
for arg in sys.argv[1:]: # slicing by removing the first name (names.py)
    print("My name is", arg)