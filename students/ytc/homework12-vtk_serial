import serial

ser = serial.Serial('COM12')

while True:
  msg = input('>')
  if msg is not None and msg != 'q':
    ser.write(msg.encode(encoding = 'utf-8'))
  elif msg == 'q':
    break

ser.close()
