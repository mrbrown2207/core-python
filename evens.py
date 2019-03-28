def is_even(num):
    return num % 2 == 0

def even_number_of_evens(nums):
    even_count = 0
    ret_val = False
    if len(nums) > 0:
        for num in nums:
            if is_even(num):
                even_count += 1

        if even_count > 0:
            ret_val = is_even(even_count)

    return ret_val;
    
# This does the same thing as the function above
def even_number_of_evens_II(nums):
    even_count = sum([1 for num in nums if is_even(num)])
    return False if even_count == 0 else is_even(even_count)
    
assert even_number_of_evens_II([]) == False, "No numbers"
assert even_number_of_evens_II([2]) == False, "One even number"
assert even_number_of_evens_II([2, 4]) == True, "Two even numbers"
assert even_number_of_evens_II([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens_II([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens_II([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens_II([1, 3, 9]) == False, "No even numbers"

print("All tests passed")
