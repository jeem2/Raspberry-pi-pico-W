import utime as t
from servo import Servo as s
 
s1 = s(0)       # Servo pin is connected to GP0
 
def s_Map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 
def s_Angle(angle):
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    s1.goto(round(s_Map(angle,0,180,0,1024))) # Convert range value to angle value
    
if __name__ == '__main__':
    while True:
        print("Turn left ...")
        for i in range(0,180,10):
            s_Angle(i)
            t.sleep(0.05)
        print("Turn right ...")
        for i in range(180,0,-10):
            s_Angle(i)
            t.sleep(0.05)