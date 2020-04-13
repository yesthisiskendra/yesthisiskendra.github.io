jumps = 0


def jumpingOnClouds(c):
    if cci < 0:
        return(jumps)
    else:
        jumps = jumps + 1
        checkNeighbor(cci - 1)


def jumpingOnClouds_iter(c):
    cci = len(c) - 1
    jumps = 0
    for i in range(len(c)):
        if cci > 0:
            if c[cci - 1] == 1:
                jumps = jumps + 1
                cci = cci - 2
            elif c[cci - 1] == 0 and c[cci - 2] != 1:
                jumps = jumps + 1
                cci = cci - 2
            else:
                jumps = jumps + 1
                cci = cci - 1
        else:
            return(jumps)


test1 = [0, 0, 1, 0, 0, 1, 0]
test2 = [0, 0, 0, 1, 0, 0]

print(jumpingOnClouds(test1))
print(jumpingOnClouds(test2))
