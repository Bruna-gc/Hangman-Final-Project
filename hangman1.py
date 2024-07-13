import tkinter as tk
from tkinter import ttk

# class for windows
class Window:
    """ make layout for all windows"""
    def __init__(self, master, title):
        self.title = title
        self.window = tk.Toplevel(master) if master else tk.Tk() 
        self.window.geometry("450x600")
        self.window.title(title)
        self.window.configure(bg="#0F67B1")

        try:
            self.next_button = tk.PhotoImage(file="next-buttonSmall.png")
        except tk.TclError:
            print("Failed ot load image. Check file path.")
            self.next_button = None

        if self.next_button:
            self.button = tk.Button(self.window, image=self.next_button, bg=self.window.cget('bg'), borderwidth=0, highlightthickness=0)
            self.button.grid(row=2, column=2)
        else:
            print("Using text button as fallback")
            self.button = tk.Button(self.window, text="Next")
            self.button.grid(row=2, column=2)
# main window
main_window = Window(None, "Hangman")

# games history
history_window = Window(main_window.window, "History")

# next_button = tk.PhotoImage(file="next-buttonSmall.png")
# button = tk.Button(main_window, image=next_button, background=None)
# button.grid(row=2, column=2)

main_window.window.mainloop()
