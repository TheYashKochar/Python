# Program to take Screenshots in certain time frame
import pyautogui,time
ssnum = int(input('Enter the Number of Screenshots : '))
dtime = int(input('Enter the Delay Time : '))
for x in range(ssnum):
    pyautogui.screenshot()
    pyautogui.screenshot(str(x+1) + '.png')
    time.sleep(5)
print('Done')
