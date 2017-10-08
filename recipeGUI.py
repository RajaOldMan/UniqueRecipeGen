from tkinter import *
from recipe import main

def getIngre(event):
    ingre = ingreEntry.get()
    finalEntry.delete(0, "end")
    finalEntry.insert(0, main(ingre))

root = Tk()
root.title("Unique Recipe Generator")

Label(root, text="Enter Ingredient: ").pack(side=LEFT)
ingreEntry = Entry(root)
ingreEntry.pack(side=LEFT)                    

submitButton = Button(root, text="submit")

submitButton.bind("<Button-1>", getIngre)
submitButton.pack(side=LEFT)

finalEntry = Entry(root, width = 100)
finalEntry.pack(side=LEFT)

root.mainloop()
