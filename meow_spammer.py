import pyautogui, time
#install pyautogui by running pip install pyautogui
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(
f"{bcolors.HEADER}----------------------------------------------------------------------{bcolors.ENDC}\n"
f"{bcolors.WARNING}                               MEOW-SPAMMER                           {bcolors.ENDC}\n"
f"{bcolors.HEADER}----------------------------------------------------------------------{bcolors.ENDC}\n"
)
command_meow = input(f"{bcolors.OKGREEN}Please enter the spam line or word:- {bcolors.ENDC}")
print(f"{bcolors.HEADER}----------------------------------------------------------------------{bcolors.ENDC}\n")
loop_meow = int(input(f"{bcolors.OKGREEN}Please enter the no. of time you want to run loop [0 for non stopable]:- {bcolors.ENDC}"))
print(f"{bcolors.HEADER}----------------------------------------------------------------------{bcolors.ENDC}\n")
delay_meow = int(input(f"{bcolors.OKGREEN}Delay while sending messages[0 for no delay]:- {bcolors.ENDC}"))
print(f"{bcolors.HEADER}----------------------------------------------------------------------{bcolors.ENDC}\n")
print(f"{bcolors.FAIL}switch to the app within next 10 seconds{bcolors.ENDC}")
time.sleep(10)
print(f"{bcolors.HEADER}----------------------------------------------------------------------{bcolors.ENDC}\n")
print(f"{bcolors.OKBLUE}Here we go!!!{bcolors.ENDC}")
while True:
       if loop_meow == 0:
              while True:
                      pyautogui.typewrite(command_meow)
                      pyautogui.press("enter")
                      time.sleep(delay_meow)
       else:
              for i in range(loop_meow):
                     pyautogui.typewrite(command_meow)
                     pyautogui.press("enter")
                     time.sleep(delay_meow)
              break
print(f"{bcolors.HEADER}----------------------------------------------------------------------{bcolors.ENDC}\n")
