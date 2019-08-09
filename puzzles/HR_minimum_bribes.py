# def minimumBribes(q):
#     total = 0
#     for i, num in enumerate(q):
#         if num > i+1:
#             total = total + (num - (i+1))
#         # print('i:', i, 'num:', num)
#     print(total)
#     # print(q)


def minimumBribes_almost(q):
    total = 0
    for i, num in enumerate(q):
        if i < len(q) - 1 and num - (q[i+1]) > 3:
            print('Too chaotic')
            return
        elif num > i+1:
            total = total + (num - (i+1))
    print(total)


def minimumBribes(q):
    for i, num in enumerate(q):
        # Need Tom's brain to talk through this part with me
        # How many spaces can someone be bribed if their partners also bribe?
        if i < len(q) - 1 and num - (q[i+1]) >= len(q)/2:
            # if i < len(q) - 1 and num - (q[i+1]) >= 3:
            print('Too chaotic')
            return
        else:
            continue
    print(recursiveSort(q))


timesSorted = 0


def recursiveSort(q):
    global timesSorted
    for i in range(len(q)-1):
        if q[i] > q[i+1]:
            q[i], q[i+1] = q[i+1], q[i]
            timesSorted = timesSorted + 1
            recursiveSort(q)
    return(timesSorted)
    # print(q, timesSorted)
    # timesSorted = 0


test1 = [2, 1, 5, 3, 4]
test2 = [1, 2, 5, 3, 4, 7, 8, 6]
test3 = [1, 2, 5, 3, 7, 8, 6, 4]
test4 = [5, 1, 2, 3, 7, 8, 6, 4]
test5 = [2, 5, 1, 3, 4]

# recursiveSort(test1)
# recursiveSort(test2)
# recursiveSort(test3)
# recursiveSort(test4)
# recursiveSort(test5)

# minimumBribes(test1)
# minimumBribes(test2)
minimumBribes(test3)  # should be 7
# minimumBribes(test4)  # should be "too chaotic"
# minimumBribes(test5) # should be "too chaotic"
