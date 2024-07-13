from breezypythongui import EasyFrame

from tkinter import PhotoImage
import tkinter as tk

# word = "appartment"

class Hangman(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Hangman Frame with breezypythongui", width="450", height="600")
        self.image = PhotoImage(file="images/lineNoBG.png")

        # create list for letters in word
        self.list_letters = [i for i in "appartment"]

        # self.list_letters = []
        # for i in range(len("school")):
        #     if "school"[i] == "school"[i-1]:
        #         self.list_letters.append("school"[i]+str(i))
        #     self.list_letters.append("school"[i])

        # print(self.list_letters)
        wordPanel = self.addPanel(row=2, column=0, background="beige")

        # create dict for key = letter / value = image dash 
        self.word_dict = {}
        for i in range(len(self.list_letters)):
            value = self.list_letters[i]
            key = wordPanel.addLabel(text="_",row=2, column=i, sticky='NWES', font="Arial", background="beige")
            self.word_dict[key] = value

        # print(self.word_dict)

        self.letter_input = self.addTextField(text="", row=3, column=0)

        self.addLabel(text="This is a label", row=1, column=0, sticky="NEWS")
        self.addButton(text="Button", row=4, column=0, command=self.onSubmit)

    def onSubmit(self):
        letter = self.letter_input.getText()
        # print(self.word_dict.items())
        items = [i for i in self.word_dict.items()]

        for (key, value) in items:
            print(key, value)
            if letter in (key,value)[-1]:
                key["text"] = value
                # self.word_dict[new_key] = self.word_dict.pop(key)

        # if letter in self.list_letters:
        #     # self.word_dict[letter]["text"] = letter
        #     # print(self.word_dict.values())
        #     pass
            else:
                print('Not in word')
            self.letter_input.setText("")


def main():
    Hangman().mainloop()

if __name__ == "__main__":
    main()