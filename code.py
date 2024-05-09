#Import all the relevant Libraries

import time
import board
import digitalio
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Set up Consumer Control - Control Codes can be found here: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/consumer_control_code.html#ConsumerControlCode
cc = ConsumerControl(usb_hid.devices)

# Set up a keyboard device. - Keycode can be found here: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html#Keycode
keyboard = Keyboard(usb_hid.devices)

# Set up keyboard to write strings from macro
write_text = KeyboardLayoutUS(keyboard)



btn1_pin = board.GP15
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2_pin = board.GP14
btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3_pin = board.GP10
btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4_pin = board.GP12
btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5_pin = board.GP11
btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

while True:
    
    
    # Keycode class defines USB HID keycodes to send using Keyboard.  
    if btn1.value:
        #print("1")
        keyboard.send(Keycode.GRAVE_ACCENT)
        time.sleep(0.4)
        write_text.write('offroad')
        time.sleep(0.4)
        keyboard.send(Keycode.ENTER)
        time.sleep(0.4)
        #keyboard.release_all()
        
    #The ConsumerControl class emulates consumer control devices such as remote controls, or the multimedia keys on certain keyboards.    
    if btn2.value:
        #print("2")
        keyboard.send(Keycode.GRAVE_ACCENT)
        time.sleep(0.4)
        write_text.write('turtle')
        time.sleep(0.4)
        keyboard.send(Keycode.ENTER)
        time.sleep(0.4)
        #keyboard.release_all()

    #KeyboardLayoutUS class which allow us to send ASCII characters    
    if btn3.value:
        #print("3")
        keyboard.send(Keycode.GRAVE_ACCENT)
        time.sleep(0.4)
        write_text.write('toolup')
        time.sleep(0.4)
        keyboard.send(Keycode.ENTER)
        time.sleep(0.4)
        #keyboard.release_all()

    #combination of different classes
    if btn4.value:
        #print("4")
        keyboard.send(Keycode.GRAVE_ACCENT)
        time.sleep(0.4)
        write_text.write('RAPIDGT')
        time.sleep(0.4)
        random_choice = random.choice(['RAPIDGT', 'COMET'])
        write_text.write(random_choice)
        time.sleep(0.4)
        #keyboard.release_all()
        
    if btn5.value:
        #print("5")
        keyboard.send(Keycode.GRAVE_ACCENT)
        time.sleep(0.4)
        write_text.write('lawyerup')
        time.sleep(0.4)
        keyboard.send(Keycode.ENTER)
        time.sleep(0.4)
        #keyboard.release_all()
    
    time.sleep(0.1)
