while True:
    try:
        num = int(input("Enter a num? "))
        break
    except ValueError:
        print("Invalid Input")
for i in range(0, 10):
    print(f"{num} x {i+1} = {5*(i+1)}")