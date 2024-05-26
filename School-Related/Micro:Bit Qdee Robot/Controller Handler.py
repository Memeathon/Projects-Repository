def on_button_pressed_a():
    radio.send_value("Dribble", -40)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_up():
    radio.send_value("Throttle", -100)
    basic.show_leds("""
        . . . . .
        # . . . #
        . # . # .
        . . # . .
        . . . . .
        """)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_tilt_left():
    radio.send_value("Turn", 100)
    basic.show_leds("""
        . # . . .
        . . # . .
        . . . # .
        . . # . .
        . # . . .
        """)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_screen_down():
    radio.send_value("Throttle", 0)
    basic.show_leds("""
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        """)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_button_pressed_ab():
    radio.send_value("Dribble", 0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_value("Dribble", 40)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_right():
    radio.send_value("Turn", -100)
    basic.show_leds("""
        . . . # .
        . . # . .
        . # . . .
        . . # . .
        . . . # .
        """)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_logo_down():
    radio.send_value("Throttle", 100)
    basic.show_leds("""
        . . . . .
        . . # . .
        . # . # .
        # . . . #
        . . . . .
        """)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

radio.set_group(9021)
basic.show_leds("""
    . . . . .
    . # # # .
    . # # # .
    . # # # .
    . . . . .
    """)
