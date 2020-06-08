import vtk
import time
import serial

class STLComponent:
  prop = vtk.vtkProperty()
  @classmethod
  def SetProperty(self, color, diffuse, specular, specularPower):
    self.prop.SetColor(color[0], color[1], color[2])
    self.prop.SetDiffuse(diffuse)
    self.prop.SetSpecular(specular)
    self.prop.SetSpecularPower(specularPower)
  def __init__(self, name):
    self.reader = vtk.vtkSTLReader()
    self.reader.SetFileName(name)
    self.mapper = vtk.vtkPolyDataMapper()
    self.mapper.SetInputConnection(self.reader.GetOutputPort())
    self.actor  = vtk.vtkActor()
    self.actor.SetMapper(self.mapper)
    self.actor.SetProperty(self.prop)

cone = vtk.vtkConeSource()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cone.GetOutputPort())

actorx = vtk.vtkActor()
actorx.SetMapper(mapper)

# create coordinate axes in the render window
axes = vtk.vtkAxesActor()
axes.SetTotalLength(10, 20, 30)
axes.SetShaftType(0)
axes.SetAxisLabels(0)
axes.SetCylinderRadius(0.02)


STLComponent.SetProperty(color = [1, 1, 1], diffuse = 1,
                         specular = 0.4, specularPower = 20)

STLName = ['arm.stl',
           'arm_motor_base.stl',
           'arming_arm.stl',
           'base.stl',
           'base_motor_mount.stl',
           'box.stl',
           'plate.stl',
           'tray.stl',
           'tray_gate.stl']
STLPart = []

for name in STLName:
  STLPart.append(STLComponent(name))

ren = vtk.vtkRenderer()
ren.SetBackground(0xCC / 255, 0xA4 / 255, 0xE3 / 255)

for part in STLPart:
  ren.AddActor(part.actor)
ren.AddActor(actorx)
ren.AddActor(axes)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetSize(600, 600)

actorx.SetOrigin(0,0,0)
for part in STLPart:
    part.actor.SetOrigin(-16,-27,122)
    part.actor.SetPosition(16,27,-122)
    part.actor.SetScale(1,1,1)

for i in range(36):
    time.sleep(0.1)
    actorx.RotateX(10)
    print(actorx.GetOrientation())
    actorx.SetOrientation(0,i*(-30),0)
    actorx.AddOrientation(5,0,0)
    STLPart[0].actor.RotateX(10)
    renWin.Render()

renWin.Render()

ser=serial.Serial("COM20",timeout=1)


while True:
    print("reading....")
    resp=ser.readline()
    if resp != b"":
        a=resp.decode()
        print(a)
        print("get commnd, I will handle it",resp)
        b=a.strip()
        if b == 'e':
            break
        c=b.split(",")
        d=list(map(int,c))
        servo1=d[0]
        servo2=d[1]
        servo3=d[2]
        print("move servo to angle",servo1,servo2,servo3)
        STLPart[0].actor.SetOrientation(servo1,0,0)
    else:
        print("working on something else..")     
    renWin.Render()

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renWin)
interactor.Start()
