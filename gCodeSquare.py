import math
import tkinter as tk


def generate():
    # get the entered value from the entry field and convert it to float and then add
    xMax = float(n1.get())
    yMax = float(n2.get())
    step = float(n3.get())
    delay = float(n4.get())
    # path = 'C:/Users/mrave/OneDrive/Desktop/ugsplatform-win/'
    path = 'C:/Users/Sonus/OneDrive - Sonus Microsystems/Desktop/ugsplatform-win/'
    fileName = 'square'

    # xMax = float(input("Enter x dimention in mm: "))
    # yMax = float(input("Enter y dimention in mm: "))
    # step = float(input("Enter the step size in mm: "))
    # delay = float(input("Enter the pause time at each point in seconds: "))

    gcodeFile = open(fileName + '.nc', 'w')

    # G21 makes the default unit mm
    # G91 makes machine movements absolute instead of relative (X1Y0Z0 becaomes a movmement of 1 to the right instead of \
    # moving to the coordinate (1, 0, 0)
    gcodeFile.write("G21\nG91\n\n")

    # The yMax and yMax are the number of steps taken, not distance
    # They need to increase if the step size is smaller than 1 or decrease if the step size is large than 1
    ySteps = int(math.ceil(yMax / step))
    xSteps = int(math.ceil(xMax / step))

    # Moves the device to the corner of the square to begin scan
    gcodeFile.write("G0 X-" + str(xMax // 2) + "Y-" + str(yMax // 2) + "\nG4 P" + str(delay) + "\n\n")

    for i in range(ySteps):
        if (i % 2 == 0):
            for j in range(xSteps - 1):
                # each of these loops includes a movement for positive X movements and a G4 for Dwell
                # Note the text G0 is not included as it was already used when moving to the corner
                gcodeFile.write("X" + str(step) + "\nG4 P" + str(delay) + "\n")
        else:
            for j in range(xSteps - 1):
                # each of these loops includes a movement for negative X movements and a G4 for Dwell
                # Note the text G0 is not included as it was already used when moving to the corner
                gcodeFile.write("X-" + str(step) + "\nG4 P" + str(delay) + "\n")
        if (i < ySteps - 1):
            # the final point in the y direction doesn't require a movement because the machine starts at 1mm
            gcodeFile.write("\nY" + str(step) + "\nG4 P" + str(delay) + "\n\n")
    tk.Label(frame, font=("Helvetica", 14), text="Done!", bg='Light Blue').grid(row=8)



root = tk.Tk()
root.title("gcode Values")
operator=""

canvas = tk.Canvas(root, height=200, width=310, bg="White")
canvas.pack()
frame=tk.Frame(root, bg="Light Blue")
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

xMaxButton = tk.Label(frame, font=("Helvetica", 14), text="xMax (mm):", bg='Light Blue').grid(row=0)

tk.Label(frame, font=("Helvetica", 14), text="yMax (mm):", bg='Light Blue').grid(row=2,column=0)

tk.Label(frame, font=("Helvetica", 14), text="Step Size (mm):", bg='Light Blue').grid(row=4,column=0)

tk.Label(frame, font=("Helvetica", 14), text="Step Delay (s):", bg='Light Blue').grid(row=6,column=0)

# define entry variables
n1 = tk.StringVar()
n2 = tk.StringVar()
n3 = tk.StringVar()
n4 = tk.StringVar()

# assign the StringVar to the entry widget textvariables
num1 = tk.Entry(frame, textvariable = n1)
num1.grid(row = 0, column = 1)
num1.insert(0, '10')
num2 = tk.Entry(frame, textvariable = n2)
num2.grid(row = 2, column = 1)
num2.insert(0, '10')
num3 = tk.Entry(frame, textvariable = n3)
num3.grid(row = 4, column = 1)
num3.insert(0, '1')
num4 = tk.Entry(frame, textvariable = n4)
num4.grid(row = 6, column = 1)
num4.insert(0, '3')

generate=tk.Button(frame, text="Generate gcode", height="2", width="14", fg="Black", bg="yellow", command=generate )
generate.grid(row=8, column=1)

root.mainloop()



