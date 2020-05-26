import serial
ser=serial.Serial("COM2")

while True:
    a=input()
    if a == 'q':
        break
    print(a)
    ser.write(a.encode())
