#WhatApp Desktop App mensage sender

import pyautogui as pg
import time
print(pg.position())

screenWidth, screenHeight = pg.size() # Get the size of the primary monitor.

currentMouseX, currentMouseY = pg.position() # Get the XY position of the mouse.

pg.moveTo(471, 1063) # Move the mouse to XY coordinates.
pg.click()          # Click the mouse.
time.sleep(10)     # makes program execution pause for 10 sec
pg.moveTo(38, 244)      # Move the mouse to XY coordinates.
pg.click(38, 244)  # Move the mouse to XY coordinates and click it. """
time.sleep(3)   # makes program execution pause for 3 sec
pg.write('Bom dia Lindinha!!', interval=0.20)  # type with quarter-second pause in between each key
pg.press('enter')     # Press the enter key. All key names are in pyautogui.KEY_NAMES


""" pyautogui.click('button.png') # Find where button.png appears on the screen and click it.
pyautogui.doubleClick()    # Double click the mouse.
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.
pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES
pyautogui.keyDown('shift') # Press the Shift key down and hold it.
pyautogui.press(['left', 'left', 'left', 'left']) # Press the left arrow key 4 times.
pyautogui.keyUp('shift')   # Let go of the Shift key.
pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.
pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked. """