import mido
from pynput.keyboard import Key, Controller

controls = mido.open_input(mido.get_input_names()[1])
keyboard = Controller()

with controls:
    for msg in controls:
        #note_on channel=0 note=96 velocity=127 time=0
        #note_on channel=0 note=97 velocity=127 time=0
        if str(msg) == 'note_on channel=0 note=96 velocity=127 time=0': #up
            keyboard.press(Key.up)
            print('up')
        elif str(msg) == 'note_on channel=0 note=97 velocity=127 time=0': #down
            keyboard.press(Key.down)
            print('down')
        print(msg)