EXPECTED = 6

def test_multiply():
    result = multiply(2, 3)
    if result != EXPECTED:
        raise AssertionError(f"Expected {EXPECTED}, got {result}")

