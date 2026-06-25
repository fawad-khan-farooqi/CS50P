# python -m pip install cowsay
# means: 
# python → Run the Python interpreter.
# -m → Run a module as a script.
# pip → The module to run.
# install cowsay → Tell pip to install the cowsay package.
# So it is equivalent to:
# "Use this specific Python installation to run pip and install cowsay."

import cowsay
import sys
if len(sys.argv) == 2:
#     cowsay.cow("Hi, "+ sys.argv[1]) # as it will only takes one argument
    cowsay.trex("hi, " + sys.argv[1])

# Note: Don't use same filename as the imported packages