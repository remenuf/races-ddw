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

keyboard.add_hotkey("f8", macro)  # Bind macro to F8
print("Macro running. Press F8 to execute.")
keyboard.wait("esc")  # Keeps the script running until Esc is pressed