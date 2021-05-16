import time
import pigpio
import serial

port = '/dev/ttyACM0'
brate = 250000

arduino = serial.Serial(port, brate)
print('통신시작')

left = arduino.readline().decode()
right = arduino.readline().decode()
print("left: ", left, " right:", right)

pi = pigpio.pi()

pi.set_servo_pulsewidth(19, left)
pi.set_servo_pulsewidth(15, right)
time.sleep(0.2)

      