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

# stringSort(arr) -> void; sorts a string list in ascending order of length
def string_sort(arr):
    """stringSort(arr) -> void; This function sorts a string list in ascending order of length."""
    for i in range(len(arr)-1):
        for j in range(i, len(arr)):
            if is_larger(len(arr[i]), len(arr[j])) > 0:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

# test_is_larger() -> bool; tests is_larger() with several tests, and returns true iff all tests pass. Prints results along the way.
def test_is_larger():
	"""test_is_larger() -> bool; This function tests the is_larger() function, and returns true if all tests pass, false otherwise. Prints results too."""
	print('Testing is_larger()')
	tests_passed = True if (is_larger(10, 30) == -1 and is_larger(20, -2) == 1 and is_larger(4, 4) == 0 and is_larger(-20, 1) == -1) else False
	print('Did all tests pass? ' + ('Yes!' if tests_passed else 'No!'))
	return tests_passed

# test_string_sort() -> bool; tests string_sort() with a single test. Returns true if the test passes.
def test_string_sort():
    """test_string_sort() -> bool; This function tests the string_sort() function, and returns true if the test passes."""
    print('Testing string_sort()')
    arr = ['shamus', 'dan', 'jasper36', 'maya']
    string_sort(arr)
    test_passed = True if (arr == ['dan', 'maya', 'shamus', 'jasper36']) else False
    print('string_sort test passed' if test_passed else 'string_sort test did not pass')

# Run the test for is_larger()
test_is_larger()

# Run the test for string_sort()
test_string_sort()

# int_sort_desc(arr) -> int; sorts an int array in descending order 
def int_sort_desc(arr):
    """int_sort_desc(arr) -> int; This function takes an array of integers as an argument and sorts them in descending order."""
    arr.sort(reverse = True)

# test_sort_desc() -> void; Uses sample array and to check int_sort_desc(arr) -> int sorts the array in descending order 
def test_sort_desc():
    """test_sort_desc() -> void; Uses sample array and calls int_sort_desc(arr) -> int sorts the array in descending order"""
    arro = [5,7,9,2,4]
    int_sort_desc(arro)
    print(arro)

# Run test for int_sort_desc(arr)
test_sort_desc()
