
import time
import board
import digitalio

button = digitalio.DigitalInOut(board.GP13)

led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT


while True:
    if button.value==True:
        
