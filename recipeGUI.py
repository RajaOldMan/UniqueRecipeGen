from tkinter import *
from recipe import main

def getIngre(event):
    ingre = ingreEntry.get()
    finalEntry.delete(0, "end")
    ingreList = main(ingre)
    if ingreList[0] == "-":
        finalEntry.insert(0, "Ingredient does not exist")
    else:
        result = ""
        for str in ingreList:
            result += str
            if str != ingreList[len(ingreList) - 1]:
                result += ", "
        finalEntry.insert(0, result)

root = Tk()
root.title("Unique Recipe Generator")

Label(root, text="Enter Ingredient: ").pack(side=LEFT)
ingreEntry = Entry(root)
ingreEntry.pack(side=LEFT)                    

submitButton = Button(root, text="submit", width = 8)

submitButton.bind("<Button-1>", getIngre)
submitButton.bind("<Return>", getIngre)
submitButton.pack(side=LEFT)

finalEntry = Entry(root, width = 80)
finalEntry.pack(side=LEFT)

root.mainloop()
