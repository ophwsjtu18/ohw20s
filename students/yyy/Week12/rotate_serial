import vtk
import serial
property = vtk.vtkProperty()
property.SetColor(0, 1, 0)
property.SetDiffuse(0.7)
property.SetSpecular(0.4)
property.SetSpecularPower(20)
Actor=[]

axes = vtk.vtkAxesActor()
axes.SetTotalLength(10, 20, 30)
axes.SetShaftType(0)
axes.SetAxisLabels(0)
axes.SetCylinderRadius(0.02)
filenames = ["plate.stl","arm.stl","tray.stl","tray_gate.stl","arm_motor_base.stl","arming_arm.stl","base.stl","base_motor_mount.stl","controller_bottom.stl","controller_top.stl"]
for i in range(10):
    reader = vtk.vtkSTLReader()
    reader.SetFileName(filenames[i])
    rtlMapper = vtk.vtkPolyDataMapper()
    rtlMapper.SetInputConnection(reader.GetOutputPort())
    actor=vtk.vtkActor()
    actor.SetMapper(rtlMapper)
    actor.SetProperty(property)
    Actor.append(actor)
ren1 = vtk.vtkRenderer()
ren1.AddActor(axes)


for j in range(10):
    Actor[j].SetPosition(0,0,0)

    ren1.AddActor(Actor[j])

ren1.SetBackground(0.1, 0.2, 0.4)


renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(300, 300)


interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renWin)
print("bbbbbbbbbbbbbbbbbbbbbbbbbbb",Actor[1].GetBounds())
print("CCCCCCCCCCCCCCCCCCCCC",Actor[1].GetCenter())
Actor[1].SetOrigin(0,-41,0)
Actor[1].SetPosition(0,41,0)
ser=serial.Serial("COM2",timeout=1)
renWin.Render()

while True:
    print("reading....")

    resp=ser.readline()
    if resp != b"":
        a=resp.decode()
        print(a)
        print("get commnd, I will handle it",resp)
        b=a.strip()
        if b == '~':
            break
        c=b.split(",")
        d=list(map(int,c))
        servo1=d[0]
        servo2=d[1]
        servo3=d[2]
        print("move servo to angle",servo1,servo2,servo3)
        Actor[1].SetOrientation(servo1,0,0)
    else:
        print("working on something else..")     
    renWin.Render()
interactor.Start()
