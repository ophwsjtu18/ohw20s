import serial

ser=serial.Serial("COM1")
ser.write("100,200,100\n".encode())

while True:
    c=input("please input bottom arm and top arm speed")
    print(c)
    if c=="q":
        break
    ser.write(c.encode())



