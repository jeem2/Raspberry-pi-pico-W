from machine import ADC
from time import sleep


adcpin = 26
pot = ADC(adcpin)


while True:
    adc_value = pot.read_u16()
    print(adc_value)
   
    volt = (3.3/65535)*adc_value
    print(round(volt,2))
   
    sleep(1)