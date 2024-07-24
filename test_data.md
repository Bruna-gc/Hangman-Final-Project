# Set of test data to fully validate the program 
## The Following are screenshots of how the script deals with each of those scenarios and a brief explanation of how it was done. The words used to test all the possibilities were "Pretty" and "Office"

## **Words used to check different scenarios:**
### **pretty** – word used to check double word functioning and check the case where the same letter is input more than once.

<br><img alt="double_letters" width="200" height="auto" src="https://github.com/user-attachments/assets/9edb9385-709a-4786-a380-fc6b717796f5"><br>
Successfully passed the test of double words after change: 
The problem was the assignments of key/value pairs in the dictionary.
Key: letter/value: tkinter label. 
_I changed to key: tkinter label/value: letter_

<br><img alt="double_letters" width="200" height="auto" src="https://github.com/user-attachments/assets/1d8fe182-7093-45e2-bcc4-cb5475789245"><br>
Successfully passed the test of raising error after input equal to a letter in the used letters after the change: 
I just added a if-else statement to determine if the letter was already in the list of used words, if so, an error would be raised. 

----------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------

### **Office – a word used to check input validation**
<br><img alt="double_letters" width="200" height="auto" src="https://github.com/user-attachments/assets/a3c74c84-d0ef-4f58-b58c-ebe754639971"><br>
Successfully passed the test of double letters in the input after change.
I added an if statement to check if the input is greater than 1. If so, an error message would appear.

<br><img alt="double_letters" width="200" height="auto" src="https://github.com/user-attachments/assets/1e5f1ba9-49fb-4c15-a505-37e2d3c8f582"><br>
Successfully passed the test of input, which was not a letter after the change.
I added an if statement to check if the input is a letter. If not, an error message will appear.


<br><img alt="double_letters" width="200" height="auto" src="https://github.com/user-attachments/assets/f4593d2a-e7fb-4fbf-9468-78524b435fa5"><br>
Successfully passed the test after the player loses.
After the user lost, I disabled the button. Because I did it, I had to remove the bind () of the input area to disable the player from guessing a letter after they lost it.

