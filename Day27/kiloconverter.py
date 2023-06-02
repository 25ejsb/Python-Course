from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=20, pady=10)

fontsize = 15

EntryMiles = Entry(width=15)
EntryMiles.grid(column=1, row=0)

Miles = Label(text="   Miles", font=("Arial", fontsize))
Miles.grid(column=2, row=0)

calculatorLabel = Label(text="is equal to", font=("Arial", fontsize))
calculatorLabel.grid(column=0, row=1)

amountofkm = Label(text="0", font=("Arial", fontsize))
amountofkm.grid(column=1, row=1)

kmlabel = Label(text="Km", font=("Arial", fontsize))
kmlabel.grid(column=2, row=1)

def convert():
    amountofkm.config(text=str(int(EntryMiles.get()) * 1.609344))

calculator = Button(text="Calculate", font=("Arial", fontsize), command=convert)
calculator.grid(column=1, row=2)

window.mainloop()