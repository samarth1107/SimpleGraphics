#Samarth Chauhan
#2018410
#Group 3
#Section B
""" Draws a design with squares and a design
with rings."""

from SimpleGraphics import *
import math

# First Figure
MakeWindow(6,bgcolor=WHITE,labels=False)
DrawRect(0,0,5.5,5.5,FillColor=WHITE,EdgeColor=CYAN,EdgeWidth=5,theta=0)
DrawRect(0,0,5,5,FillColor=WHITE,EdgeColor=CYAN,EdgeWidth=5,theta=-5)
DrawRect(0,0,4.5,4.5,FillColor=WHITE,EdgeColor=CYAN,EdgeWidth=5,theta=-10)
DrawRect(0,0,4,4,FillColor=WHITE,EdgeColor=CYAN,EdgeWidth=5,theta=-15)
DrawRect(0,0,3.5,3.5,FillColor=WHITE,EdgeColor=CYAN,EdgeWidth=5,theta=-20)
DrawRect(0,0,3,3,FillColor=WHITE,EdgeColor=CYAN,EdgeWidth=5,theta=-25)


# Second Figure
MakeWindow(15,bgcolor=WHITE,labels=False)
# Rings
DrawDisk(0,0,4,EdgeWidth=1)
DrawDisk(8,0,4,EdgeWidth=1)
DrawDisk(-8,0,4,EdgeWidth=1)
DrawDisk(-4,4*(math.sqrt(3)),4,EdgeWidth=1)
DrawDisk(4,4*(math.sqrt(3)),4,EdgeWidth=1)
DrawDisk(0,8*(math.sqrt(3)),4,EdgeWidth=1)


ShowWindow()
