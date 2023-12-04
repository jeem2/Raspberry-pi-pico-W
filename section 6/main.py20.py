from machine import Pin, I2C        #importing relevant modules & classes
from time import sleep
import utime
import socket
import network
import bme280                       #importing BME280 library
 
i2c=I2C(0,sda=Pin(20), scl=Pin(21), freq=400000)    #initializing the I2C method
 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("**********","**********")
 
def web_page():
    bme = bme280.BME280(i2c=i2c)          #BME280 object created
    html = """<html><head><meta http-equiv="refresh" content="5"><meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"><style>body { text-align: center; font-family: "Helvetica", Arial;}
  table { border-collapse: collapse; width:55%; margin-left:auto; margin-right:auto; }
  th { padding: 12px; background-color: #87034F; color: white; }
  tr { border: 2px solid #000556; padding: 12px; }
  tr:hover { background-color: #bcbcbc; }
  td { border: none; padding: 14px; }
  .sensor { color:DarkBlue; font-weight: bold; background-color: #ffffff; padding: 1px;  
  </style></head><body><h1>BME280 Pi Pico W Weather Station</h1>
  <table><tr><th>Parameters</th><th>Value</th></tr>
  <tr><td>Temperature</td><td><span class="sensor">""" + str(bme.values[0]) + """</span></td></tr>
  <tr><td>Pressure</td><td><span class="sensor">""" + str(bme.values[1]) + """</span></td></tr>
  <tr><td>Humidity</td><td><span class="sensor">""" + str(bme.values[2]) + """</span></td></tr> 
  
  <head><meta http-equiv="refresh" content="5"><meta name="viewport" content="width=device-width, initial-scale=1"><style>img{display: block; margin-left: auto; margin-right: auto;}</style></head><body><img src="data:image/jpeg;base64,/9j/  </body></html>"""

    return html
  
# Wait for connect or fail
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(1)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('wifi connection failed')
else:
    print('connected')
    ip=wlan.ifconfig()[0]
    print('IP: ', ip)
    
# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 80))
server.listen(5)
print('listening on', addr)
    
while True:
    try:
        conn, addr = server.accept()
        conn.settimeout(3.0)
        print('client connected from', addr)
        request = conn.recv(1024)
        conn.settimeout(None)
        # HTTP-Request receive
        print('Request:', request)              
        # HTTP-Response send
        response = web_page()
        conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print('connection closed')
