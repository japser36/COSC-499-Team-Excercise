print('Hello world!')

# is_larger(n1, n2) -> int; returns -1 if n1 smaller, 1 if n1 bigger, and 0 otherwise (if equal).
def is_larger( n1, n2 ):
	"""is_larger( n1: int, n2: int ) -> int; This function compares the two numbers passed, and returns -1 if the first number is smaller, 1 if the first number is larger, and 0 if the numbers are equal."""
	if n1 < n2:
		return -1
	elif n1 > n2:
		return 1
	else:
		return 0

# test_is_larger() -> bool; tests is_larger() with several tests, and returns true iff all tests pass. Prints results along the way.
def test_is_larger():
	"""test_is_larger() -> bool; This function tests the is_larger() function, and returns true if all tests pass, false otherwise. Prints results too."""
	print('Testing is_larger()')
	tests_passed = True if (is_larger(10, 30) == -1 and is_larger(20, -2) == 1 and is_larger(4, 4) == 0 and is_larger(-20, 1) == -1) else False
	print('Did all tests pass? ' + ('Yes!' if tests_passed else 'No!'))
	return tests_passed

# Run the test for is_larger()
test_is_larger()
