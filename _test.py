import pytest

def square(n):
    return n**2 

def cube(n):
    return n**3 

def fifth(n):
    return n**5 

def test_sqaure():
    assert square(2) == 4   , "Test failed: Square of 2 should be same to 4"
    assert square(3) == 9 , "Test failed; Square of 3 should be same to 9"
def test_cube():
    assert cube(2) == 8, "Test failed: Cube of 2 should be equal to 8"
    assert cube(3) == 27, "Test failed: Cube of 3 should be equal to 27"

def test_fifth():
    assert fifth(2) == 32, "Test failed: Fifth power of 2 should be equal to 32"
    assert fifth(3) == 243, "Test failed: Fifth power of 3 should be equal to 243"


def test_invalid_input():
        with pytest.raises(TypeError):
            square("invalid")
        with pytest.raises(TypeError):
            cube("invalid")
        with pytest.raises(TypeError):
            fifth("invalid")
 