import vtk

property = vtk.vtkProperty()
property.SetColor(0, 1, 0)
property.SetDiffuse(0.7)
property.SetSpecular(0.4)
property.SetSpecularPower(20)
Actor=[]
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
for j in range(10):
    Actor[j].SetPosition(0,0,0)
    ren1.AddActor(Actor[j])

ren1.SetBackground(0.1, 0.2, 0.4)


renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(300, 300)
renWin.Render()
