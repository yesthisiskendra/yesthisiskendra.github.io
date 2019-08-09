# WORKS ON FIRST TWO TEST CASES
# def repeatedString(s, n):
#     if len(s) == 1:
#         return n
#     else:
#         string = s * n
#         string = string[:n]
#         return string.count('a')


def repeatedStrings(s, n):
    # print(len(s) % n)
    # print(type(len(s)/n), n/len(s), n % len(s))
    step1 = s.count('a')
    step2 = step1 * (int(n/len(s)))
    remainderString = s[:(n % len(s))]
    # step3 = int(step2) + remainderString.count('a')
    step3 = step2 + remainderString.count('a')
    print(step3)

    # if (len(s)/n)


def getFirstN(string, n):
    string = string * n
    string = string[:n]
    return string.count('a')
    print(string[:n])


def countA(string):
    print(string.count('a'))


test1 = 'a' * 10000
# test2 = 'abcabcabcabcabc'
test2 = 'aba'
test3 = 'cfimaakj'
# countA('abcabcabcabcabc')
# getFirstN('abcabcabcabcabc', 10)
repeatedStrings(test1, 10000)
repeatedStrings(test2, 10)
repeatedStrings(test3, 554045874191)
