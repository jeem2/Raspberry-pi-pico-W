import machine as m
import utime as t

sensor_pir = m.Pin(28,m.Pin.IN)
led = m.Pin(15, m.Pin.OUT)
buzzer = m.Pin(14, m.Pin.OUT)

def pir_handler(pin):
    print("ALARM! Motion detected!")
    for i in range (50):
        led. toggle()
        buzzer.toggle()
        t.sleep_ms(200)
        
sensor_pir.irq(trigger=machine.Pin.IRQ_RISING,handler=pir_handler)

while True:
    led.toggle()
    t.sleep(5)