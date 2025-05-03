import mido
from pynput import keyboard

controls = mido.open_input(mido.get_input_names()[1])

with controls:
    for msg in controls:
        print(msg)