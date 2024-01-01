import rp2 as r
from rp2 import PIO
from machine import Pin 
from time import sleep as s
# ------ #
# sevseg #
# ------ #

@r.asm_pio(set_init=[PIO.IN_HIGH]*4)
def keypad():
    wrap_target()
    set(y, 0)                             # 0
    label("1")
    mov(isr, null)                        # 1
    set(pindirs, 1)                       # 2
    in_(pins, 4)                          # 3
    set(pindirs, 2)                       # 4
    in_(pins, 4)                          # 5
    set(pindirs, 4)                       # 6
    in_(pins, 4)                          # 7
    set(pindirs, 8)                       # 8
    in_(pins, 4)                          # 9
    mov(x, isr)                           # 10
    jmp(x_not_y, "13")                    # 11
    jmp("1")                              # 12
    label("13")
    push(block)                           # 13
    irq(0)
    mov(y, x)                             # 14
    jmp("1")                              # 15
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
  
sm = r.StateMachine(0, keypad, freq=2000, in_base=Pin(10, Pin.IN, Pin.PULL_DOWN), set_base=Pin(6))
sm.active(1)
sm.irq(oninput)

print("Please press any key on the keypad, or press Ctrl+C to enter REPL.")
while True:
  s(0.1)
