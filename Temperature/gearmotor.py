import time
import board
import pulseio
import pwmio
from adafruit_motor import motor 

# Motor A
in1 = board.GP2
in2 = board.GP3
pwm_a = pwmio.PWMOut(board.GP5)
pwm_b = pwmio.PWMOut(board.GP7)
def forward():
    in1.value = True
    in2.value = False
    pwm_a.duty_cycle = 0x7FFF  # PWM duty cycle (0-65535)

    in3.value = True
    in4.value = False
    pwm_b.duty_cycle = 0x7FFF
    
def backward():
    in1.value = False
    in2.value = True
    pwm_a.duty_cycle = 0x7FFF

    in3.value = False
    in4.value = True
    pwm_b.duty_cycle = 0x7FFF

def stop():
    in1.value = False
    in2.value = False
    pwm_a.duty_cycle = 0

    in3.value = False
    in4.value = False
    pwm_b.duty_cycle = 0

# Move forward for 2 seconds
forward()
time.sleep(2)

# Stop for 1 second
stop()
time.sleep(1)

# Move backward for 2 seconds
backward()
time.sleep(2)

# Stop
stop()