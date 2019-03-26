from tkinter import *
import json
from difflib import get_close_matches

# Loading the json data as python dictionary
with open("bierce.json") as dfile:
    data = json.load(dfile)

def exit():
    return w.destroy()

def evaluate(event):
    res.configure(text="-- " +  definition(entry.get()))

def definition(word):
    word = word.upper()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        alt = get_close_matches(word, data.keys(), n=2)
        out = "That word could not be found; \n-- The closest word(s) in this dictionary:  "
        if len(alt) == 2:
            return out + str(alt[0]) + ', ' + str(alt[1])
        else:
            return out + str(alt[0])
    else:
        return ("Unable to evaluate your entry.")

w = Tk()
w.title("Dictionary")
w.minsize(300, 190)
Label(w, text="The Cynic's Word Book (1906 edition)\n").pack()
Label(w, text="Enter a word and hit return:").pack()
entry = Entry(w)
entry.bind("<Return>", evaluate)
entry.pack()
res = Message(w)
Label(w, text="Definition:").pack()
res.pack()
b = Button(w, text="Exit", command=exit).pack()

w.mainloop()


