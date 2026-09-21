


import pyautogui
import time

x = 1834
y = 525

print("Script started!")
print("Har 30 seconds mein Retry button par DOUBLE CLICK hoga.")

# Steam window par jaane ke liye 5 seconds
time.sleep(5)

while True:
    # Cursor Retry button par le jao
    pyautogui.moveTo(x, y, duration=0.5)

    time.sleep(0.5)

    # ===== FIRST CLICK =====
    pyautogui.mouseDown(button="left")
    time.sleep(0.2)
    pyautogui.mouseUp(button="left")

    # Click ke beech gap
    time.sleep(0.3)

    # ===== SECOND CLICK =====
    pyautogui.mouseDown(button="left")
    time.sleep(0.2)
    pyautogui.mouseUp(button="left")

    print("Double click sent:", time.strftime("%H:%M:%S"))

    # 30 seconds wait
    time.sleep(30)


############################

# import pyautogui
# import time

# # Steam Retry button position
# x = 1834
# y = 525

# print("Auto Retry Clicker Started!")
# print("Har 30 sec mein Retry button click hoga.")
# print("Stop karne ke liye Ctrl + C dabao.")

# while True:
#     pyautogui.click(x, y)
#     print("Retry button clicked:", time.strftime("%H:%M:%S"))

#     time.sleep(30)
