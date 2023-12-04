from picozero import Speaker
from time import sleep


speaker = Speaker(15)


while True:
    speaker.on()
    sleep(1)
    speaker.off()
    sleep(1)