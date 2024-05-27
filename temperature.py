import board

import busio,displayio, os, terminalio, microcontroller

import time

from lcd.lcd import LCD, CursorMode

from lcd.i2c_pcf8574_interface import I2CPCF8574Interface



# Pin definitions

# I2C used for LCD Display

i2c_scl = board.GP2

i2c_sda = board.GP3

i2c_address = 0x27 # 39 decimal



# LCD display info

cols = 16

rows = 2



# Setup LCD display

i2c = busio.I2C(scl=i2c_scl, sda=i2c_sda)

interface = I2CPCF8574Interface(i2c, i2c_address)

lcd = LCD(interface, num_rows=rows, num_cols=cols)

lcd.set_cursor_mode(CursorMode.HIDE)





def main ():
    temperature = 0
    temperature_value_label=1
    temperature_string = f"{temperature}°C"
    temperature_label=1
    temperature =  round(microcontroller.cpu.temperature,1)
    temperature_string = f"{temperature}°C"
    while True:
        
        
        lcd.print(f"    {temperature_string}")
        print(f"    {temperature_string}")
        time.sleep(2)
        lcd.clear()
        time.sleep(1)
    time.sleep(1)
'''
    ADC_voltage = adc.read_u16() * (3.3 / (65536))
    temperature_celcius = 27 - (ADC_voltage - 0.706)/0.001721
    temp_fahrenheit=32+(1.8*temperature_celcius)
    print("Temperature: {}°C {}°F".format(temperature_celcius,temp_fahrenheit))
    time.sleep_ms(500)
    
    lcd.clear()

    lcd.print ("      lol")

    time.sleep (2)

    lcd.clear()

    lcd.print ("About to start\nthe timer")

    time.sleep (2)
    count = 0

    while True:

        lcd.clear()

        lcd.print ("Counting:\n"+str(count))

        count += 1

        time.sleep(1)
'''



if __name__ == '__main__':

    main()