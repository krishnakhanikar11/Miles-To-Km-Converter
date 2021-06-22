from tkinter import *

window = Tk()
window.title("mile to km")
window.minsize(width=300, height=300)

label = Label(text="is Equal to")
label.grid(row = 1, column = 0, sticky = W, pady = 2)


label2 = Label(text="Miles")
label2.grid(row = 0, column = 2, sticky = W, pady = 2)

def action():
    answer = float(entry.get())
    in_km = answer*1.60934
    label3.config(text=in_km)
    return in_km

entry = Entry(width=15)
entry.grid(row = 0, column = 1, sticky = W, pady = 2)

label3 = Label(text="0")

label3.grid(row = 1, column = 1, sticky = W, pady = 2)

label4 = Label(text="Km")
label4.grid(row = 1, column = 2, sticky = W, pady = 2)

#calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(row = 2, column = 1, sticky = W, pady = 2)



window.mainloop()
