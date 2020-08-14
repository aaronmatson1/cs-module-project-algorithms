'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # I need to start with 1, because if you multiply by 0, you're just gonna get more 0's.
    result = 1

    for x in arr: # Start a for loop to loop through our array, and multiply each value with the result.
        result *= x # Once we multiply, we will have a new result. Keep multiplying until we run out of elements in the array
    return [result / x for x in arr] # our result will then be divided the number in our list
    # Using the first arr = [1, 2, 3, 4, 5] it will return a result of 120.
    # 120 will then be divided by each number in our list, giving us an output of [120, 60, 40, 30, 24]


if __name__ == '__main__':
    # Use the main function to test your implementation
     arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
