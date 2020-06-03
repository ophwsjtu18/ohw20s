import vtk
import time
import serial
ser=serial.Serial("COM13",timeout=0.1)
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
    
class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.angle=0
   def execute(self,obj,event):
      print(self.timer_count,event)
      if event !="TimerEvent":
         return
      resp=ser.readline()
      if resp != b"":
          a=resp.decode()
          print(1)
          print("get commnd, I will handle it",resp)
          b=a.strip()
          c=b.split(",")
          d=list(map(int,c))
          servo1=d[0]
         # servo2=d[1]
          #servo3=d[2]
          self.angle=servo1
          print("move servo to angle",self.angle)
         
      else:
          print("working on something else..")     
      #window.Render()
      #renderer.GetActiveCamera().Azimuth( 10 )
      self.actors[0].SetOrientation(self.angle,0,0)
    
      iren = obj
      iren.GetRenderWindow().Render()
      self.timer_count += 1
       
def main():
  STLComponent.SetProperty(color = [1, 1, 1], diffuse = 1,
                           specular = 0.4, specularPower = 20)
  STLName = ['arming_arm.stl',
            'arm_motor_base.stl',
            'arm.stl',
            'base.stl',
            'base_motor_mount.stl',
            'controller_bottom.stl',
            'controller_top.stl',
            'plate.stl',
            'tray.stl',
            'tray_gate.stl']
  STLPart = []

  for name in STLName:
    STLPart.append(STLComponent(name))

  STLPart[0].actor.SetPosition(20, 0, -10)
  STLPart[0].actor.SetOrigin(0, -20, 190)
  STLPart[3].actor.SetPosition(-5, 35, 20)
  STLPart[3].actor.RotateZ(90)
  STLPart[5].actor.SetPosition(-20, 0, -90)
  STLPart[6].actor.SetPosition(-20, 0, -90)
  ren = vtk.vtkRenderer()
  ren.SetBackground(0xCC / 255, 0xA4 / 255, 0xE3 / 255)
  for part in STLPart:
    ren.AddActor(part.actor)

  renWin = vtk.vtkRenderWindow()
  renWin.AddRenderer(ren)
  renWin.SetSize(600, 600)
  renderWinInteractor = vtk.vtkRenderWindowInteractor()
  renderWinInteractor.SetRenderWindow(renWin)
  renWin.Render()
    # Initialize must be called prior to creating timer events.
  renderWinInteractor.Initialize()
  STLPart[2].actor.SetOrigin(0,-17,123)
 # STLPart[0].actor.SetPosition(16,0,-122)
  #STLPart[0].actor.SetOrigin(0,0,0)

   
  
  cb = mytimercallback()
  cb.actors.append(STLPart[0].actor)
 
   # Sign up to receive TimerEvent
 
  renderWinInteractor.AddObserver('TimerEvent', cb.execute)
  timerId = renderWinInteractor.CreateRepeatingTimer(100);

   #start the interaction and timer
  renderWinInteractor.Start()
  interactor = vtk.vtkRenderWindowInteractor()
  interactor.SetRenderWindow(renWin)
  interactor.Start()
  
if __name__ == '__main__':
   main()
