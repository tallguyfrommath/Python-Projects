# Practical 2
# Submitted by : Abhishek
# College: Hindu College(Section A)
# date: 07-01-2021
while True:
    d = 0
    print("\t\t\t\t\t\t\t\t\t\tMENU\t\t\t\t\t\n\t\t\ta) +\t\tb) -\t\tc) *\t\td) /\t\te)//\t\tf) %\n")
    c= input("Enter your choice: ").lower()
    n=int(input("Enter the first number: "))
    q=int(input("Enter the second number: "))
    print(f"The sum of numbers {n} and {q} is {n}+{q}= ",n+q) if c == "a" else d ==0
    print(f"The difference of numbers {n} and {q} is {n}-{q}= ",n-q) if c == "b" else d ==0
    print(f"The product of numbers {n} and {q} is {n}*{q}=" ,n*q) if c == "c" else d ==0
    print(f"The quotient of numbers {n} and {q} is {n}/{q}= ",n/q) if c == "d" else d ==0
    print(f"The floor division of numbers {n} and {q} is {n}//{q}= ",n//q) if c == "e" else d ==0
    print(f"The modulo of numbers {n} and {q} is {n}%{q}= ",n%q) if c == "f" else d ==0
    c =input("Do you want to re enter the numbers? (y/n)").lower()
    if c == "y":
        continue
    else:
        break
