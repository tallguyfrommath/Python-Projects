a= input("enter your name player 1: ")
b= input("enter your name player 2: ")
t = input("enter the number of tries you want to play ")
aw,bw,counter = 0,0,0
while counter < int(t):
    print(f"starting the game, {a} will go first and then {b}")
    while True:
        ca = input(f"enter your choice {a}: ").lower()
        cb = input(f"enter your choice {b}: ").lower()
        if ca in ["stone","paper","scissors","rock"] and cb in ["stone","paper","scissors","rock"]:
            break
        else:
            print(r"Please choose any of 'stone','paper','scissors','rock','Stone','Paper','Scissors','Rock' ")
            continue
    if (ca in ["stone","rock"] and cb in ['scissors'])|(ca in ["scissors"] and cb in ["paper"])|(ca == "paper" and cb in ["stone","rock"]):
        counter +=1
        print(f"{a} wins !")
        aw +=1
        continue
    elif (cb in ["stone","rock"] and ca in ['scissors'])|(cb in ["scissors"] and ca in ["paper"])|(cb == "paper" and ca in ["stone","rock"]):
        counter +=1
        print(f"{b} wins !")
        bw+=1
        continue
    else:
        print("tie, not counted")
print(f"{a} won") if aw>bw else print(f"{b} won")