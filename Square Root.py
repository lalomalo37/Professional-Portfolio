def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        # The raise statement raises an error when a condition is satisfied.
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2
            # The abs function returns a the absolute (non-negative) value of a number 
            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            elif square_mid < square_target:
                low = mid
            else:
                high = mid
        # The "is" keyword determines whether two variables refer to the exact same object in memory. 
        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root
# Another example of the "is" keyword:
# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# list3 = list1

# print(list1 is list2)  Output: False (different objects in memory, even if values are equal)
# print(list1 == list2)  Output: True (values are equal)
# print(list1 is list3)  Output: True (list3 refers to the same object as list1)

N = 1024
square_root_bisection(N)