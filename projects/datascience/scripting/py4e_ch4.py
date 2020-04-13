# Python for Everybody
# Chapter 4. Functions
# Exercise 7


def computegrade(score):
    try:
        if score > 1:
            return('Bad score')
        if score >= .90:
            return('A')
        elif score >= .80:
            return('B')
        elif score >= .70:
            return('C')
        elif score >= .60:
            return('D')
        elif score < .6:
            return('F')
    except:
        return('Bad score')


# TESTING
print(computegrade(.95))
print(computegrade('perfect'))
print(computegrade(10))
print(computegrade(.75))
print(computegrade(.5))
