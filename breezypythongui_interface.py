from breezypythongui import EasyFrame
from tkinter import messagebox
import tkinter as tk

# var = tk.StringVar()
# entry = tk.Entry()

class Hangman(EasyFrame):
    """class will define the hangman frame"""
    def __init__(self):
        EasyFrame.__init__(self, title="Hangman", width="450", height="600")
        self.setup_GUI()
        # mistakes in game
        self.mistakes = 0

    def setup_GUI(self):
        # create list for letters in word
        # I will add a file full of words and use it here later on
        self.list_letters = [i for i in "eye"]
        
        #header panel
        headerPanel = self.addPanel(row=0, column=0, columnspan=3, background="gray")
        headerPanel.addButton(text="Close", row=0, column=0, command=self.quit)
        headerPanel.addLabel(text="Title will go here", row=0, column=1, font="Heveltica 20" ,background="gray", sticky='W')

        # used words
        self.used_letters_list = []
        self.used_letters = self.addLabel(text="Used words", row=2, column=0, font="Heveltica 10", sticky="NEWS")

        #hangman panel
        hangmanPanel = self.addPanel(row=4, column=0, columnspan=3, background="light blue")
        hangmanPanel.addLabel(text="possible hangman will go here", row=0, column=0, sticky='NEWS', background="light blue")
        self.canvas = tk.Canvas(self, width=200, height=200)
        self.canvas.grid(row=4, column=0, columnspan=3)

        #word panel
        wordPanel = self.addPanel(row=6, column=0, background="beige", columnspan=3)

        # create dict for key = text / value = letter, I couldn't creat the diffetrent keys for double letters
        self.word_dict = {}
        for i in range(len(self.list_letters)):
            value = self.list_letters[i]
            key = wordPanel.addLabel(text="_",row=0, column=i, sticky='NWES', font="Heveltica 20", background="beige")
            self.word_dict[key] = value

        self.letter_input = self.addTextField(text="", row=8, column=0)
        # var = tk.StringVar()
        # self.letter_input= tk.Entry(self, textvariable=var)
        # self.letter_input.grid(row=8, column=1)

        self.addButton(text="Enter", row=8, column=2, command=self.onSubmit)
        # tk.Button(self, text="Enter tk", background="pink",highlightbackground="blue", command=self.onSubmit).grid(row=8, column=2)
        self.addButton(text="History", row=10, column=2, command=self.show_history)

    def show_history(self):
        History(self)

    def onSubmit(self):
        """Define action of button"""
        letter = self.letter_input.getText().lower()

        if self.exceptions(letter):
            return

        if self.is_in_word(letter, self.list_letters):
            self.change_key(letter)
            print("is in word")
            if self.check_win():
                messagebox.showwarning("You win!", "You won the game, Congratulations!")
        else:
            self.used_letters["text"] = self.add_to_used_letters(letter)
            self.mistakes += 1
            self.draw_hangman()
        self.letter_input.setText("")

    def exceptions(self, letter):
        if len(letter) != 1:
            messagebox.showerror("Invalid letter", "enter a letter")
            return True
        if not letter.isalpha():
            messagebox.showerror("Invalid letter", "The input must be a letter")
            return True
        if letter in self.used_letters_list:
            messagebox.showerror("Invalid letter", "You already chose this letter!")
            return True

    def draw_hangman(self):
        """Draw hangman"""
        if self.mistakes >= 1:
            # Draw the gallows
            self.canvas.create_line(20, 190, 100, 190, width=3)
            self.canvas.create_line(60, 190, 60, 20, width=3)
            self.canvas.create_line(60, 20, 150, 20, width=3)
            self.canvas.create_line(150, 20, 150, 50, width=3)

        if self.mistakes >= 2:
            # Draw the head
            self.canvas.create_oval(130, 50, 170, 90, width=2)

        if self.mistakes >= 3:
            # Draw the body
            self.canvas.create_line(150, 90, 150, 140, width=2)

        if self.mistakes >= 4:
            # Draw the left arm
            self.canvas.create_line(150, 100, 120, 120, width=2)

        if self.mistakes >= 5:
            # Draw the right arm
            self.canvas.create_line(150, 100, 180, 120, width=2)

        if self.mistakes >= 6:
            # Draw the left leg
            self.canvas.create_line(150, 140, 130, 180, width=2)

        if self.mistakes >= 7:
            # Draw the right leg
            self.canvas.create_line(150, 140, 170, 180, width=2)
    
    def check_win(self):
        count = 0
        for key, value in self.word_dict.items():
            print(key["text"], value)
            if key["text"] == value:
                count += 1
        if count == len(self.list_letters):
            return True
        return False

    def is_in_word(self, letter, list):
        return letter in list

    def change_key(self, letter):
        for key, value in self.word_dict.items():
            if value == letter:
                key["text"] = value    

    def add_to_used_letters(self, letter):
        print(self.used_letters_list)
        self.used_letters_list.append(letter)
        return "Guessed letters: "+", ".join(self.used_letters_list)
            
    def new_game(self):
        """Will reset the hangman game"""
        self.used_letters["text"] = "Used letters:"
        # clean the hangman panel
        pass

class History(tk.Toplevel):
    """History class as a Toplevel window"""
    def __init__(self, master):
        self.top = super().__init__(master)
        self.title("Game History")
        self.geometry("300x400")
        tk.Label(self, text="Hello there!").grid(row=0, column=0)
        tk.Button(self, text="close", command=self.close).grid(row=1, column=0)

    def close(self):
        """Close toplevel window"""
        self.destroy()

def main():
    Hangman().mainloop()

if __name__ == "__main__":
    main()
