import sys
from mymodule import hello
from mymodule import goodbye

if len(sys.argv) < 2:
    sys.exit()

hello(sys.argv[1])
goodbye(sys.argv[1])

