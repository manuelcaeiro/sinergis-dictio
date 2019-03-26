# sinergis-dictio
A Python 3 responsive reader for the JSON representation of The Cynic's Word Book

(It will work with any other dictionary in JSON file format)

# The dictionary
Bierce's word book has only 996 words. It would frustrating to look for some words in it and probably get no output most of the times.

Fortunately, Python language has a built-in function called *get\_close_matches()* that returns "a list of the best 'good enough' matches" - see [here](https://docs.python.org/3.6/library/difflib.html), and that allows to output 'suggestions' for other (similar) words inside the word book.

# How to use
Download the bundle "cynics\_wordbook.exe" (presently only for Windows) from the repository and run it - no need to install.

If you use _Pydroid_ or _Phytonista_, download the files "gui\_dict.py" and "bierce.json" into the same folder on your mobile device, and run the .py file.

Either way, when you run the program it will appear a small window.

![](https://github.com/manuelcaeiro/sinergis-dictio/blob/master/screenshots/empty.JPG)

Enter the word which definition you're looking for in the text box and hit return. If the word is in the word book, the definition will be shown.

If the word is not in the word book you may be shown 1 or 2 alternatives...

or a message saying "Unable to read/understand your entry". That will be the case if you enter profanities like the "F word", or "@!*%&#", or "java"(1).

You can delete the word in the text box, write other word and hit return as many times as you want (until you get bored, and then you may click on "Exit" and the window will magically disappear).

(1) Python programmer's joke.

# Licences
See [here](https://github.com/manuelcaeiro/sinergis-dictio/blob/master/Licences.md)

# TODO
- Upon request: executable bundles for Ubuntu and Debian.

- Upon request (plus a generous donation): Build JSON files for other dictionaries.

- Upon request (plus a VERY generous donation): Make a fancy GUI for the dictionaries with pyglet.
