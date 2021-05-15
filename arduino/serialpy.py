import serial

arduino = serial.Serial('COM6', 19200)
print('통신시작')

while True:
  read = arduino.readline().decode()
  print(read)
