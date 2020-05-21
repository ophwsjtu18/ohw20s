import serial

ser=serial.Serial("COM12")

while True:
    a=input("please type your cmd here, q for quit, e for remote quit.")
    print(a)
    if a=='q':
        break
    ser.write(a.encode())
