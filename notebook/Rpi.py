import time
import pigpio
import serial

port = '/dev/ttyACM0'
brate = 9600
cmd = 'temp'

seri = serial.Serial(port, baudrate = brate, timeout= None)
print(seri.name)

seri.write(cmd.encode())

while 1:
    if seri.in_waiting != 0:
        content = seri.readline()
        print(content.decode())
        

pi = pigpio.pi()
pi.set_servo_pulsewidth(19, 1400)
pi.set_servo_pulsewidth(15, 1400)
time.sleep(0.2)

