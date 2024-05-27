

import time
import board
import digitalio
import pulseio
import simpleio
import busio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

sen_S0 = digitalio.DigitalInOut(board.GP14)
sen_S0.direction = digitalio.Direction.OUTPUT

sen_S1 = digitalio.DigitalInOut(board.GP15)
sen_S1.direction = digitalio.Direction.OUTPUT

sen_S2 = digitalio.DigitalInOut(board.GP17)
sen_S2.direction = digitalio.Direction.OUTPUT

sen_S3 = digitalio.DigitalInOut(board.GP16)
sen_S3.direction = digitalio.Direction.OUTPUT

sen_OUT = pulseio.PulseIn(board.GP18, idle_state=True)


# Set output frequency scaling to 20%
sen_S0.value = True
sen_S1.value = False

color = "NONE"
prev_color = ""

while True:
    sen_S2.value = False
    sen_S3.value = False

    time.sleep(0.01)

    # Wait for an active pulse
    while len(sen_OUT) == 0:
        pass

    sen_OUT.pause() # Pause while we do something with the pulses

    red_freq = sen_OUT[0]
    red_color = simpleio.map_range(red_freq, 100, 530, 100, 0)

    sen_OUT.clear()
    sen_OUT.resume()

    sen_S2.value = True
    sen_S3.value = True

    time.sleep(0.01)

    # Wait for an active pulse
    while len(sen_OUT) == 0:
        pass

    # Pause while we do something with the pulses
    sen_OUT.pause()

    green_freq = sen_OUT[0]
    green_color = simpleio.map_range(green_freq, 150, 700, 100, 0)

    sen_OUT.clear()
    sen_OUT.resume()

    sen_S2.value = False
    sen_S3.value = True

    time.sleep(0.01)

    # Wait for an active pulse
    while len(sen_OUT) == 0:
        pass

    # Pause while we do something with the pulses
    sen_OUT.pause()

    blue_freq = sen_OUT[0]
    blue_color = simpleio.map_range(blue_freq, 70, 600, 100, 0)

    #print("{}\t{}\t{}".format(red_freq, green_freq, blue_freq))
    #print("{}\t{}\t{}".format(int(red_color), int(green_color), int(blue_color)))
    print(f"Red: {red_color}, Blue: {blue_color}, Green: {green_color}")

    if red_color < 50 and green_color < 50 and blue_color < 50:
        color = "none"
    elif red_color > green_color and \
         red_color > blue_color:
        color = "RED  "
    elif green_color > red_color and \
         green_color > blue_color:
        color = "GREEN"
    elif blue_color > green_color and \
         blue_color > red_color:
        color = "BLUE "

    if color != prev_color:
        prev_color = color

        print(color)
       

    time.sleep(0.1)

    sen_OUT.clear()
    sen_OUT.resume()