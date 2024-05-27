import machine
import time

# Define the servo pin
servo_pin = 15

# Set PWM parameters
pwm_freq = 50  # PWM frequency in Hz
pulse_width_open = 0.5  # Pulse width for open position (in ms)
pulse_width_closed = 1.5  # Pulse width for closed position (in ms)

# Initialize PWM pin
pwm = machine.PWM(servo_pin, freq=pwm_freq)

def open_gripper():
    # Set PWM pulse width for open position
    pwm.duty_u16(int(65535 * pulse_width_open / 10))

def close_gripper():
    # Set PWM pulse width for closed position
    pwm.duty_u16(int(65535 * pulse_width_closed / 12))

# Open the gripper
open_gripper()
time.sleep(2)

# Close the gripper
close_gripper()
time.sleep(2)