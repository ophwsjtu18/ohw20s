import serial
import time
import vtk

##
# Definitions and global presets here
##

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
           'tray_gate.stl',
           'box.stl']
STLPart = []

axes = None

##
# For debug only
##

# axes = vtk.vtkAxesActor()
# axes.SetTotalLength(10, 20, 30)
# axes.SetShaftType(0)
# axes.SetAxisLabels(0)
# axes.SetCylinderRadius(0.02)

##
# For debug only
##

ser = serial.Serial('COM11', timeout = 1)

color_lilac = [0xCC / 255, 0xA4 / 255, 0xE3 / 255]

##
# Assembly and initialize
##

for name in STLName:
  STLPart.append(STLComponent(name))

STLPart[2].actor.SetPosition(20, 0, -10)
STLPart[2].actor.SetOrigin(0, -20, 190)
STLPart[3].actor.SetPosition(15, 35, 20)
STLPart[3].actor.RotateZ(90)
STLPart[5].actor.SetPosition(0, 0, -90)
STLPart[6].actor.SetPosition(0, 0, -90)

ren = vtk.vtkRenderer()
ren.SetBackground(color_lilac[0], color_lilac[1], color_lilac[2])
for part in STLPart:
  ren.AddActor(part.actor)

##
# For debug only
##

if axes is not None:
  ren.AddActor(axes)

##
# For debug only
##

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetSize(600, 600)
renWin.Render()

##
# Remote control by serial port
##

while True:
  msg = str(ser.readline(), encoding = 'utf-8').split('\r')[0]
  # In case that someone uses Windows to debug, which uses '\r\n' to break lines
  if msg != '':
    print('Command got:', msg)
    if msg == '~':
      print('Exit command got, exiting command mode...')
      ser.close()
      break
    else:
      try:
        angle = float(msg)
        if angle > 90:
          print('Too big angle, limited to 90')
          angle = 90
        elif angle < 0:
          print('Too small angle, limited to 0')
          angle = 0
      except BaseException:
        print('Unrecognized command:', msg)
        continue
      # STLPart[2].actor.SetOrientation(angle, 0, 0)
      currentAngle = STLPart[2].actor.GetOrientation()[0]
      # print(currentAngle)
      i = 0
      while abs(angle - STLPart[2].actor.GetOrientation()[0]) >= 0.5:
        # print((angle - currentAngle) * 0.01, STLPart[2].actor.GetOrientation()[0])
        STLPart[2].actor.AddOrientation((angle - currentAngle) * 0.01, 0, 0)
        renWin.Render()
        i += 1
        print('Render process:', i, '%')
        time.sleep(0.01)
      STLPart[2].actor.SetOrientation(angle, 0, 0)
      renWin.Render()
      print('Completed')
      time.sleep(1)
  else:
    print('idle')
    time.sleep(1)

##
# Interactive mode
##

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renWin)
interactor.Start()
