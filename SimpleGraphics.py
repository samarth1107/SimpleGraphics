# SimpleGraphics.py

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
from time import sleep as pause

# Built-in SimpleGraphics colors
YELLOW    = [1.0,1.0,0.0]
CYAN      = [0.0,1.0,1.0]
MAGENTA   = [1.0,0.0,1.0]
RED       = [1.0,0.0,0.0]
GREEN     = [0.0,1.0,0.0]
BLUE      = [0.0,0.0,1.0]
WHITE     = [1.0,1.0,1.0]
BLACK     = [0.0,0.0,0.0]
PURPLE    = [.57,.17,.93]
DARKGRAY  = [.33,.33,.33]
LIGHTGRAY = [.67,.67,.67]
ORANGE    = [1.0,.50,0.0]
PINK      = [1.0,.71,.80]


def MakeWindow(M,labels=True,bgcolor=WHITE):
    plt.figure(figsize=(8,8), dpi=80)
    # Where to put the axis ticks.
    plt.xticks(np.linspace(-M, M, 2*M+1, endpoint=True))
    plt.yticks(np.linspace(-M, M, 2*M+1, endpoint=True))
    # The x and y ranges along the axes.
    plt.xlim(-M,M)
    plt.ylim(-M,M)
    # Background color
    axes = plt.gca() #get current axes
    axes.set_facecolor(bgcolor) 
    if not labels:
        # Suppress the ticks
        axes.set_xticks([]) # remove number labels and ticks
        axes.set_yticks([])
       
def ShowWindow(time=None):
    if time==None:
        plt.show()
    else:
        plt.show(block=False)
        pause(time)
    
def CloseWindow():
    plt.close()


def DrawRect(a,b,L,W,theta=0.0,FillColor=None,EdgeColor=BLACK,EdgeWidth=1):
    # These arrays specify the (x,y) coordinates of the rectangle corners.
    L = float(L)
    W = float(W)
    theta = theta*np.pi/180
    x1 = np.array([-L/2,L/2,L/2,-L/2,-L/2])
    y1 = np.array([-W/2,-W/2,W/2,W/2,-W/2])
    x = a + np.cos(theta)*x1 - np.sin(theta)*y1
    y = b + np.sin(theta)*x1 + np.cos(theta)*y1
    if FillColor is None:
        # No fill, just draw the perimeter
        plt.plot(x,y,color=EdgeColor,linewidth=EdgeWidth)
    else:
        # Fill and accent the perimeter according to the values of eColor and eWidth.
        plt.fill(x,y,facecolor=FillColor,edgecolor=EdgeColor,linewidth=EdgeWidth)


def DrawDisk(a,b,r,FillColor=None,EdgeColor=BLACK,EdgeWidth=1):    
    theta= np.linspace(0,2*np.pi,256,endpoint=True)
    x = a+r*np.cos(theta)
    y = b+r*np.sin(theta)
    if FillColor is None:
        # No fill, just the perimeter
        plt.plot(x,y,color=EdgeColor,linewidth=EdgeWidth)
    else:
        # Fill and accent the perimeter according to the values of EdgeColor and EdgeWidth.
        plt.fill(x,y,facecolor=FillColor,edgecolor=EdgeColor,linewidth=EdgeWidth)


def DrawStar(a,b,r,theta=0.0,FillColor=None,EdgeColor=BLACK,EdgeWidth=1):
    # The radius of the inner 5 vertices..
    r2 = r/(2*(1+np.sin(np.pi/10)))
    # Compute the 10 vertices
    tau = np.linspace(0,2*np.pi,11,endpoint=True) + np.pi/10 + theta*np.pi/180
    x = np.cos(tau); x[0:11:2]= r*x[0:11:2]; x[1:11:2]=r2*x[1:11:2]; x = x+a
    y = np.sin(tau); y[0:11:2]= r*y[0:11:2]; y[1:11:2]=r2*y[1:11:2]; y = y+b
    
    # Display...  
    if FillColor is None:
        # No fill, just the perimeter
        plt.plot(x,y,color=EdgeColor,linewidth=EdgeWidth)
    else:
        # Fill and accent the perimeter according to the values of eColor and eWidth.
        plt.fill(x,y,facecolor=FillColor,edgecolor=EdgeColor,linewidth=EdgeWidth)
        
    
def DrawLineSeg(x0,y0,x1,y1,LineColor=BLACK,LineWidth=1):
    plt.plot([x0,x1],[y0,y1],linewidth=LineWidth,color=LineColor)
    
def DrawText(x,y,s,FontColor=BLACK,FontSize=10):
    plt.text(x,y,s,color=FontColor,fontsize=FontSize)
    
def Title(s,FontColor=BLACK,FontSize=18):
    plt.title(s,fontsize=FontSize,color=FontColor)
    
def DrawPoly(x,y, FillColor=None, EdgeWidth=1, EdgeColor=BLACK):
    # These arrays specify the (x,y) coordinates of the rectangle corners.
    u = list(x);u.append(u[0])
    v = list(y);v.append(v[0])
    if FillColor is None:
        # No fill, just draw the perimeter
        plt.plot(u, v,linewidth=EdgeWidth,color=EdgeColor)
    else:
        # Fill and accent the perimeter according to the value of stroke.
        plt.fill(u, v, facecolor=FillColor, edgecolor=EdgeColor, linewidth=EdgeWidth)
