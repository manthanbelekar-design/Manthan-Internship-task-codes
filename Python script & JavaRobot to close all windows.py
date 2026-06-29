import pyautogui
import time

# Pause before starting
time.sleep(2)

# Get screen resolution
width, height = pyautogui.size()

print("Screen Width :", width)
print("Screen Height :", height)

# Move mouse to the center of the screen
pyautogui.moveTo(width // 2, height // 2, duration=2)

# Left click
pyautogui.click()

# Draw a small square with the mouse
pyautogui.dragRel(100, 0, duration=0.5, button='left')
pyautogui.dragRel(0, 100, duration=0.5, button='left')
pyautogui.dragRel(-100, 0, duration=0.5, button='left')
pyautogui.dragRel(0, -100, duration=0.5, button='left')

# Minimize all open windows
pyautogui.hotkey('win', 'd')

print("Automation completed.")