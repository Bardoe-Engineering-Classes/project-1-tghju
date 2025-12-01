from machine import ADC, PWM, Pin
import time

potR = ADC(26)
potG = ADC(27)
potB = ADC(28)

red = PWM(Pin(15))
green = PWM(Pin(14))
blue = PWM(Pin(13))

red.freq(1000)
green.freq(1000)
blue.freq(1000)

while True:
    readingR = potR.read_u16()
    red.duty_u16(readingR)
    readingG = potG.read_u16()
    green.duty_u16(readingG)
    readingB = potB.read_u16()
    blue.duty_u16(readingB)
    time.sleep(0.01)
