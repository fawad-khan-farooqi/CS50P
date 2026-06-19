#  Debugger helps you to find the issues
#  Set breakpoint, from where you want to start debugging
#  Then start debugging
# Step into -> means that line by line
# Step over -> execute and display just result 
# (used when you are sure, that this line or function is ok)

def main():
    h = int(input("What's Height? "))
    pyramid(h)

def pyramid(n):
    for i in range(n):
        print("#"*(i+1))

if __name__ == "__main__":
    main()