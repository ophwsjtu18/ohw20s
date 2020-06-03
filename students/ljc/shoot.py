import vtk
import time

#colors = vtk.vtkNamedColors()

reader1 = vtk.vtkSTLReader()
reader1.SetFileName("arm.stl")
reader2 = vtk.vtkSTLReader()
reader2.SetFileName("arm_motor_base.stl")
reader3 = vtk.vtkSTLReader()
reader3.SetFileName("plate.stl")

mapper1=vtk.vtkPolyDataMapper()
mapper1.SetInputConnection(reader1.GetOutputPort())
mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputConnection(reader2.GetOutputPort())
mapper3 = vtk.vtkPolyDataMapper()
mapper3.SetInputConnection(reader3.GetOutputPort())

axes = vtk.vtkAxesActor()
axes.SetTotalLength(1, 2, 3)
axes.SetShaftType(0)
axes.SetAxisLabels(0)
axes.SetCylinderRadius(0.02)

actor1=vtk.vtkActor()
actor1.SetMapper(mapper1)
actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor3 = vtk.vtkActor()
actor3.SetMapper(mapper3)

#assembly = vtk.vtkAssembly()
#assembly.AddPart(actor1)
#assembly.AddPart(actor2)
#assembly.AddPart(actor3)
#assembly.SetOrigin(actor1.GetCenter())


renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

transform = vtk.vtkTransform()
transform.Translate(1.0, 0.0, 0.0)

#axes = vtk.vtkAxesActor()
#axes.SetUserTransform(transform)

#axes.GetXAxisCaptionActor2D().GetCaptionTextProperty().SetColor(colors.GetColor3d("Red"))

renderer.AddActor(actor1)
renderer.AddActor(actor2)
renderer.AddActor(actor3)
renderer.AddActor(axes)


renderer.SetBackground(0,1,1)

print("actor1 center:",actor1.GetCenter())
print("actor2 center:",actor2.GetCenter())
print("actor3 center:",actor3.GetCenter())


actor1.SetOrigin(-16,-14,122)
actor2.SetOrigin(0,0,0)
actor3.SetOrigin(0,0,0)

for i in range(10):
    time.sleep(0.1)
    actor1.RotateX(0.2)
    renderWindow.Render()

for i in range(36):
    time.sleep(0.01)
    actor1.RotateX(2)    
    renderWindow.Render()

for i in range(10):
    time.sleep(0.1)  
    renderWindow.Render()
    
for i in range(68):
    time.sleep(0.01)
    actor1.RotateX(-1)    
    renderWindow.Render()

renderWindowInteractor.Start()
