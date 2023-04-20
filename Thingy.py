import numpy as np
from numpy import random as rnd
import matplotlib.pyplot as plt
import math as m
import os

while True: 

    #a
    print("a")
    inp = input()

    if inp == "t":
        a = 1
        sf = "cos"
        b = 1
        h = 0
        k = 0
        break
    else:
        a = int(inp)

    #determining type
    print("cos or sin")
    inp = input()
    if inp == "cos":
        sf = inp
        restart = False
    elif inp == "sin":
        sf = inp
        restart = False
    else:
        restart = True
        print("you will have to reenter everything")

    #b
    print("B")
    inp = input()
    b = int(inp)


    print("h")
    inp = input()
    h = int(inp)

    print("k")
    inp = input()
    k = int(inp)

    #restart if nescecary
    if restart == True:
        print("restart")
    else:
        break

x = 1

if sf == "cos":
    f = (a * m.cos(b * (x - h)) + k)
else:
    f = (a * m.sin(b * (x - h)) + k)

xpoints = np.array([float(0)])
ypoints = np.array([float(0)])


while x <= 100:
    if sf == "cos":
        f = (a * m.cos(b * (x - h)) + k)
    else:
        f = (a * m.sin(b * (x - h)) + k)

    print(f)
    if x == 100:
        q = open("Log_x.txt", "a")
        q.write(str(x))
        q.close
        np.append(arr = xpoints, values = x)

        q = open("Log_y.txt", "a")
        q.write(str(f))
        q.close
        np.append(arr = ypoints, values = f)
        break
    else:
        q = open("Log_x.txt", "a")
        q.write(str(x))
        q.write("\n")
        q.close
        np.append(arr = xpoints, values = x)
        
        q = open("Log_y.txt", "a")
        q.write(str(f))
        q.write("\n")
        q.close
        np.append(arr = ypoints, values = f)
    
    x += 1

g = open("Log_x.txt", "r")
h = open("Log_y.txt", "r")

#x = np.array([float(0)])
#y = np.array([float(0)])

#p = 1
#while p <= 100:
#    np.append(arr = x, values = str(g.readline(p)))
#    np.append(arr = y, values = str(h.readline(p)))
#    p += 1
#    break

print(xpoints)
print(ypoints)

plt.plot(xpoints, ypoints)
plt.show()
