# Student Grade Calculator
def main():
    marks = get_marks()
    grade = get_grade(marks)
    print(f"Grade: {grade}")
def get_marks():
    while True:
        try:
            marks = int(input("Enter marks? "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be within 0 to 100")
                continue
        except ValueError:
            print("Invalid Input!")
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "Fail"


if __name__ == "__main__":
    main()

