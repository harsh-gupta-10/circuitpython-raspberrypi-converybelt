import time
import board
import digitalio

ir_sensor_pin = board.GP0  # Adjust this pin based on your wiring
ir_sensor = digitalio.DigitalInOut(ir_sensor_pin)
ir_sensor.direction = digitalio.Direction.INPUT

while True:
    if ir_sensor.value==False:
        print("IR detected!")
    else:
        print("No IR signal.")
    time.sleep(0.1)  # Adjust the sleep time as needed
