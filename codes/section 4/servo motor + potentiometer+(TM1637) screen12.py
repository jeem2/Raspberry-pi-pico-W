from machine import Pin, PWM, ADC
import utime as t
import tm1637

pot=ADC(0)
servo1=PWM(Pin(15))
servo1.freq(50)
#inicializar leds
ledh=Pin(18,Pin.OUT)
ledm=Pin(19,Pin.OUT)
ledl=Pin(20,Pin.OUT)


tm= tm1637.TM1637(clk=Pin(1), dio=Pin(0))
tm.brightness(2)
while 1:
    valor=int(1638+(pot.read_u16()/10)) #65535/(8191-1638)
    servo1.duty_u16(valor)
    tm.number(int(valor))
    if (valor>1638 and valor<1830):
        ledh.value(1)   #valor bajo
        ledm.value(0)   #valor medio
        ledl.value(0)   #valor bajo
    if (valor>=1830 and valor<3944):
        ledm.value(1)   #valor medio
        ledh.value(0)   #valor bajo
        ledl.value(0)   #valor bajo
    if (valor>=3944 and valor<8192):
        ledl.value(1)   #valor bajo
        ledh.value(0)   #valor bajo
        ledm.value(0)   #valor medio

    print (valor)
    t.sleep(.3)