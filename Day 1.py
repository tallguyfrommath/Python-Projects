# To create a list of desired length and by element give index and by index give element and remove it
y = []
a = int(input("enter the size of array: "))
c = 0
q=0
while c <a:
    y.append(int(input("enter the value you want to enter ")))
    c+=1
print(f"your list of numbers is {y}")
b = int(input("enter the value for which you want to know the index for "))
if b in y:
    for x in y:
        if x == b:
            break
        q+=1
print(f"the element {b} is at index {q}")
ask =int(input("enter the value you want to remove from list: "))
if ask in y:
    y.remove(ask)
print(y)