def Turn(turnFactor: number):
    qdee.qdee_setMotorSpeed(turnFactor * -1, turnFactor)
    if turnFactor > 0:
        basic.show_leds("""
            . . # . .
            . # . . .
            # . . . .
            . # . . .
            . . # . .
            """)
    elif turnFactor < 0:
        basic.show_leds("""
            . . # . .
            . . . # .
            . . . . #
            . . . # .
            . . # . .
            """)
    else:
        basic.show_leds("""
            . . # . .
            . # . # .
            # . . . #
            . # . # .
            . . # . .
            """)
def DribbleDir(num: number):
    qdee.qdee_setBusServo(qdee.busServoPort.PORT10, 1, num, 0)
def SensorLogic(MinDist: number):
    if qdee.qdee_ultrasonic(qdee.ultrasonicPort.PORT2) < MinDist:
        return 1
    else:
        return 0
def Throttle(value: number):
    qdee.qdee_setMotorSpeed(value, value)
    if value > 0:
        basic.show_leds("""
            . . # . .
            . # . # .
            # . . . #
            . . . . .
            . . . . .
            """)
    elif value < 0:
        basic.show_leds("""
            . . . . .
            . . . . .
            # . . . #
            . # . # .
            . . # . .
            """)
    else:
        basic.show_leds("""
            . . # . .
            . # . # .
            # . . . #
            . # . # .
            . . # . .
            """)

def on_received_value(name, value2):
    if name == "Dribble":
        DribbleDir(value2)
    if name == "Throttle":
        Throttle(value2)
    elif name == "Turn":
        Turn(value2)
radio.on_received_value(on_received_value)

qdee.qdee_Init()
radio.set_group(9021)
basic.show_leds("""
    . . . . .
    . # # # .
    . # # # .
    . # # # .
    . . . . .
    """)
