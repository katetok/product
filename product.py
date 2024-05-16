import doctest

def product(a, b):
    """Return product of a and b.

        >>> product(2, 2)
        4

        >>> product(2, -2)
        -4
    """
    return a * b

#print(product(3, -3))

doctest.testmod()

    
'''# Call doctest to execute tests
try:
    doctest.testmod()
    print("All tests passed!")
except Exception as e:
    print("Some tests failed:", e)'''