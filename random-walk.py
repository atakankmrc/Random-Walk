import random
import numpy as np
import matplotlib.pyplot as plt

xArray = []
iArray = []

numberOfSteps = 100  # Change this to change number of steps


def random_walk1D(n):
    x = 0
    for i in range(1, n+1):
        step = random.choice(["up", "down"])
        if step == "up":
            x = x + 1
        else:
            x = x - 1
        xArray.append(x)
        iArray.append(i)
    return(x)


walk = random_walk1D(numberOfSteps)
text = "Last Position: " + str(walk)

plt.plot(iArray, xArray)
plt.suptitle(text)
plt.title("Random Walk")
plt.xlabel("Step")
plt.ylabel("Position")
plt.show()
