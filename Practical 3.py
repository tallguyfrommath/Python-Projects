# Practical 3
# Submitted by : Abhishek
# College: Hindu College(Section A)
# date: 07-01-2021

a = float(input("enter the coefficient of x^2 "))
b = float(input("enter the coefficient of x "))
c = float(input("enter the constant term "))
print(f"your quadratic equation is {a}x^2+{b}x+{c}")
import numpy as np
y = np.roots([a,b,c])
print("the roots of the quadratic equation are ","x=",str(y[0]).replace("j","i"),"and","x=",str(y[1]).replace("j","i"))