#!/usr/bin/env python
#
# This example demonstrates the creation of multiple actors and the
# manipulation of their properties and transformations. It is a
# derivative of Cone.py, see that example for more information.
#

import vtk
import time

property = vtk.vtkProperty()
property.SetColor(0, 1, 0)
property.SetDiffuse(0.7)
property.SetSpecular(0.4)
property.SetSpecularPower(20)

#RTLreader
reader=[]
rtlMapper=[]
actor=[]
stl=["arm.stl","arm_motor_base.stl","arming_arm.stl","base.stl","base_motor_mount.stl","controller_bottom.stl","controller_top.stl","plate.stl","tray.stl","tray_gate.stl"]

ren = vtk.vtkRenderer()

for i in range(0,9):

    reader.append(vtk.vtkSTLReader())
    reader[i].SetFileName(stl[i])
    rtlMapper.append(vtk.vtkPolyDataMapper())
    rtlMapper[i].SetInputConnection(reader[i].GetOutputPort())
    actor.append(vtk.vtkActor())
    actor[i].SetMapper(rtlMapper[i])
    actor[i].SetProperty(property)
    ren.AddActor(actor[i])

ren.SetBackground(0.1, 0.2, 0.4)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetSize(600, 600)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renWin)
renWin.Render()
interactor.Start()

