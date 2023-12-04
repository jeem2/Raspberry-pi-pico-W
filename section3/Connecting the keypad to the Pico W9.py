import rp2
from rp2 import PIO
from machine import Pin
from time import sleep


@rp2.asm_pio(set_init=[PIO.IN_HIGH]*4)
def keypad():
    wrap_target()
    set(y, 0)                             
    label("1")
    mov(isr, null)                        
    set(pindirs, 1)                       
    in_(pins, 4)                          
    set(pindirs, 2)                       
    in_(pins, 4)                          
    set(pindirs, 4)                       
    in_(pins, 4)                          
    set(pindirs, 8)                       
    in_(pins, 4)                          
    mov(x, isr)                           
    jmp(x_not_y, "13")                    
    jmp("1")                              
    label("13")
    push(block)                           
    irq(0)
    mov(y, x)                             
    jmp("1")                              
    wrap()


for i in range(10, 14):
  Pin(i, Pin.IN, Pin.PULL_DOWN)


key_names = "*7410852#963DCBA"


def oninput(machine):
  keys = machine.get()
  while machine.rx_fifo():
      keys = machine.get()
  pressed = []
  for i in range(len(key_names)):
      if (keys & (1 << i)):
          pressed.append(key_names[i])
  print("Keys changed! pressed keys:", pressed)
 
sm = rp2.StateMachine(0, keypad, freq=2000, in_base=Pin(10, Pin.IN, Pin.PULL_DOWN), set_base=Pin(6))
sm.active(1)
sm.irq(oninput)


print("Please press any key on the keypad, or press Ctrl+C to enter REPL.")
while True:
  sleep(0.1)