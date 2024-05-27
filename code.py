import time
import board
import pwmio,busio,displayio, os, terminalio, microcontroller
from digitalio import DigitalInOut, Direction
import digitalio
from adafruit_motor import servo
from lcd.lcd import LCD, CursorMode
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface


ir_sensor_pin = board.GP0
ir_sensor = digitalio.DigitalInOut(ir_sensor_pin)
ir_sensor.direction = digitalio.Direction.INPUT

ir_sensor_pin2 = board.GP1
ir_sensor2 = digitalio.DigitalInOut(ir_sensor_pin2)
ir_sensor2.direction = digitalio.Direction.INPUT

in1 = DigitalInOut(board.GP11)
in1.direction = Direction.OUTPUT
in2 = DigitalInOut(board.GP12)
in2.direction = Direction.OUTPUT
pwm_a = pwmio.PWMOut(board.GP13, frequency=100, duty_cycle=0)

pwm_servo = pwmio.PWMOut(board.GP14, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(
    pwm_servo, min_pulse=500, max_pulse=2200
)
pwm_servo = pwmio.PWMOut(board.GP15, duty_cycle=2 ** 15, frequency=50)
servo2 = servo.Servo(
    pwm_servo, min_pulse=500, max_pulse=2200
)

 


def gear_forward():
    in1.value = False
    in2.value = True
    pwm_a.duty_cycle = 0x7FFF

def gear_stop():
    time.sleep(1)
    in1.value = False
    in2.value = False
    pwm_a.duty_cycle = 0
    time.sleep(2)  # Delay for 3 seconds

def gripo_open():
    #print("servo test: 90")
    #servo1.angle = 90
    #time.sleep(1)
    print("servo test: 0")
    servo1.angle = 0
    time.sleep(0.1)
    gear_stop()
    time.sleep(0.7)
    print("servo test: 90")
    servo1.angle = 90
    time.sleep(0.2)
    print("servo test: 180")
    servo1.angle = 180
    time.sleep(0.5)
   

def gripo_close():
  
    servo1.angle = 180
    time.sleep(0.3)

    servo1.angle = 0
    time.sleep(0.2)
    
def servo_default():
    print("servo test: 90")
    servo2.angle = 90
    time.sleep(0.2)
    print("servo test: 90")
    servo2.angle = 90
    time.sleep(0.3)
    gripo_close()
    print("servo test: 180")
    servo2.angle = 180
    time.sleep(0.5)
def servo_box():
    print("servo test: 90")
    servo2.angle = 90
    time.sleep(0.4)
    print("servo test: 0")
    servo2.angle = 0
    time.sleep(0.3)
    print("servo test: 90")
    servo2.angle = 90
    time.sleep(0.5)
    print("servo test: 180")
    servo2.angle = 180
    time.sleep(0.5)
    


while True:
    if ir_sensor.value == False:
        
        gear_stop()
    elif ir_sensor2.value == False:
        gripo_open()
        time.sleep(1)
        
       
        servo_default()
        
    gear_forward()

