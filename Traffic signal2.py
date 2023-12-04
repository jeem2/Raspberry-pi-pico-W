import machine
import utime
ledRed = machine.Pin(1,machine.Pin.OUT)
ledAmber = machine.Pin(5,machine.Pin.OUT)
ledGreen = machine.Pin(9,machine.Pin.OUT)


while 1 :
  ledRed.value(1)
  utime.sleep(2)
  ledRed.value(0)
  ledAmber.value(1)
  utime.sleep(2)
  ledAmber.value(0)


  ledGreen.value(1)
  utime.sleep(2)
  ledGreen.value(0)