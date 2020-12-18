name = input('Enter your name: ')
msg = 'Welcome {}!'
print(msg.format(name), 'to the prime number calculator')
while True:
    try:
        num = input('Please enter a number upto which you want to check: ')
        if int(num) == 1:
            print('1 is not prime')
            ask = input('do you want to chwck for another number? YES/NO')
            if ask not in ['Y', 'yes', 'y', 'YES']:
                break
        elif int(num) == 2:
            print('2 is prime')
            ask = input('do you want to chwck for another number? YES/NO')
            if ask not in ['Y', 'yes', 'y', 'YES']:
                break
        elif int(num) > 2:
            y = list()
            k = list()
            for n in range(2,int(num)):
                k.append(n)
                if int(num) % n != 0:
                    y.append(n)
            if k == y:
                print(num,"is prime!")
                ask = input('do you want to chwck for another number? YES/NO')
                if ask not in ['Y', 'yes', 'y', 'YES']:
                    break
            else:
                print(num, 'is not prime!')
                ask = input('do you want to chwck for another number? YES/NO: ')
                if ask not in ['Y', 'yes', 'y', 'YES']:
                    break
        elif int(num) <= 0:
            print(num,'is not prime')
            ask = input('do you want to chwck for another number? YES/NO')
            if ask not in ['Y','yes','y','YES']:
                break
    except:
        print('Please enter an integer only')
