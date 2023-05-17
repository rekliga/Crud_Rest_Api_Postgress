from logica import problema1

def test_p1():
    assert len(problema1())==100
def test_p1_fizz():
    assert problema1()[2] == "fizz"
def test_p1_buzz():
    assert problema1()[4] == "buzz"
def test_p1_fizz_buzz():
    assert problema1()[14] == "fizz buzz"

