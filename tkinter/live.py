import matplotlib.pyplot as plt
import matplotlib.animation as an
from random import randint
x = [var for var in range(1,51)]
y= [randint(5,25) for var in range(1,51)]
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
def change(interval):
    global x,y
    ax.clear()
    x.append(x[-1]+1)
    y.append(randint(5,25))
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Graph")
    ax.plot(x,y,"b:")
    ax.scatter(x,y,c='r')
    x.pop(0)
    y.pop(0)
    ax.set_xlim(-5+x[0],5+x[-1])
    ax.set_ylim(0,30)
ani = an.FuncAnimation(fig,change,interval=1) #1000 mili seconds
plt.show()
