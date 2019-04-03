def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, received {1}".format(expected, actual)

def test_not_equal(actual, expected):
    assert expected != actual, "Did not expect {0}, but received {1}".format(expected, actual)

def test_is_in(coll, item):
    assert item in coll, "{0} does not contain {1}".format(coll, item)

def test_not_in(coll, item):
    assert item not in coll, "{0} does contain {1}".format(coll, item)
    
def test_between(num, lo, hi):
    assert num in range(lo, hi), "{0} is not between {1} and {2}".format(num, lo, hi)
