from machine import ADC, PWM, Pin
import time

# setting pots (pots are on bottom right of breadboard for spacing)
potR = ADC(26) # GP26 = ADC0
potG = ADC(27) # GP27 = ADC1
potB = ADC(28) # GP28 = ADC2

# LEDs are on top left of breadboard, except blue resistor (right side) due to space
red = PWM(Pin(15)) # red color is marked as orange wire (red is power, black for ground)
green = PWM(Pin(14)) # green wire
blue = PWM(Pin(13)) # blue wire

red.freq(1000)
green.freq(1000)
blue.freq(1000)

# potInClass for potentiometer code, RGBLedTesting branch for LED code
while True:
    readingR = potR.read_u16()
    red.duty_u16(readingR)
    readingG = potG.read_u16()
    green.duty_u16(readingG)
    readingB = potB.read_u16()
    blue.duty_u16(readingB)
    time.sleep(0.01)
