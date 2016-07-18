

def condense_ranges(str1):
    
    # Convert string of ranges to a list of ranges, extra spaces removed.
    ranges = [item.strip() for item in str1.split(",")]

    # Convert each range to a tuple of integers; append to list.
    int_ranges = []
    for rnge in ranges:
        split_ranges = rnge.split(":")
        num1, num2 = int(split_ranges[0]), int(split_ranges[1])
        int_ranges.append((num1, num2))

    # Find condensed ranges by keeping track of lowest and highest number
    # in consecutive range, adding to output. 
    output = ""
    low = None
    high = None

    for rnge in sorted(int_ranges):
        # If first tuple, set low to first item of tuple, set high to second 
        # item of tuple.
        if low is None:
            low = rnge[0]
            high = rnge[1]
        # If the next range is consecutive, overlapping, or a sub-range of 
        # the last, condense ranges. 
        elif rnge[0] <= high + 1 and rnge[1] > high:
            high = rnge[1]
        # Otherwise, append the range represented by low, high to output string; 
        # reset low, high to current range.  
        else:
            output = output + str(low) + ":" + str(high) + ","
            low = rnge[0]
            high = rnge[1]

    output = output + str(low) + ":" + str(high)

    return output



print condense_ranges("1:4, 5:10,11:20") 
print condense_ranges("1:4 , 5 : 10,11:20") 
print condense_ranges("1:5,20:30,30:40,40:50,50:60")
print condense_ranges("1:20, 1:7")











