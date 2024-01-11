from tkinter import *

def converter():
    miles = float(entry_box.get())
    km= round(miles*1.609,2)
    Label_result.config(text=f"{km}")
    


window = Tk()
# window.minsize(height=100,width=100)
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)


#entry
entry_box = Entry(width=8)
entry_box.focus()
entry_box.insert(END, string="0")
entry_box.grid(column=1,row=0)


#Labels

Label_miles = Label(text="Miles") 
Label_miles.grid(column=2,row=0)

Label_equal = Label(text="is equal to")
Label_equal.grid(column=0,row=1)

Label_result = Label()
Label_result.grid(column=1,row=1)

Label_km = Label(text="Km")
Label_km.grid(column=2,row=1)

#Button

cal_button = Button(text="Calculate",command=converter)
cal_button.grid(column=1,row=2)

window.mainloop()