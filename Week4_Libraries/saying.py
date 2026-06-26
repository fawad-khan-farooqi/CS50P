import sys
# from mymodule import hello
# from mymodule import goodbye
import mymodule

if len(sys.argv) < 2:
    sys.exit()

mymodule.hello(sys.argv[1])
mymodule.goodbye(sys.argv[1])

