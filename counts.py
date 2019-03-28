def count_upper_case(msg):
    return sum([1 for c in msg if c.isupper()])

assert count_upper_case("")  == 0, "Empty string"
assert count_upper_case("A")  == 1, "One uppercase letter"
assert count_upper_case("a")  == 0, "One lowercase letter"
assert count_upper_case("£$%^&")  == 0, "Special characters"
assert count_upper_case("Foo man Foo") == 2, "3 words two have uppercase"
assert count_upper_case("ABCDEFCGA") == 9, "All uppercase"
assert count_upper_case("123456789") == 0, "All numeric"

print("All tests passed")


