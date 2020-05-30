import vtk
import serial

class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.ser=serial.Serial("COM2","9600",timeout=0.2)
       self.botspeed=0
       self.topspeed=0
   def execute(self,obj,event):
      print(self.timer_count,event)
      if event !="TimerEvent":
         return
      resp=self.ser.readline().decode().strip()
      if resp !="":
         spds=resp.split(",")
         print(resp)
         print(spds)
         speeds=list(map(float,spds))
         print(speeds,speeds[0],speeds[1],speeds[2])
         self.botspeed=speeds[0]
         self.topspeed=speeds[1]
         print("speed update",self.botspeed,self.topspeed)
      self.actors[0].SetPosition(20,0,-10)
      self.actors[0].SetOrigin(0,-20,190)
      self.actors[1].SetPosition(15,35,20)
      self.actors[1].SetOrigin(-15,-35,-20)
      self.actors[0].RotateX(self.botspeed);
      self.actors[1].RotateX(self.topspeed);
      iren = obj
      iren.GetRenderWindow().Render()
      self.timer_count += 1


def main():

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
    renWin.Render()
    interactor.Initialize()
    cb = mytimercallback()
    cb.actors.append(Actor[1])
    cb.actors.append(Actor[5])
    interactor.AddObserver('TimerEvent', cb.execute)
    timerId = interactor.CreateRepeatingTimer(100)
    interactor.Start()

if __name__ == '__main__':
   main()
