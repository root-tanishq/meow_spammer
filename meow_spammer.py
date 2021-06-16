import os, pyautogui, time
command = input("Please enter the spam line or word:- ")
print("switch to the app within next 10 seconds")
time.sleep(10)
print("Here we go!!!")
while True:
       pyautogui.typewrite(command)
       pyautogui.press("enter")
