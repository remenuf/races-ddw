import keyboard
import time

def macro():
    keyboard.write("</b>")  # Type <b>
    time.sleep(0.1)
    keyboard.press_and_release("home")  # Press Home
    time.sleep(0.1)
    keyboard.write("<b>")  # Type <b>
    time.sleep(0.5)
    keyboard.press_and_release("delete")  # Press Delete 4 times
    keyboard.press_and_release("delete")
    keyboard.press_and_release("delete")
    keyboard.press_and_release("delete")

def macro2():
    keyboard.write("</i>")  # Type <b>
    time.sleep(0.1)
    keyboard.press_and_release("left")
    keyboard.press_and_release("left")
    keyboard.press_and_release("left")
    keyboard.press_and_release("left")
    keyboard.press_and_release("left")
    keyboard.press_and_release("left")
    keyboard.press_and_release("left")
    keyboard.press_and_release("left")
    keyboard.press_and_release("left")
    keyboard.press_and_release("left")
    keyboard.press_and_release("left")
    keyboard.press_and_release("left")
    time.sleep(0.1)
    keyboard.write('<i>')  # Type <b>
    time.sleep(0.5)
    keyboard.press_and_release("delete")  # Press Delete 4 times
    keyboard.press_and_release("delete")
    keyboard.press_and_release("delete")
    keyboard.press_and_release("delete")
    keyboard.press_and_release("left")
    keyboard.press_and_release("left")
    keyboard.press_and_release("left")
    time.sleep(0.1)
    keyboard.write("</span>")  # Type <b>
    time.sleep(0.1)
    keyboard.press_and_release("home")  # Press Home
    time.sleep(0.1)
    keyboard.write('<span style="color: #ee4612; font-weight: bold;">')  # Type <b>
    time.sleep(0.5)
    keyboard.press_and_release("delete")  # Press Delete 4 times
    keyboard.press_and_release("delete")
    keyboard.press_and_release("delete")
    keyboard.press_and_release("delete")
    keyboard.press_and_release("delete")
    keyboard.press_and_release("delete")
    keyboard.press_and_release("delete")

keyboard.add_hotkey("f8", macro)  # Bind macro to F8
keyboard.add_hotkey("f7", macro2) 
print("Macro running. Press F8 to execute.")
keyboard.wait("esc")  # Keeps the script running until Esc is pressed