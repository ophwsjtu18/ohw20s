import vtk
import time
import serial


class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.botspeed=1
       self.topspeed=1
   def execute(self,obj,event):
       print(self.timer_count,event)
       self.actors[0].SetPosition(20,0,-10)
       self.actors[0].SetOrigin(-20,-25,120)
       self.actors[0].RotateX(self.topspeed);
       self.timer_count += 1


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

ser=serial.Serial("COM13",timeout=1)
renWin.Render()

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
renWin.SetSize(500, 500)
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renWin)

print("bbbbb",Actor[1].GetBounds())
print("CCCCC",Actor[1].GetCenter())

renWin.Render()
interactor.Initialize()

cb = mytimercallback()
cb.actors.append(Actor[1])

interactor.AddObserver('TimerEvent', cb.execute)
timerId = interactor.CreateRepeatingTimer(100)
interactor.Start()

