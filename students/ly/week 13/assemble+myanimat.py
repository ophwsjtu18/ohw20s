import vtk
import serial

class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.ser=serial.Serial("COM13","9600",timeout=0.5)
       self.leftspeed=0
       self.rightspeed=0
   def execute(self,obj,event):
      print(self.timer_count,event)
      if event !="TimerEvent":
         return
      resp=self.ser.readline().decode().strip()
      if resp !="":
         spds=resp.split(",")
         print(resp)
         print(spds)
         speeds=list(map(int,spds))
         print(speeds,speeds[0],speeds[1],speeds[2])
         self.leftspeed=speeds[0]
         self.rightspeed=speeds[1]
         print("speed update",self.leftspeed,self.rightspeed)
      self.actors[0].RotateX(self.leftspeed);
      self.actors[1].RotateX(self.rightspeed);
      iren = obj
      iren.GetRenderWindow().Render()
      self.timer_count += 1

def main():
   
   

   #Create a mapper and actor
   #Read STL
   reader1 = vtk.vtkSTLReader()
   reader1.SetFileName("arm.stl")
   reader2 = vtk.vtkSTLReader()
   reader2.SetFileName("arming_arm.stl")
   reader3 = vtk.vtkSTLReader()
   reader3.SetFileName("arm_motor_base.stl")
   reader4 = vtk.vtkSTLReader()
   reader4.SetFileName("base.stl")
   reader5 = vtk.vtkSTLReader()
   reader5.SetFileName("base_motor_mount.stl")
   reader6 = vtk.vtkSTLReader()
   reader6.SetFileName("box.stl")
   reader7 = vtk.vtkSTLReader()
   reader7.SetFileName("plate.stl")
   reader8 = vtk.vtkSTLReader()
   reader8.SetFileName("tray.stl")
   reader9 = vtk.vtkSTLReader()
   reader9.SetFileName("tray_gate.stl")

    
   #Create a mapper and actor
   mapper1 = vtk.vtkPolyDataMapper()
   mapper1.SetInputConnection(reader1.GetOutputPort())
   mapper2 = vtk.vtkPolyDataMapper()
   mapper2.SetInputConnection(reader2.GetOutputPort())
   mapper3 = vtk.vtkPolyDataMapper()
   mapper3.SetInputConnection(reader3.GetOutputPort())
   mapper4 = vtk.vtkPolyDataMapper()
   mapper4.SetInputConnection(reader4.GetOutputPort())
   mapper5 = vtk.vtkPolyDataMapper()
   mapper5.SetInputConnection(reader5.GetOutputPort())
   mapper6 = vtk.vtkPolyDataMapper()
   mapper6.SetInputConnection(reader6.GetOutputPort())
   mapper7 = vtk.vtkPolyDataMapper()
   mapper7.SetInputConnection(reader7.GetOutputPort())
   mapper8 = vtk.vtkPolyDataMapper()
   mapper8.SetInputConnection(reader8.GetOutputPort())
   mapper9 = vtk.vtkPolyDataMapper()
   mapper9.SetInputConnection(reader9.GetOutputPort())

   actor1 = vtk.vtkActor()
   actor1.SetMapper(mapper1)
   actor2 = vtk.vtkActor()
   actor2.SetMapper(mapper2)
   actor3 = vtk.vtkActor()
   actor3.SetMapper(mapper3)
   actor4 = vtk.vtkActor()
   actor4.SetMapper(mapper4)
   actor5 = vtk.vtkActor()
   actor5.SetMapper(mapper5)
   actor6 = vtk.vtkActor()
   actor6.SetMapper(mapper6)
   actor7 = vtk.vtkActor()
   actor7.SetMapper(mapper7)
   actor8 = vtk.vtkActor()
   actor8.SetMapper(mapper8)
   actor9 = vtk.vtkActor()
   actor9.SetMapper(mapper9)

   # assembly actor1 and actor2
   assembly = vtk.vtkAssembly()
   assembly.AddPart(actor3)
   assembly.AddPart(actor4)
   assembly.AddPart(actor5)
   assembly.AddPart(actor6)
   assembly.AddPart(actor7)
   assembly.AddPart(actor8)
   assembly.AddPart(actor9)


   # Setup a renderer, render window, and interactor
   renderer = vtk.vtkRenderer()
   renderWindow = vtk.vtkRenderWindow()
   #renderWindow.SetWindowName("Test")

   renderWindow.AddRenderer(renderer);
   renderWindowInteractor = vtk.vtkRenderWindowInteractor()
   renderWindowInteractor.SetRenderWindow(renderWindow)

   #Add the actor to the scene
   renderer.AddActor(actor1)
   renderer.AddActor(actor2)
   renderer.AddActor(assembly)
   renderer.SetBackground(0,0,0.8) # Background color white

   actor1.SetOrigin(-16,-27,122)
   actor1.SetPosition(16,27,-122)
   actor1.SetScale(1,1,1)
   actor2.SetOrigin(-35,-37,190)
   actor2.SetPosition(16,27,-122)
   actor2.SetScale(1,1,1)
   assembly.SetOrigin(-16,-27,122)
   assembly.SetPosition(16,27,-122)
   assembly.SetScale(1,1,1)

   #Render and interact
   renderWindow.Render()

   # Initialize must be called prior to creating timer events.
   renderWindowInteractor.Initialize()

   # Sign up to receive TimerEvent
   cb = mytimercallback()
   cb.actors.append(actor1)
   cb.actors.append(actor2)
   renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
   timerId = renderWindowInteractor.CreateRepeatingTimer(100);

   #start the interaction and timer
   renderWindowInteractor.Start()


if __name__ == '__main__':
   main()
