import vtk
import time
import serial

ser = serial.Serial('COM13', timeout = 1)

#STLreader
reader=[]
stlMapper=[]
actor=[]
stl=["arm.stl","except arm.stl"]
ren = vtk.vtkRenderer()
property = vtk.vtkProperty()
property.SetColor(1, 1, 1)
property.SetDiffuse(2)
property.SetSpecular(0.8)
property.SetSpecularPower(20)

for i in range(0,2):

    reader.append(vtk.vtkSTLReader())
    reader[i].SetFileName(stl[i])
    stlMapper.append(vtk.vtkPolyDataMapper())
    stlMapper[i].SetInputConnection(reader[i].GetOutputPort())
    actor.append(vtk.vtkActor())
    actor[i].SetMapper(stlMapper[i])
    actor[i].SetProperty(property)
    
actor[0].SetPosition(116.5,0,0)
actor[1].RotateZ(-90)

actor[0].SetOrigin(0, -17, 123)
for i in range(0,2):
    ren.AddActor(actor[i])
ren.SetBackground(0.3, 0.3, 0.7)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetSize(600, 600)
renWin.Render()

angle=45

currentAngle = actor[0].GetOrientation()[0]  
i = 0  
while abs(angle - actor[0].GetOrientation()[0]) >= 0.5:
        actor[0].AddOrientation((angle - currentAngle) * 0.01, 0, 0)
        renWin.Render()
        i += 1
        print('Render process:', i, '%')
        time.sleep(0.01)
        actor[0].SetOrientation(angle, 0, 0)
        renWin.Render()
        print('Completed')
        time.sleep(1)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renWin)
interactor.Start()

'''from  wsj  serial COM
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
      currentAngle = actor[0].GetOrientation()[0]  
      i = 0  
      while abs(angle - actor[0].GetOrientation()[0]) >= 0.5:
        actor[0].AddOrientation((angle - currentAngle) * 0.01, 0, 0)
        renWin.Render()
        i += 1
        print('Render process:', i, '%')
        time.sleep(0.01)
        actor[0].SetOrientation(angle, 0, 0)
        renWin.Render()
        print('Completed')
        time.sleep(1)
  else:
    print('idle')
    time.sleep(1)
'''
