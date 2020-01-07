''' Pure functions
    A function is called pure function if it always returns the same result f
    or same argument values and it has no side effects like modifying an argument (or global variable) or outputting something.
     strlen(), pow(), sqrt()
'''

def multiply_2_pure(numbers):
    new_numbers = []
    for n in numbers:
        new_numbers.append(n * 2)
    return new_numbers

original_numbers = [1, 3, 5, 10]
changed_numbers = multiply_2_pure(original_numbers)
print(original_numbers) # [1, 3, 5, 10]
print(changed_numbers) #[2, 6, 10, 20]

