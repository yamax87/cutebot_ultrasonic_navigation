sonar2 = 0

def on_gesture_screen_down():
    cuteBot.stopcar()
    while True:
        basic.show_leds("""
            . . . . .
            # # # # .
            . . # . .
            . # . . .
            # # # # .
            """)
        control.wait_micros(500)
        basic.show_leds("""
            . # # # #
            . . . # .
            . . # . .
            . # # # #
            . . . . .
            """)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_logo_pressed():
    global sonar2
    basic.show_leds("""
        . . . . .
        . # . # .
        . . # . .
        # . . . #
        . # # # .
        """)
    soundExpression.hello.play()
    control.wait_micros(1000)
    while True:
        sonar2 = cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS)
        cuteBot.color_light(cuteBot.RGBLights.ALL, 0x00ff00)
        if sonar2 > 0.01 and sonar2 < 100:
            cuteBot.motors(-100, 100)
            cuteBot.color_light(cuteBot.RGBLights.ALL, 0xff0000)
        else:
            cuteBot.motors(100, 100)
            cuteBot.color_light(cuteBot.RGBLights.ALL, 0x00ffff)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)
