import tkinter as tk
from breezypythongui import EasyFrame
from random import choice

class Hangman(EasyFrame):
    def __init__(self, word):
        EasyFrame.__init__(self, title="Hangman", width="450", height="600", resizable=False)
        self.history_window = None

        self.mistakes = 0
        self.points = 0

        self.used_letters_list = []
        self.word = word
        self.list_letters = [i for i in word]  # Replace with word selection logic later

        self.load_images()
        self.setup_GUI()

    def new_word(self):
        # get word form list of words
        with open("word_list.txt", "r") as file:
            list_word = [line.strip() for line in file]
            word = choice(list_word)
            print(word)
        return word

    def load_images(self):
        """Load all the images"""
        self.close = tk.PhotoImage(file="images/close.png")
        self.history = tk.PhotoImage(file="images/button_history.png")
        self.enter = tk.PhotoImage(file="images/button_enter.png")
        self.reset = tk.PhotoImage(file="images/button_reset.png")

    def setup_GUI(self):
        """Set up all the GUI"""
        self.create_header_panel()
        self.create_used_letters_label()
        self.create_hangman_panel()
        self.create_word_panel()
        self.create_buttons_panel()
        self.create_input_area()


    def create_header_panel(self):
        """Create the header pannel with close btton and title"""
        header_panel = self.addPanel(row=0, column=0, columnspan=3, background="gray")
        self.close_button = header_panel.addButton(text="close", row=0, column=0, command=self.quit)
        self.make_button(self.close_button, self.close, color="gray")
        self.title = header_panel.addLabel(text="Hangman Game", row=0, column=1, font="Helvetica 20", background="gray", sticky='W')

    def create_used_letters_label(self):
        """Create the label for used letter"""
        self.used_letters = self.addLabel(text="Used letters", row=2, column=0, columnspan=3, font="Helvetica 10", sticky="NEWS")

    def create_hangman_panel(self):
        """Create hangman pannel in the window"""
        hangman_panel = self.addPanel(row=4, column=0, columnspan=3, background="light blue")
        hangman_panel.addLabel(text="possible hangman will go here", row=0, column=0, sticky='NEWS', background="light blue")
        self.canvas = tk.Canvas(self, width=200, height=200, background="light blue", borderwidth=0)
        self.canvas.grid(row=4, column=0, columnspan=3)

    def create_word_panel(self):
        """Create the word panel in the window"""
        self.word_panel = self.addPanel(row=6, column=0, background="beige", columnspan=3)
        self.word_dict = {}
        for i, value in enumerate(self.list_letters):
            key = self.word_panel.addLabel(text="_", row=0, column=i, sticky='NWES', font="Helvetica 20", background="beige")
            self.word_dict[key] = value

    def create_input_area(self):
        """Create the input area in the window"""
        self.letter_input = self.addTextField(text="", row=8, column=0)
        # if self.enter_button["state"] == "normal":
        #     self.letter_input.bind("<Return>", lambda event: self.onSubmit())


    def create_buttons_panel(self):
        """Create button area"""
        self.buttons_panel = self.addPanel(row=8, column=2)
        self.create_buttons(self.buttons_panel)

    def create_buttons(self, buttons_panel):
        """Create the button in the window"""
        self.enter_button = buttons_panel.addButton(text="Enter", row=0, column=0, command=self.onSubmit)
        self.make_button(self.enter_button, self.enter)
        self.history_button = buttons_panel.addButton(text="History", row=0, column=1, command=self.show_history)
        self.make_button(self.history_button, self.history)
        self.new_game = buttons_panel.addButton(text="reset", row=0, column=2, command=self.new_game)
        self.make_button(self.new_game, self.reset)

    def make_button(self, button, image, color="white"):
        """Makes button with images in GUI"""
        button["image"] = image
        button.config(width=image.width(), height=image.height(), borderwidth=0, background=color)

    def show_history(self):
        """Show history window"""
        # self is the master window :) !
        if self.history_window == None:
            History(self)
        else:
            self.update()

    def onSubmit(self):
        """Main logic of the game. Check if letter in word when enter button is pressed"""
        letter = self.letter_input.getText().lower()
        if self.exceptions(letter):
            return
        if letter in self.list_letters:
            self.change_key(letter)
            if self.check_win():
                self.won()
                self.points += 1
        else:
            self.used_letters["text"] = self.add_to_used_letters(letter)
            self.mistakes += 1
            self.draw_hangman()
            if self.mistakes >= 7:
                self.lost()
        self.letter_input.setText("")

    def exceptions(self, letter):
        """handles exceptions"""
        if len(letter) != 1:
            tk.messagebox.showerror("Invalid letter", "enter a letter")
            return True
        if not letter.isalpha():
            tk.messagebox.showerror("Invalid letter", "The input must be a letter")
            return True
        if letter in self.used_letters_list:
            tk.messagebox.showerror("Invalid letter", "You already chose this letter!")
            return True
        return False
    
    def change_key(self, letter):
        """Change key of the dict to be equal to the letter"""
        for key, value in self.word_dict.items():
            if value == letter:
                key["text"] = value

    def add_to_used_letters(self, letter):
        """Add letter to used letters"""
        self.used_letters_list.append(letter)
        return "Guessed letters: " + ", ".join(self.used_letters_list)

    def check_win(self):
        """Return if all letters are in word"""
        # all() method will return true if all the letters are in word and false otherwise
        return all(key["text"] == value for key, value in self.word_dict.items())
    
    def  won(self):
        """Changet the title (winnig), diable the button and clear the canvas"""
        self.title["text"] = "CONGRATULATIONS!"
        self.enter_button["state"] = "disabled"
        self.canvas.delete("all")

    def lost(self):
        """Chnage the title (losing), disable the button and cleat the canvas"""
        self.title["text"] = "OH, YOU LOST!"
        self.enter_button["state"] = "disabled"
        self.canvas.delete("all")

    def new_game(self):
        """Reset the hole game"""
        self.title["text"] = "Hangman Game"
        self.enter_button["state"] = "normal"
        # reset used words list and label
        self.used_letters_list = []
        self.used_letters["text"] = "Used letters"

        # reset the list of letters in word
        word = self.new_word()
        self.list_letters = [i for i in word] 

        # reset list of "_" for word
        for i in self.word_dict.keys():
            self.word_dict[i] = "_"

        # reset label
        for i, value in enumerate(self.list_letters):
            key = self.word_panel.addLabel(text="_", row=0, column=i, sticky='NWES', font="Helvetica 20", background="beige")
            self.word_dict[key] = value

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
    

class History(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Game History")
        self.geometry("200x100")
        label_points = tk.Label(self, text="Curent Points: " + str(self.master.points))
        label_mistakes = tk.Label(self, text="\nCurent Mistakes: " + str(self.master.mistakes))

        label_points.grid(row=0, column=0)
        label_mistakes.grid(row=1, column=0)

        label_points.config(text="Curent Points: " + str(self.master.points))
        label_mistakes.config(text="\nCurent Mistakes: " + str(self.master.mistakes))

        tk.Button(self, text="close", command=self.destroy).grid(row=2, column=0)


def main():
    # get word form list of words
    with open("word_list.txt", "r") as file:
        list_word = [line.strip() for line in file]
        word = choice(list_word)
        print(word)
    Hangman(word).mainloop()

if __name__ == "__main__":
    main()
