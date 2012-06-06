from numpy import pi, sin, cos, arange
from matplotlib.pyplot import figure, show, plot
from matplotlib.animation import FuncAnimation

fig = figure()

x = arange(0, 2*pi, 0.02)
foo = plot(x, sin(x))[0]
bar = plot(x, cos(x))[0]

def animate(i):
    dx = 0.02
    foo.set_ydata(sin(x+i*dx))
    bar.set_ydata(cos(x+i*dx))

ani = FuncAnimation(fig, animate, arange(1, 314), interval=20)
show()
