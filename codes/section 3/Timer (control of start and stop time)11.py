from machine import Pin, Timer
import tm1637

tm = tm1637.TM1637(clk=Pin(14), dio=Pin(15))
button_pin = 13

counter_ms = 0
running = False

def setup():
    global button
    button = Pin(button_pin, Pin.IN, Pin.PULL_UP)
    button.irq(trigger=Pin.IRQ_RISING, handler=button_isr)
    
def button_isr(pin):
    global running
    running = not running

def display_time(timer):
    global counter_ms
    if running:
        tm.number(counter_ms)
        counter_ms += 1

def loop():
    timer = Timer(freq=100, mode=Timer.PERIODIC, callback=display_time)
    while True:
        pass

if __name__ == '__main__':
    setup()
    loop()
