# Hangman-Final-Project

## Final project of Software Development - Summer Class

The application for this project is a hangman game with a GUI developed with tkinter and a non-standard library called breezypythongui, I used the class EasyFrame to build some of my interface. 

I built two classes, one for each window. The first window is the Hangman game window and contain all the logic for the game itself. The second, however, is the history window, where points and mistakes are stored - The points are all the correctly guessed words, and the mistakes are all the wrong letters guessed.

For my game, I used a file with 100 common English words to choose randomly.

Also, for the sake of complete validation, there is also a function to handle exceptions with input from the user

### My game and project contain:
2 window: Hangman and History window.

5 labels: used letters' label, title label, hangman word label, mistake label, and point label (last twp in the second window).

5 buttons: enter button, history button, close button, reset button, and close button in the history window.
_because there are 5 buttons, there are also 5 call back functions_

4 images: images in enter, history, reset, and close buttons in the hangman window.
_all 4 buttons have their own image, for security, however, all buttons have also alternate text if the image does not load _

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### In my project, I had initials problems with:
code organization: I had problems implementing a modular approach since there were many things I wanted to add to the project further in the process. In the end, however, I could implement a modular approach breaking down the steps I needed to follow.

changing "_" in the label for a word when there were double letters: I had a little bit of problems changing the "_" to a letter but I figured out how I should solve the problem.

communication Hangman-History: I had trouble setting the communication between both windows since I had to update the mistakes and points. I could update the History window every time you open it again, but not instantly when the point or mistake is made.

The main interface is as follows:
<br><img alt="finalProjectInterface" width="200" height="auto" src="https://github.com/user-attachments/assets/c0ece5e0-cb1e-4611-9aa0-76db80b7d8b4">
