def jumpingOnClouds_iter(c):
    cci = len(c) - 1
    jumps = 0
    while cci > 0:
        if c[cci - 1] == 1:
            jumps = jumps + 1
            cci = cci - 2
        elif c[cci - 1] == 0 and c[cci - 2] != 1:
            jumps = jumps + 1
            cci = cci - 2
        else:
            jumps = jumps + 1
            cci = cci - 1
    return(jumps)


test1 = [0, 0, 1, 0, 0, 1, 0]  # should return 4
test2 = [0, 0, 0, 1, 0, 0]  # should return 3
test3 = [0, 0, 0, 0, 1, 0]  # should return 3

print(jumpingOnClouds_iter(test2))
