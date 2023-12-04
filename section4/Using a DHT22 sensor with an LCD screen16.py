from machine import I2C, Pin
from time import sleep
from dht import DHT22
from pico_i2c_lcd import I2cLcd

dht = DHT22(Pin(15))

i2c = I2C(0,scl=Pin(5), sda=Pin(4), freq=100000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
 
while True:
    dht.measure()
    temp = dht.temperature()
    hum = dht.humidity()
    print("Temperature: {}°C   Humidity: {:.0f}% ".format(temp, hum))

    lcd.clear()
    lcd.putstr('Temp: ' + str(temp) + " C")
    lcd.move_to(0,1)
    lcd.putstr('Hum: ' + str(hum) + "%")

    sleep(2)