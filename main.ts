let sonar2 = 0
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showLeds(`
        . . . . .
        . # . # .
        . . # . .
        # . . . #
        . # # # .
        `)
    soundExpression.hello.play()
    control.waitMicros(2000000)
    while (true) {
        sonar2 = cuteBot.ultrasonic(cuteBot.SonarUnit.Centimeters)
        cuteBot.colorLight(cuteBot.RGBLights.ALL, 0x00ff00)
        if (sonar2 > 0.01 && sonar2 < 50) {
            cuteBot.motors(-100, 100)
            cuteBot.colorLight(cuteBot.RGBLights.ALL, 0xff0000)
        } else {
            cuteBot.motors(100, 100)
            cuteBot.colorLight(cuteBot.RGBLights.ALL, 0x00ffff)
        }
    }
})
