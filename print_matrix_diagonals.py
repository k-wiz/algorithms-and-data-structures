matrix = [[0,0,0,0], [1,1,1,1], [2,2,2,2], [3,3,3,3]] 
 
 for (var col = 0; col < n; col++) {
    for (var row = 0; row <= col; row++)
      print matrix[row][col - row];
    print "\n";
  }


  