let Lightmeter = 0
let teplota = 0
input.onButtonPressed(Button.A, function () {
    radio.sendValue("teplota", input.temperature())
})
input.onButtonPressed(Button.B, function () {
    Lightmeter = input.lightLevel()
    basic.showNumber(Lightmeter)
    if (Lightmeter == Math.constrain(Lightmeter, 129, 255)) {
        basic.showString("Save")
    }
})
radio.onReceivedValue(function (name, value) {
    teplota = input.temperature()
    radio.sendValue("RadioSV", input.temperature())
    if (true) {
        basic.showNumber(input.temperature())
    } else {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    }
})
radio.onReceivedValue(function (RadioSV, value2) {
    basic.showNumber(input.temperature())
})
