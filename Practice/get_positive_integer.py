#Program 5: get a positive number by using try, except, raise 
# Handle: abc and negative numbers gracefully.


while True:
    try:
        num = int(input("Enter a number? "))
        if num < 0:
            raise ValueError
        break
    except ValueError:
        print("It's not a positive number")

print(num)