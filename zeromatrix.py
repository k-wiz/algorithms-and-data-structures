"""Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

A matrix without zeroes doesn't change:

    >>> zero_matrix([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

But if there's a zero, zero both that row and column:

    >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

Make sure it works with non-square matrices:

    >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]
"""

def zero_matrix3(matrix):

    nrows = len(matrix)
    ncols = len(matrix[0])

    rows = [False] * nrows
    cols = [False] * ncols

    #track the row and column of a 0. 
    for y in range(nrows):
        for x in range(ncols):
            if matrix[y][x] == 0:
                rows[y] = True
                cols[x] = True

    #zero out row, column
    for y in range(nrows):
        for x in range(ncols):
            if rows[y] == True:
                matrix[y][x] = 0
            if cols[x] == True:
                matrix[y][x] = 0


    return matrix


def zero_matrix2(matrix):

    nrows = len(matrix)
    ncols = len(matrix[0])

    # Keep track of indeces of rows and columns to clear.
    clear_rows = []
    clear_cols = []

    # Find rows & cols with 0. 
    for x in range(nrows):
        for y in range(ncols):
            if matrix[x][y] == 0:
                clear_rows.append(x)
                clear_cols.append(y)

    # Zero out rows & cols with 0.
    for x in range(nrows):
        for y in range(ncols):
            if x in clear_rows or y in clear_cols:
                matrix[x][y] = 0

    return matrix

print zero_matrix2([[0,1,2], [3,4,5], [6,7,8]])






def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""

    if matrix == []:
        return []

    nrows = len(matrix)
    ncols = len(matrix[0])

    clear_rows = [False] * nrows
    clear_cols = [False] * ncols

    #Pass 1: Figure out which rows and cols have 0's.
    for y in range(nrows):
        for x in range(ncols):
            if matrix[y][x] == 0:
                clear_rows[y] = True
                clear_cols[x] = True



    #Pass 2: Clear those rows and cols. 
    for y in range(nrows):
        for x in range(ncols):
            if clear_rows[y] or clear_cols[x]:
                matrix[y][x] = 0


    return matrix 








    # Get index of the zero, make all other nums with that index 0. 

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** TESTS PASSED! YOU'RE DOING GREAT!\n"
