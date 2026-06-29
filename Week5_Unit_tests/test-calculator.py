from calculator import square

def main():
    test_square()



#def test_square():
    # If we wanted to test many more conditions, our test code could easily become bloated.
    # if square(2) != 4:
    #     print("Square of 2 isn't 4")
    # elif square(3) != 9:
    #     print("square of 3 isn't 9")
# alternatively, we can test like;
def test_square():
    try:
        assert square(2) == 4 # assume confidently
    except AssertionError:
        print("square of 2 isn't 4") # i.e. assertion is proved wrong
    try:
        assert square(3) == 9 # assume confidently
    except AssertionError:
        print("square of 3 isn't 9") # i.e. assertion is proved wrong    

if __name__ == "__main__":
    main() 