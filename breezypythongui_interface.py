from breezypythongui import EasyFrame
from tkinter import messagebox

from tkinter import PhotoImage
import tkinter as tk

# word = "appartment"

class Hangman(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Hangman Frame with breezypythongui", width="450", height="600")

        # create list for letters in word
        self.list_letters = [i for i in "appartment"]
        
        #header panel
        headerPanel = self.addPanel(row=0, column=0, columnspan=3, background="gray")
        headerPanel.addButton(text="Exit", row=0, column=0, command=self.quit)
        headerPanel.addLabel(text="Title will go here", row=0, column=1, background="gray", sticky='W')

        # used words
        self.used_letters_list = set()
        self.used_letters = self.addLabel(text="Used word will go here", row=2, column=0, sticky="NEWS")

        #hangman panel
        hangmanPanel = self.addPanel(row=4, column=0, columnspan=3, background="light blue")
        hangmanPanel.addLabel(text="possible hangman will go here", row=0, column=0, sticky='NEWS', background="light blue")

        #word panel
        wordPanel = self.addPanel(row=6, column=0, background="beige", columnspan=3)

        # create dict for key = text / value = letter, otherwise I couldn't creat the same key for double letters
        self.word_dict = {}
        for i in range(len(self.list_letters)):
            value = self.list_letters[i]
            key = wordPanel.addLabel(text="_",row=0, column=i, sticky='NWES', font="Arial", background="beige")
            self.word_dict[key] = value

        self.letter_input = self.addTextField(text="", row=8, column=1, sticky='NW')

        self.addButton(text="Enter", row=8, column=2, command=self.onSubmit)


    def onSubmit(self):
        letter = self.letter_input.getText()
        if len(letter) != 1:
            messagebox.showerror("Invalid letter", "enter only one letter")
            return

        # for loop bcause of double letters in words
        for (key, value) in self.word_dict.items():
            if letter.lower() in (key,value)[-1]:
                key["text"] = value
            else:
                print('Not in word')
                self.used_letters_list.add(letter+",")
                # assign text to list of words (for better display)
                self.used_letters["text"] = list(self.used_letters_list)
                self.letter_input.setText("")
                return
            self.letter_input.setText("")


def main():
    Hangman().mainloop()

if __name__ == "__main__":
    main()
