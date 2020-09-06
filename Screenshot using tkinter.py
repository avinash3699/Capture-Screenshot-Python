# Python Program to take Screenshot with GUI

# importing 'tkinter' module for GUI
# importing 'pyautogui' module for taking screenshot

from tkinter import *
from pyautogui import screenshot

# creating and setting the title of the GUI window
window = Tk()
window.title("Taking Screenshot using tkinter and pyautogui")

# uncomment the below line to restrict the user to change the dimensions
#window.resizable(width=FALSE,height=FALSE)

# changing the background color of the GUI window to 'black'
window.configure(background="black")

# global declaration of variable 'count_of_screenshots'
# this counts the number of screenshot the user took and  the count on the screen
count_of_screenshot = 1

# fuction that executes the screenshot process when 'screen_shot_button' is clicked
def clicked():
    global count_of_screenshot

    ''' capturing screenshot using the method 'screenshot' from 'pyautogui' module and
        saving it using 'save' method in which the desired name of screenshot is passed '''
    
    ss = screenshot()
    ss.save("screenshot%d.jpeg"%(count_of_screenshot))
    print_completed = Label(window,text="Screenshot " + str(count_of_screenshot) + " taken..!", fg="yellow",bg="black").pack()

    # incrementing the value of 'count_of_screenshot' when the user takes one
    count_of_screenshot += 1

# creeating a button for taking a screenshot
screen_shot_button = Button(window, text = "Click here to take screenshot\nYou can take multiple screenshots", bd=0, bg="black",fg="yellow", command = lambda : clicked())
screen_shot_button.pack()

# to start the GUI window, 'mainloop' method is sed
window.mainloop()
