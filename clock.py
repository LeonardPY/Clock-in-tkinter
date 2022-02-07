from tkinter import *
import math
import datetime


# x coordinate in radian 
def x_coordinate(length, angle):
    return width / 2 + length * math.cos(angle * math.pi / 180)

# y coordinate in radian 
def y_coordinate(length, angle):
    return height / 2 - length * math.sin(angle * math.pi / 180)

# paramert screean
width = 400
height = 400
# to center degree
radius = 150

# Tk(scrren)
root = Tk()
# name projecta 
root.title("Clock")

# Convas funkci gives a screen parameter
canvas = Canvas(root, width = width , height = height)
canvas.pack()
# screen create oval 
canvas.create_oval(width/2-radius, height/2-radius, width/2 + radius, height/2 +radius)
seconds = canvas.create_line(0, 0, 0, 0, fill = "red")
minutes = canvas.create_line(0, 0, 0, 0)
hours = canvas.create_line(0, 0, 0, 0)

def change_hand(length, time, clock_hand, degres):
    alpha = 90 - time * degres
    x1 = x_coordinate(0, alpha)
    y1 = x_coordinate(0, alpha)
    x2 = x_coordinate(length, alpha)
    y2 = y_coordinate(length, alpha)
    canvas.coords(clock_hand, x1,y1,x2,y2)

def update():
    time = str(datetime.datetime.now())
    sec = int(time[17:19])
    min = int(time[14:16])
    h = int(time[11:13])

    change_hand(radius - 20, sec, seconds, 6)
    change_hand(radius - 40, min, minutes, 6)
    change_hand(radius - 60, h, hours, 30)

    root.after(1000, update)

alpha = 60
for i in range(1, 13):
    canvas.create_text(x_coordinate(radius + 10, alpha), y_coordinate(radius + 10, alpha), text=i,
                        fill = "darkblue", font="Times 10 italic bold")
    alpha -= 30
    
for i in range(60):
    x1 = x_coordinate(radius, alpha)
    y1 = y_coordinate(radius, alpha)
    if alpha % 30 == 0:
        x2 = x_coordinate(radius-20, alpha)
        y2 = y_coordinate(radius-20, alpha)
    else:
        x2 = x_coordinate(radius-10, alpha)
        y2 = y_coordinate(radius-10, alpha)
    canvas.create_line(x1, y1, x2, y2)
    alpha += 6

update()
# the Tk screen will not close
root.mainloop()
