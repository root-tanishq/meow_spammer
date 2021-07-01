import argparse
import pyautogui
import time

#Made with <3 by Boy from future

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--times', type=int,help='No. of times you want to run the spammer(Put 0 for infinite)',default=0)
    parser.add_argument('-s','--spam', type=str ,help='Following line or word you want to spam',required=True)
    parser.add_argument('-d','--delay',type=int,help='delay between sending spam messages',default=0)
    args = parser.parse_args()

print(
f"{bcolors.HEADER}----------------------------------------------------------------------{bcolors.ENDC}\n"
f"{bcolors.WARNING}                               MEOW-SPAMMER                           {bcolors.ENDC}\n"
f"{bcolors.HEADER}----------------------------------------------------------------------{bcolors.ENDC}\n"
)
print(f"{bcolors.FAIL}switch to the app within next 10 seconds{bcolors.ENDC}")
time.sleep(10)
print(f"{bcolors.HEADER}----------------------------------------------------------------------{bcolors.ENDC}\n")
print(f"{bcolors.OKBLUE}Here we go!!!{bcolors.ENDC}")
while True:
       if args.times == 0:
              while True:
                      pyautogui.typewrite(args.spam)
                      pyautogui.press("enter")
                      time.sleep(args.delay)
       else:
              for i in range(args.times):
                     pyautogui.typewrite(args.spam)
                     pyautogui.press("enter")
                     time.sleep(args.delay)
              break
print(f"{bcolors.HEADER}----------------------------------------------------------------------{bcolors.ENDC}\n")

