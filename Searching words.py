a=0
while a != 1:
    n = input("Please enter the name of your file with extension: ")
    try:
        file = open(n,"r",encoding='utf-8')
        break
    except:
        print("File not found, please enter a valid name")
l =file.readlines()
import re
b=[]
for item in l:
    if item.startswith('a'):
        b.append(re.findall("a{1,1}[^aeiouy]*e{1,1}[^aeiouy]*i{1,1}[^aeiouy]*o{1,1}[^aeiouy]*u{1,1}[^aeiouy]*", item))
    elif item.startswith('e') or item.startswith('i') or item.startswith('o') or item.startswith('u'):
        continue
    else:
        b.append(re.findall("[^aeiouy]*a{1,1}[^aeiouy]*e{1,1}[^aeiouy]*i{1,1}[^aeiouy]*o{1,1}[^aeiouy]*u{1,1}[^aeiouy]*", item))
for item in b:
    if item == []:
        continue
    else:
        print(item,end=" ")
