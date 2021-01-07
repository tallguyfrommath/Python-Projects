# Practical 4
# Submitted by : Abhishek
# College: Hindu College(Section A)
# date: 07-01-2021
y=None
y = input("enter the number you want to reverse and 'stop' to stop: ")
while y != "stop":
    print("The reversed number is",y[::-1])
    s=0
    for i in str(y):
        s += int(i)
    print(f"The sum of digits is {s}")
    y = input("enter the number you want to reverse and 'stop' to stop: ")

