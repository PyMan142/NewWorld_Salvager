import pydirectinput
from pynput.keyboard import *

keyboard = Controller()

#  ======== settings ========
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.backspace
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause
    
    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")

def display_controls():
    print("Salvager is running")
    print("- Controls:")
    print("\t f1 = Resume")
    print("\t f2 = Pause")
    print("\t backspace = Exit")
    print("-----------------------------------------------------")
    print('Press f1 to start ...')

def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pydirectinput.keyDown('s')
            pydirectinput.click()
            pydirectinput.keyDown('e')
            pydirectinput.keyUp('e')
            pydirectinput.keyUp('s')

    lis.stop()

if __name__ == "__main__":
    main()