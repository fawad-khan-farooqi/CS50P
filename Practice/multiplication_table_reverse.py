# Multiplication table in reverse
while True:
    try:
        num = int(input("Enter a num? "))
        break
    except ValueError:
        print("Invalid Input")
for i in range(10, 0, -1):
    print(f"{num} x {i} = {num*i}")