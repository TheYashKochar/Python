# Program to automate mouse
import pyautogui
width, height = pyautogui.size()
print(pyautogui.position())
pyautogui.moveTo(10,10)
pyautogui.moveTo(100,100, duration = 1.5)
pyautogui.moveRel(200,0, duration=2)
pyautogui.moveRel(0,-50, duration=2)
pyautogui.click(0,1074)
#print(pyautogui.displayMousePostion())
