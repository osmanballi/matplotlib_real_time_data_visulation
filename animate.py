import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('ggplot')

def animate(i):

    data= pd.read_csv("data.csv")
    x=data["x_value"]
    y1=data["y1_value"]
    y2=data["y2_value"]

    plt.cla()

    plt.plot(x, y1, label="y1 values")
    plt.plot(x, y2, label="y2 values")

    plt.legend(loc = "upper left")
    plt.tight_layout()

animation = FuncAnimation(plt.gcf(),animate,interval=1000)
plt.show()