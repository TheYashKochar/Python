# Program to Search Something in Windows OS
import pyautogui
key = input('Enter the Search Material : ')#.split()
#Using UELI/PowerToys
#pyautogui.hotkey('alt','space')
#Using Windows Search
pyautogui.hotkey('win','s')
pyautogui.typewrite(key)
