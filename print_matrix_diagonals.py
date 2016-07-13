matrix1 = [[9,3,4,2], [8,6,1,2], [5,5,6,7], [1,2,8,4]] 
 
# JS implementation: 
 for (var col = 0; col < n; col++) {
    for (var row = 0; row <= col; row++)
      print matrix[row][col - row];
    print "\n";
  }



# Python implementation: 
# def print_diagonals(matrix):
#     n = len(matrix[0])
#     print "n", n
#     col = 0
#     print "col", col
#     row = 0
#     print "row", row
#     for col in range(n-1):
#         print "COL", col
#         while row < col:
#             for row in range(n -1):
#                 print "ROW", row
#                 print matrix[row][col - row]

# print_diagonals(matrix1)


