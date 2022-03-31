Lightmeter = 0
teplota = 0

def on_button_pressed_a():
    radio.send_value("teplota", input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Lightmeter
    Lightmeter = input.light_level()
    basic.show_number(Lightmeter)
    if Lightmeter == Math.constrain(Lightmeter, 129, 255):
        basic.show_string("Save")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    global teplota
    teplota = input.temperature()
    radio.send_value("RadioSV", input.temperature())
    if True:
        basic.show_number(input.temperature())
    else:
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . #
        """)
radio.on_received_value(on_received_value)

def on_received_value2(RadioSV, value2):
    basic.show_number(input.temperature())
radio.on_received_value(on_received_value2)
