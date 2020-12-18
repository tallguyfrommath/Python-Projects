name = input('Enter your name: ')
msg = 'Welcome {}!'
print(msg.format(name), 'to the number guessing game')
import random
number = random.randint(1,50)
while True:

    try:
        guess = int(input('{}! enter your guess: '.format(name)))
        count = 0
        while guess != number:

            if guess < number:
                if guess == -1:
                    print('Welcome to cheat mode {}!, The number is'.format(name))
                    print(number)
                    print('We will not add this to your count :)')

                else:
                    print('Your guess was wrong! ')
                    count += 1
                    left = 4 - count
                    print('{} your guess is lower than the number'.format(name))
                    print('{} you have {} chance left'.format(name,left))
                    if number - guess <= 2:
                        print('you are close!')



            elif guess > number:
                print('Your guess was wrong! ')
                count += 1
                left = 4 - count
                print('{} your guess is greater than the number'.format(name))
                print('{} you have {} chance left'.format(name, left))
                if guess - number <= 3:
                    print('you are close!')
            if count == 4:
                break
            else:
                guess = int(input('{}! re-enter your guess: '.format(name)))

        if guess == number:
            print('Congratulations {}!, your guess was correct'.format(name))
            print('you took {} attempts'.format(count+1))
            break
        elif count == 4:
            print('sorry {}!, you lose!'.format(name))
            print('you took {} number of attempts to guess {}'.format(count,number))
            ask2 = input('Do you want to play again? Y/N ')
            if ask2 in ['y', 'yes', 'Yes', 'Y']:
                continue
            else:
                print('Goodbye {}'.format(name))
                break

    except:
        print('{}! you must enter only integers'.format(name))
        print('{}! we will restart the game'.format(name))
        ask = input('continue ? Y/N ')
        if ask in ['y','yes','Yes','Y']:
            number =  random.randint(1,50)
            continue
        else:
            break