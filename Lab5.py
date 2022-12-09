import pyautogui
import keyboard
import time

def cautare_google():
    if pyautogui.locateOnScreen(r'C:\Proiecte\Inteligenta-Artificiala\Screenshot_1.png', confidence=0.7) != None:
        camp_google=pyautogui.locateOnScreen(r'C:\Proiecte\Inteligenta-Artificiala\Screenshot_1.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(3)
        pyautogui.write("https://www.youtube.com")
        pyautogui.press('enter')
    else:
        print ("Imaginea nu e pe ecran")

time.sleep(3)
cautare_google()

def cautare_youtube():
    if pyautogui.locateOnScreen(r'C:\Proiecte\Inteligenta-Artificiala\Screenshot_2.png', confidence=0.7) != None:
        camp_youtube=pyautogui.locateOnScreen(r'C:\Proiecte\Inteligenta-Artificiala\Screenshot_2.png', confidence=0.7)
        pyautogui.click(camp_youtube)
        time.sleep(5)
        pyautogui.write("https://www.youtube.com/results?search_query=selly")
        pyautogui.press('enter')
    else:
        print ("Imaginea nu e pe ecran")

time.sleep(3)
cautare_youtube()

def coordonate():
   print(pyautogui.position())

time.sleep(3)
coordonate()