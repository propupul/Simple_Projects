import random
import time

KEEP_GOING = 'y'
while KEEP_GOING == 'y':
    number_sides = 0
    times_roll = 0
    while number_sides == 0 or times_roll == 0:
        try:

            number_sides = int(input("How many sides should the die have? "))
            times_roll = int(input("How many times do you want to roll? "))

        except:
            print('Not a number')

    numbers_rolled = []

    for numbers in range(1, number_sides+1):
        a_list = []
        a_list.append(numbers)
    print('Die has',a_list, 'sides')

    input('Press ENTER to roll..')

    for times in range(times_roll):

        for numbers in a_list:
            number_rolled = random.randint(1, numbers)
            numbers_rolled.append(number_rolled)

    ROLL_DICT = {}
    for numbers in numbers_rolled:
        how_many_times = numbers_rolled.count(numbers)
        ROLL_DICT[numbers] = how_many_times



    for key in ROLL_DICT:
        percent1 = float(ROLL_DICT.get(key)/len(numbers_rolled))
        percent2 = float(ROLL_DICT.get(key)/len(numbers_rolled))
        time.sleep(.3)
        print('Rolling')
        if ROLL_DICT.get(key) == 1:
            percent1 = str(percent1)
            percent2 = str(percent2)
            print(key, 'was rolled', ROLL_DICT.get(key), 'time', 'That is %s' % percent1 +'%')
        else:
            print(key, 'was rolled', ROLL_DICT.get(key), 'times', 'That is %s' % percent2 +'%')

    KEEP_GOING = input('Would you like to keep going [y/n]: ')