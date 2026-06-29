from calculator import square
# separate functions, because, in one function, pytest stop checking where the error occurs
# So, separate functions ensure that pytest check each function,
#  and tells every type of error in one execution
def test_positive():
    assert square(2) == 4
    assert square(5) == 25

def test_negative():
    assert square(-2) == 4
    assert square(-5) == 25

def test_zero():
    assert square(0) == 0

# no main, no try-excepts, no prints 