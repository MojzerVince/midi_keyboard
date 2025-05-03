import mido

#print(mido.get_input_names())  # List all available MIDI input devices

keyboard = mido.open_input(mido.get_input_names()[0]) #billentyűk

with keyboard:
    for msg in keyboard:
        print(msg)