import matplotlib.pyplot as plt

def collatz(n):
    """This function takes an integer n and returns the next value in the
    Collatz sequence based on whether n is even or odd."""
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1

# Get user input for starting values and number of sequences
start = int(input("Enter starting value: "))
num_seqs = int(input("Enter number of sequences to graph: "))

# Initialize lists to hold x and y values for graph
x_vals = []
y_vals = []

# Generate Collatz sequences and add to lists
for i in range(num_seqs):
    n = start + i
    curr_x = [i+1]
    curr_y = [n]
    while n != 1:
        n = collatz(n)
        curr_x.append(len(curr_x)+1)
        curr_y.append(n)
    x_vals.append(curr_x)
    y_vals.append(curr_y)

# Create graph
for i in range(num_seqs):
    plt.plot(x_vals[i], y_vals[i], label=str(start+i))
plt.xlabel("Step")
plt.ylabel("Value")
plt.title("Collatz Conjecture")
plt.legend()
plt.show()
