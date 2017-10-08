from tkinter import *
from recipe import main

def getIngre(event):
    ingre = ingreEntry.get()
    finalEntry.delete(0, "end")
    extrasEntry.delete(0, "end")
    ingreList = main(ingre)
    if ingreList[0] == "-":
        finalEntry.insert(0, "Ingredient does not exist")
    else:
        result = " "
        extras = " "
        for i in range(7):
            if i < 5:
                result += ingreList[i]
                if i != 4:
                    result += ", "

            else:
                extras += ingreList[i]
                if i == 5:
                    extras += ", "
    
        finalEntry.insert(0, result)
        extrasEntry.insert(0, extras)

root = Tk()
root.title("The Overactive Imagination Food Bible")

Label(root, text=" Enter Ingredient ").pack(side=LEFT)
ingreEntry = Entry(root)
ingreEntry.pack(side=LEFT)                    

submitButton = Button(root, text="submit", width = 8)

submitButton.bind("<Button-1>", getIngre)
submitButton.bind("<Return>", getIngre)
submitButton.pack(side=LEFT)

Label(root, text=" Main Ingredients: ").pack(side=LEFT)

finalEntry = Entry(root, width = 100)
finalEntry.pack(side=LEFT)

Label(root, text=" Suggested Extras: ").pack(side=LEFT)

extrasEntry = Entry(root, width = 50)
extrasEntry.pack(side=LEFT)

Label(root, text=" ").pack(side=LEFT)

root.mainloop()
