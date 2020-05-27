import vtk
import time
import serial


Actor=[]

axes = vtk.vtkAxesActor()
axes.SetTotalLength(10, 20, 30)
axes.SetShaftType(0)
axes.SetAxisLabels(0)
axes.SetCylinderRadius(0.02)

filenames = [
    "plate.stl",
    "arm.stl",
    "tray.stl",
    "tray_gate.stl",
    "arm_motor_base.stl",
    "arming_arm.stl",
    "base.stl",
    "base_motor_mount.stl",
    "controller_bottom.stl",
    "controller_top.stl"
    "box.stl"]

property = vtk.vtkProperty()
property.SetColor(0, 0, 1)
property.SetDiffuse(1)
property.SetSpecular(0)
property.SetSpecularPower(10)

for i in range(10):
    reader = vtk.vtkSTLReader()
    reader.SetFileName(filenames[i])

    mapper1 = vtk.vtkPolyDataMapper()
    mapper1.SetInputConnection(reader.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper1)
    actor.SetProperty(property)
    Actor.append(actor)

ren1 = vtk.vtkRenderer()
ren1.AddActor(axes)


for i in range(10):
    Actor[i].SetPosition(0,0,0)
    ren1.AddActor(Actor[i])

ren1.SetBackground(1, 1, 1)


renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(500, 500)


interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renWin)
print("bbbbb",Actor[1].GetBounds())
print("CCCCC",Actor[1].GetCenter())

for i in range(10):
    Actor[i].SetOrigin(-16,48,122)
    Actor[i].SetPosition(16,-48,-122)
    
ser=serial.Serial("COM13",timeout=1)
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
