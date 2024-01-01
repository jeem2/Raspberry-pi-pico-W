from machine import Pin,PWM
import utime as t
import random as r
Led_R = PWM(Pin(20))
Led_G = PWM(Pin(18))
Led_B = PWM(Pin(16))
# Define the frequency
Led_R.freq(1000)   
Led_G.freq(1000)   
Led_B.freq(1000)   
if __name__ == "__main__":
    while True:
        # range of random numbers
        R=r.randint(0,65535)      
        G=r.randint(0,06535)
        B=r.randint(0,65535)
        print(R,G,B)   
        Led_R.duty_u16(R)
        Led_G.duty_u16(G)
        Led_B.duty_u16(B) 
        t.sleep_ms(1000)
  
