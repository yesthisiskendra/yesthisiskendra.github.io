def computepay(h, r):
    hours = int(h)
    rate = int(r)
    overtimeearnings = 0
    overtimehours = 0
    if hours > 40:
        overtimehours = hours - 40
        overtimerate = rate * 1.5
        overtimeearnings = overtimerate * overtimehours

    print('EARNINGS: ', (float(hours-overtimehours)*float(rate)) + overtimeearnings)


hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
computepay(hours, rate)
