import pyautogui
import time

time.sleep(5)
# Open the wordlist file with utf-8 encoding and read all lines
with open('wordlist.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Loop through each line and type it with a 1-second interval
for line in lines:
    pyautogui.write(line.strip())  # Type the line (strip removes any extra newline)
    pyautogui.press('enter')       # Press enter after typing the line
    time.sleep(1)                  # Wait for 1 second before typing the next line
