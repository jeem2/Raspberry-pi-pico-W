import machine as m
import utime as t
RLED = m.Pin(1,m.Pin.OUT)
YLED = m.Pin(5,m.Pin.OUT)
GLED = m.Pin(9,m.Pin.OUT)
while 1 : 
  RLED.value(1)
  t.sleep(2)
  RLED.value(0)
  YLED.value(1)
  t.sleep(2)
  YLED.value(0)
  GLED.value(1)
  t.sleep(2)
  GLED.value(0)