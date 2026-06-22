# Input a number and print: 
# Even/Odd
# Positive/Negative
def main():
    num = get_number()
    print("Even", end="|") if num % 2 == 0 else print("Odd", end="|" )
    print("Positive") if num > 0 else print("Negative") 

def get_number():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Invalid Value")

main() 