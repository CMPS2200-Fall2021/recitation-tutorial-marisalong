def sum_of_squares(a):
	sum = 0
	for i in a:
		sum += i*i
	return sum

def test_one():
    assert sum_of_squares([1,2,3]) == 14

def test_two():
	assert sum_of_squares([3,4,5]) == 50

test_one()
