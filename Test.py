import numpy as np
import matplotlib.pyplot as plt
import math as m

# Get user input for parameters
while True: 
    print("Enter value for a:")
    a = int(input())

    print("Enter 'cos' or 'sin':")
    sf = input().lower()
    if sf not in ["cos", "sin"]:
        print("Invalid input. Try again.")
        continue

    print("Enter value for b:")
    b = int(input())

    print("Enter value for h:")
    h = int(input())

    print("Enter value for k:")
    k = int(input())

    # If all inputs are valid, break out of loop
    break

# Generate x values and calculate y values
x = np.arange(0, 101)
if sf == "cos":
    y = a * np.cos(b * (x - h)) + k
else:
    y = a * np.sin(b * (x - h)) + k

# Save data to files
np.savetxt("Log_x.txt", x, delimiter=",")
np.savetxt("Log_y.txt", y, delimiter=",")

# Plot the data
plt.plot(x, y)
plt.show()
