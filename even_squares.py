import math

def even_squares(a, b):
    """Returns the number of even squares (nums that have even sqaure roots)
    between a and b, inclusive."""

    count = 0

    for i in range(a, b+1):
        if math.sqrt(i).is_integer():
            count += 1

    return count

print even_squares(1, 5)
print even_squares(9, 25)