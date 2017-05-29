import random

NUMBER_OF_ATTEMPTS = 10
RANGE_BOTTOM = 5
RANGE_TOP = 15
guessesLeft = NUMBER_OF_ATTEMPTS

while True:
    #generate the random number
    random_number = random.randint(RANGE_BOTTOM, RANGE_TOP)

    #give the user a certain amount of guesses
    for i in range (NUMBER_OF_ATTEMPTS):
        guess = int(raw_input('Guess the number between ' + str(RANGE_BOTTOM) + ' and ' + str(RANGE_TOP) + ": "))
        guessesLeft = (NUMBER_OF_ATTEMPTS - (i+1))
        if guess == random_number:
            print 'Well done!'
            break
        elif guess > random_number:
            print "Too high. You have " + str(guessesLeft) + " attempts left"
        else:
            print "Too low. You have " + str(guessesLeft) + " attempts left"

    print 'let\'s try a new number'