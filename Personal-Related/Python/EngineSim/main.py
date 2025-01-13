import os
import keyboard

I = 50  # Inertia constant
rpm = 1000  # Initial RPM
throttle = 0  # Throttle input (0 to 1)
torque_curve = lambda rpm: 160 - 1e-10 * rpm  # Simple torque function

for _ in range(1000000):
    if keyboard.is_pressed("w"):
        throttle = 1
    else:
        throttle = 0.01
    torque = torque_curve(rpm) * throttle
    friction = 0.02 * rpm  # Frictional torque
    net_torque = torque - friction
    alpha = net_torque / I
    rpm += (alpha * 0.016) * (60 / (2 * 3.14159))  # Update RPM
    print(f"Throttle: {throttle}, RPM: {rpm}\r", end="")
