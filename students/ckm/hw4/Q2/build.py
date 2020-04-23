#!C:\Users\86152\AppData\Local\Programs\Python\Python37\python.exe
#coding=utf-8
import cgi,cgitb
import os
import time
from mcpi.minecraft import  Minecraft
form=cgi.FieldStorage()
mc=Minecraft.create()
mc_move=form.getvalue("mc_move")
mc_dir=form.getvalue("mc_dir")
#map=[[0.5,0.5]for x in range(10)]
#print(map)

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\'utf-8'\>")
print("<title>ckm1919</title>")
print("</head>")
print("<body>")
print("I'm Building now")
print("</body>")
print("</html>")

import mcpi.block as block
mc=Minecraft.create();
pos=mc.player.getTilePos();
def box(x,y,z,l,w,h,num=12):
    for i in range(0,l):
        for j in range(0,w):
            for k in range(0,h):
                mc.setBlock(x+i,y+j,z+k,num);




def house(x,y,z,l,w,h,q=3):
    box(x,y,z,l,1,h,q)
    box(x,y,z,1,w,h,q)
    box(x,y,z,l,w,1,q)
    box(x,y+w,z,l,1,h,q)
    box(x+l,y,z,1,w,h,q)
    box(x,y,z+h,l,w,1,q)
    windows(x,y+5.0/10*w,z);
    windows(x+4.0/l*10,y+6.0/10*w,z);
    windows(x+8.0/10*l,y+6.0/10*w,z)
    windows(x,y+5.0/10*w,z+h);
    windows(x+4.0/10*l,y+6.0/10*w,z+h);
    windows(x+8.0/10*l,y+6.0/10*w,z+h)
    box(x+6,y,z+h,2,4,1,block.WOOD.id)
    
    
    
    



def windows(x,y,z):
    box(x,y,z,2,2,1,20)





tmpa=pos.x
tmpb=pos.y+10
tmpc=pos.z
house(pos.x,pos.y+10,pos.z,10,10,10)



