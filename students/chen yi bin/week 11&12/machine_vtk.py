#a version from outstanding student

import vtk

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

STLComponent.SetProperty(color = [1, 1, 1], diffuse = 1,
                         specular = 0.4, specularPower = 20)

STLName = ['arm.stl',
           'arm_motor_base.stl',
           'arming_arm.stl',
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

STLPart[2].actor.SetPosition(20, 0, -10)
STLPart[3].actor.SetPosition(15, 35, 20)
STLPart[3].actor.RotateZ(90)
STLPart[5].actor.SetPosition(0, 0, -90)
STLPart[6].actor.SetPosition(0, 0, -90)

ren = vtk.vtkRenderer()
ren.SetBackground(0xCC / 255, 0xA4 / 255, 0xE3 / 255)
for part in STLPart:
  ren.AddActor(part.actor)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetSize(600, 600)
renWin.Render()
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renWin)
interactor.Start()
