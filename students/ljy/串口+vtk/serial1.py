import serial


ser=serial.Serial("COM2")

while True:
    a=input("input,q to quit,'~'to shut down")
    print(a)
    ser.write(a.encode())
    if a=='q':
        break
