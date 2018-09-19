### Example 11-1: Example tkinter program for structured graphics

# Note: this cannot be run from within IDLE since IDLE is itself a
# tkinter application. Run from the command line or another IDE.

colors = ('gray80', 'black', 'black', 'gray30',
          'gray50', 'gray70', 'gray30', 'black')
import tkinter
tk = tkinter.Tk()                   # initialize tkinter
tk.title('demo')                    # give window a title
canvas = tkinter.Canvas(tk)         # create the canvas
canvas.pack()                       # use the Packer geometry manager
canvas.create_rectangle(20, 10, 120, 80, fill=colors[0])
canvas.create_line(20, 100, 120, 100, width=4, fill=colors[1])
canvas.create_line(20, 170, 45, 115, 70, 170, 95, 115,
                   120, 170, fill=colors[2])
canvas.create_polygon(150, 180, 175, 115, 190, 160, 215, 125,
                       240, 180, fill=colors[3])
canvas.create_oval(180, 55, 250, 115, fill=colors[4])
canvas.create_arc(140, 10, 240, 80, extent=240,
                  width=4, fill=colors[5], outline=colors[6])
canvas.create_text(20, 190, text='Drawing on a tkinter canvas',
                   anchor='w', font=(('Verdana', 'sans'), 14, 'italic'),
                   fill=colors[7])

input('Press the Return key to close the window(s)')
tk.destroy()                         # close the window
