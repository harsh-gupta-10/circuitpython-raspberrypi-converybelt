import time
import board
import pwmio
from digitalio import DigitalInOut, Direction

# Motor A
in1 = DigitalInOut(board.GP11)
in1.direction = Direction.OUTPUT
in2 = DigitalInOut(board.GP12)
in2.direction = Direction.OUTPUT
pwm_a = pwmio.PWMOut(board.GP13, frequency=100, duty_cycle=0)

# Motor B

def forward():
    in1.value = True
    in2.value = False
    pwm_a.duty_cycle = 0x7FFF  # PWM duty cycle (0-65535)


def backward():
    in1.value = False
    in2.value = True
    pwm_a.duty_cycle = 0x7FFF

  

def stop():
    in1.value = False
    in2.value = False
    pwm_a.duty_cycle = 0

    

# Move forward for 2 seconds
forward()
time.sleep(20)

# Stop for 1 second
stop()
time.sleep(1)

# Move backward for 2 seconds
backward()
time.sleep(2)

# Stop
stop()
