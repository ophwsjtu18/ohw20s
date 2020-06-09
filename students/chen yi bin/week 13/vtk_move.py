import vtk
import serial
import time

i=0

class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.ser=serial.Serial("COM6","9600",timeout=0.5)
       self.angle1=0
       self.angle2=0
       self.angle3=0
       self.angle4=0
   def execute(self,obj,event):
      #print(self.timer_count,event)
      if event !="TimerEvent":
         return
      resp=self.ser.readline().decode().strip()
      if resp !="":
         spds=resp.split(",")
         print(resp)
         print(spds)
         angle=list(map(int,spds))
         print(angle,angle[0],angle[1],angle[2],angle[3])
         self.angle1=angle[0]-90
         self.angle2=angle[1]
         self.angle3=angle[2]
         self.angle4=angle[3]
         print("收到指令",self.angle1,self.angle2,self.angle3,self.angle4)
         print("瞄准中...")
         
         global i
         j=0
         k=45
         l=60
         h=90
         if i<=self.angle1:
            while i<=self.angle1:
               i+=1
               self.actors[0].SetOrientation(0,0,i)
               iren = obj
               iren.GetRenderWindow().Render()
               time.sleep(0.005)
         else:
            while i>self.angle1:
               i-=1
               self.actors[0].SetOrientation(0,0,i)
               iren = obj
               iren.GetRenderWindow().Render()
               time.sleep(0.005)
         
         print("装弹中...")
         while j<=self.angle4:
            j+=1
            self.actors[2].SetOrientation(j,0,0)
            iren = obj
            iren.GetRenderWindow().Render()
            time.sleep(0.0025)
         
         while j>=0:
            j-=1
            self.actors[2].SetOrientation(j,0,0)
            iren = obj
            iren.GetRenderWindow().Render()
            time.sleep(0.0025)
         
         print("蓄力中...")
         while k<=self.angle2:
            k+=1
            self.actors[1].SetOrientation(k-90,0,0)
            iren = obj
            iren.GetRenderWindow().Render()
            time.sleep(0.0025)
         
         print("解锁，发射！")
         while l<=self.angle3:
            l+=1
            self.actors[3].SetOrientation(0,0,l-60)
            iren = obj
            iren.GetRenderWindow().Render()
            time.sleep(0.0005)

         while h<=self.angle2:
            h+=1
            self.actors[4].SetOrientation(h-60,0,0)
            iren = obj
            iren.GetRenderWindow().Render()
            time.sleep(0.0005)

         time.sleep(0.3)
         
         print("复位中...")
         while h>=90:
            k-=1
            h-=1
            self.actors[1].SetOrientation(k-90,0,0)
            self.actors[4].SetOrientation(h-90,0,0)
            iren = obj
            iren.GetRenderWindow().Render()
            time.sleep(0.0025)
         while k>=45:
            k-=1
            self.actors[1].SetOrientation(k-90,0,0)
            iren = obj
            iren.GetRenderWindow().Render()
            time.sleep(0.0025)
         while l>=60:
            l-=1
            self.actors[3].SetOrientation(0,0,l-60)
            iren = obj
            iren.GetRenderWindow().Render()
            time.sleep(0.0005)
            
         '''while i>=0:
            i-=1
            self.actors[0].SetOrientation(0,0,i)
            iren = obj
            iren.GetRenderWindow().Render()
            time.sleep(0.005)'''
         
      else :
          print("待机中...")
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
   reader10 = vtk.vtkSTLReader()
   reader10.SetFileName("bar.stl")

    
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
   mapper10 = vtk.vtkPolyDataMapper()
   mapper10.SetInputConnection(reader10.GetOutputPort())

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
   actor10 = vtk.vtkActor()
   actor10.SetMapper(mapper10)

   # assembly actor1 and actor2
   assembly1 = vtk.vtkAssembly()
   assembly1.AddPart(actor3)
   assembly1.AddPart(actor5)
   assembly1.AddPart(actor7)
   assembly1.AddPart(actor8)

   assembly2 = vtk.vtkAssembly()
   assembly2.AddPart(actor4)
   assembly2.AddPart(actor6)

   assembly3 = vtk.vtkAssembly()
   assembly3.AddPart(actor1)
   assembly3.AddPart(actor2)
   assembly3.AddPart(assembly1)
   assembly3.AddPart(actor9)
   assembly3.AddPart(actor10)

   # Setup a renderer, render window, and interactor
   renderer = vtk.vtkRenderer()
   renderWindow = vtk.vtkRenderWindow()
   renderWindow.SetWindowName("Catapult T3")

   renderWindow.AddRenderer(renderer)
   #renderWindow.SetFrameRate(10)
   renderWindowInteractor = vtk.vtkRenderWindowInteractor()
   renderWindowInteractor.SetRenderWindow(renderWindow)

   #print("bbbbbbbbbbbbbbbbbbbbbbbbbbb",actor10.GetBounds())
   #print("CCCCCCCCCCCCCCCCCCCCC",actor10.GetCenter())

   #Add the actor to the scene
   renderer.AddActor(assembly2)
   renderer.AddActor(assembly3)
   renderer.SetBackground(0,0.8,0.8) # Background color white

   actor1.SetOrigin(-16,-27,122)
   actor1.SetPosition(16,27,-122)
   actor1.SetScale(1,1,1)
   actor2.SetOrigin(-35,-37,190)
   actor2.SetPosition(16,27,-122)
   actor2.SetScale(1,1,1)
   actor9.SetOrigin(8,72,124)
   actor9.SetPosition(16,27,-122)
   actor9.SetScale(1,1,1)
   actor10.SetOrigin(-41,54,120)
   actor10.SetPosition(16,27,-122)
   actor10.SetScale(1,1,1)
   assembly1.SetOrigin(-16,-27,122)
   assembly1.SetPosition(16,27,-122)
   assembly1.SetScale(1,1,1)
   assembly2.SetOrigin(-16,-27,122)
   assembly2.SetPosition(16,27,-122)
   assembly2.SetScale(1,1,1)

   #Render and interact
   renderWindow.Render()

   # Initialize must be called prior to creating timer events.
   renderWindowInteractor.Initialize()

   # Sign up to receive TimerEvent
   cb = mytimercallback()
   cb.actors.append(assembly3)
   cb.actors.append(actor2)
   cb.actors.append(actor9)
   cb.actors.append(actor10)
   cb.actors.append(actor1)
   renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
   timerId = renderWindowInteractor.CreateRepeatingTimer(100)
   #start the interaction and timer
   renderWindowInteractor.Start()


if __name__ == '__main__':
   main()
