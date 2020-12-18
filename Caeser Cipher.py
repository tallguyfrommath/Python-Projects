q= list(range(1,27))
Q=list(range(1,27))
l=["a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
L=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
s = None
while s != 'stop':
    print("\t\t\t\t\tMENU\t\t\t\t\t\t")
    y = input("\t\t\twhat do you want to do?\n\t\ta. encrypt \t\t\tb. decrypt\nEnter your choice:")
    if y=='a':
        k = int(input("enter your encryption key value: "))
        m= input("Type the message you want to encrypt: ").split()
        a=[]
        b=[]
        me=''
        for i in m:
            for j in i:
                if j in l:
                    me =me+l[((ord(j)%26-19)+k)%26]
                if j in L:
                    me =me+L[((ord(j)%26-13)+k)%26]
            me+='  '
        print('Your encrypted message is: ',me)
    if y=='b':
        k = int(input("enter your decryption key value: "))
        m= input("Type the message you want to encrypt: ").split()
        a=[]
        b=[]
        me=''
        for i in m:
            for j in i:
                if j in l:
                    me =me+l[((ord(j)%26-19)-k)%26]
                if j in L:
                    me =me+L[((ord(j)%26-13)-k)%26]
            me+='  '
        print('Your encrypted message is: ',me)
    s = input("\t\t\twhat do you want to do?\n\t\ta. encrypt \t\t\tb. decrypt\t\t\tstop\nEnter your choice:").lower()