"""Write a function that, given a string, finds the longest run of identical 
characters and returns an array containing the start and end indices of that 
run. If there are two runs of equal length, return the first one. 
Return [0,0] for no runs."""

def longest_run(string):

    char = None
    current_run = 0
    longest_run = 0
    starting_index = 0


    for i in range(len(string)):
        if char is None:
            char = string[i]
            current_run += 1
            longest_run = current_run
        elif string[i] == char:
            current_run += 1
        else:
            if current_run == longest_run:
                starting_index = i
            elif current_run > longest_run:
                longest_run = current_run
                starting_index = i - longest_run
            current_run = 1
            char = string[i]

    if current_run > longest_run:
        longest_run = current_run
        starting_index = len(string) - longest_run

    if longest_run == 0:
        return [0,0]
    else:
        return [starting_index, starting_index + longest_run -1]


print longest_run('sdfffffiii')
print longest_run("")
print longest_run("kelleeeee")
print longest_run('hhhhhh')