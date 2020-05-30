import pyautogui
import time

i=0
while(i < 30):
	print(pyautogui.position())
	i+=1
	time.sleep(1)