import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import time, datetime

keyboard = Controller()
# # h = input("when you want to sent message hours:")
h = datetime.datetime.now().hour
# print(h, type(h))
m = datetime.datetime.now().minute + 2
# print(m, type(m))
# print(*dir(datetime.time), sep='\n')
# m = input("minutes:")
for x in range(5):
    pywhatkit.sendwhatmsg('+380505953204', f'Получилось! {h}:{str(m)}', h, m)
    pyautogui.click()

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)

    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)
    time.sleep(1)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    print("Message Send Successfully")
    m = int(m) + 1



