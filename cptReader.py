import os
# corss platform tts engine
# https://pypi.python.org/pypi/pyttsx3/2.6
import pyttsx3
# cross platform clipboard
# https://pypi.python.org/pypi/clipboard/0.0.4
import clipboard
# maybe platform issue keyboard
# https://pypi.python.org/pypi/pynput
from pynput.keyboard import Key, Controller, Listener
# pynput could also be used for shortcuts/hotkeys
# cross platform shortcuts/hotkeys
# https://pypi.python.org/pypi/PyGlobalShortcut
## can't get this working.

engine = pyttsx3.init()
keyboard = Controller()

def onWord(*args, **kwargs):
   print (self, args, kwargs)
   if location > 10:
      engine.stop()

engine = pyttsx3.init()
engine.connect('started-word', onWord)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

def read():
    old_clipboard = clipboard.paste()
    with keyboard.pressed(Key.ctrl):
        keyboard.press('c')
        keyboard.release('c')
    engine.say(clipboard.paste())
    clipboard.copy(old_clipboard)
    engine.runAndWait()

def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.alt_l:
        # read
        read()
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()
