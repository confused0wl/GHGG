# -*- coding: utf-8 -*-
"""
Created on Sat May 30 20:52:51 2020

@author: me442
"""
from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt
import numpy as np

class Vertex:
  # Basic class of point
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
class Facet:
  # Basic class of facet
  # May need to enforce method invariant of listing points counter clockwise
  # for consistency
  def __init__(self):
    self.pt_list = []
  def add_vertex(self, vtx):
    self.pt_list.append(vtx)
  def add_list_vtxs(self,vtx_list):
    for vtx in vtx_list:
      self.add_vertex(vtx)
class Box:
  # A box here is defined as a list of facets
  # an invariant is that this makes a closed shape
  def __init__(self):
    self.facet_list = []
  def setDims(self,W,L,H):
    self.W = W
    self.H = H
    self.L = L
  def add_facet(self, facet):
    self.facet_list.append(facet)
  def add_list_facets(self,facets_list):
    for facet in facets_list:
      self.add_facet(facet)
class GH(Box):
  # A GH extends box type here is defined as a list of facets
  def __init__(self):
    super().__init__()
  def setDims(self,W,L,Hg,Hp):
    self.W = W
    self.L = L
    self.Hg = Hg
    self.Hp = Hp
class MultiSpanGH:
  def __init__(self):
    self.box_list = []
  def setNumSpans(self,num_spans):
    self.numSpans = num_spans
  def add_box(self, box):
    self.box_list.append(box)
  def add_list_box(self,box_list):
    for box in box_list:
      self.add_box(box)
      
def genBox(W,L,H):
  # Basic rectangular box with 6-sides
  # This can be used as framework for structural information (framing percentage)
  # R1 - Front, R2 - back, R3-bottom, R4-Top
  # R5 - near side, R6 - far side (not aligned with axis)
  #*******************************
  R1 = Facet()
  r1v1 =Vertex(0,0,0)
  r1v2 = Vertex(W,0,0)
  r1v3 = Vertex(W,0,H)
  r1v4 = Vertex(0,0,H)
  r1_list = [r1v1,r1v2,r1v3,r1v4]
  R1.add_list_vtxs(r1_list)
  
  R2 = Facet()
  r2v1 =Vertex(0,L,0)
  r2v2 = Vertex(W,L,0)
  r2v3 = Vertex(W,L,H)
  r2v4 = Vertex(0,L,H)
  r2_list = [r2v1,r2v2,r2v3,r2v4]
  R2.add_list_vtxs(r2_list)
  
  R3 = Facet()
  r3v1 =Vertex(0,0,0)
  r3v2 = Vertex(W,0,0)
  r3v3 = Vertex(W,L,0)
  r3v4 = Vertex(0,L,0)
  r3_list = [r3v1,r3v2,r3v3,r3v4]
  R3.add_list_vtxs(r3_list)
  
  R4 = Facet()
  r4v1 =Vertex(0,0,H)
  r4v2 = Vertex(W,0,H)
  r4v3 = Vertex(W,L,H)
  r4v4 = Vertex(0,L,H)
  r4_list = [r4v1,r4v2,r4v3,r4v4]
  R4.add_list_vtxs(r4_list)
  
  R5 = Facet()
  r5v1 =Vertex(0,0,0)
  r5v2 = Vertex(0,L,0)
  r5v3 = Vertex(0,L,H)
  r5v4 = Vertex(0,0,H)
  r5_list = [r5v1,r5v2,r5v3,r5v4]
  R5.add_list_vtxs(r5_list)
  
  R6 = Facet()
  r6v1 =Vertex(W,0,0)
  r6v2 = Vertex(W,L,0)
  r6v3 = Vertex(W,L,H)
  r6v4 = Vertex(W,0,H)
  r6_list = [r6v1,r6v2,r6v3,r6v4]
  R6.add_list_vtxs(r6_list)
  
  b1 = Box()
  b1.setDims(W,L,H)
  b1.add_list_facets([R1,R2,R3,R4,R5,R6])
  return b1

def genGableGH(W,L,Hg,Hp):
  # Basic Gable greenhouse with 9 facets
  # R1 - Front, R2 - back, R3-bottom, R4a-Top near side, R4b-top far side
  # R5 - near side, R6 - far side (not aligned with axis)
  # R7- front triangular section, R8- back triangular section
  #*******************************
  R1 = Facet()
  r1v1 =Vertex(0,0,0)
  r1v2 = Vertex(W,0,0)
  r1v3 = Vertex(W,0,Hg)
  r1v4 = Vertex(0,0,Hg)
  r1_list = [r1v1,r1v2,r1v3,r1v4]
  R1.add_list_vtxs(r1_list)
  
  R2 = Facet()
  r2v1 =Vertex(0,L,0)
  r2v2 = Vertex(W,L,0)
  r2v3 = Vertex(W,L,Hg)
  r2v4 = Vertex(0,L,Hg)
  r2_list = [r2v1,r2v2,r2v3,r2v4]
  R2.add_list_vtxs(r2_list)
  
  R3 = Facet()
  r3v1 =Vertex(0,0,0)
  r3v2 = Vertex(W,0,0)
  r3v3 = Vertex(W,L,0)
  r3v4 = Vertex(0,L,0)
  r3_list = [r3v1,r3v2,r3v3,r3v4]
  R3.add_list_vtxs(r3_list)
  
  R4a = Facet()
  r4av1 =Vertex(0,0,Hg)
  r4av2 = Vertex(0,L,Hg)
  r4av3 = Vertex(W/2,L,Hp)
  r4av4 = Vertex(W/2,0,Hp)
  r4a_list = [r4av1,r4av2,r4av3,r4av4]
  R4a.add_list_vtxs(r4a_list)
  
  R4b = Facet()
  r4bv1 =Vertex(W,0,Hg)
  r4bv2 = Vertex(W/2,0,Hp)
  r4bv3 = Vertex(W/2,L,Hp)
  r4bv4 = Vertex(W,L,Hg)
  r4b_list = [r4bv1,r4bv2,r4bv3,r4bv4]
  R4b.add_list_vtxs(r4b_list)  
  
  R5 = Facet()
  r5v1 =Vertex(0,0,0)
  r5v2 = Vertex(0,L,0)
  r5v3 = Vertex(0,L,Hg)
  r5v4 = Vertex(0,0,Hg)
  r5_list = [r5v1,r5v2,r5v3,r5v4]
  R5.add_list_vtxs(r5_list)
  
  R6 = Facet()
  r6v1 =Vertex(W,0,0)
  r6v2 = Vertex(W,L,0)
  r6v3 = Vertex(W,L,Hg)
  r6v4 = Vertex(W,0,Hg)
  r6_list = [r6v1,r6v2,r6v3,r6v4]
  R6.add_list_vtxs(r6_list)
  
  R7 = Facet()
  r7v1 =Vertex(0,0,Hg)
  r7v2 = Vertex(W,0,Hg)
  r7v3 = Vertex(W/2,0,Hp)
  r7_list = [r7v1,r7v2,r7v3]
  R7.add_list_vtxs(r7_list)

  R8 = Facet()
  r8v1 =Vertex(0,L,Hg)
  r8v2 = Vertex(W,L,Hg)
  r8v3 = Vertex(W/2,L,Hp)
  r8_list = [r8v1,r8v2,r8v3]
  R8.add_list_vtxs(r8_list)
  
  b1 = GH()
  b1.setDims(W,L,Hg,Hp)
  b1.add_list_facets([R1,R2,R3,R4a,R4b,R5,R6,R7,R8])
  return b1

def rotatePoint(vtx,theta):
  x = vtx.x
  vtx.x = np.cos(theta*np.pi/180)*vtx.x - np.sin(theta*np.pi/180)*vtx.y
  vtx.y = np.sin(theta*np.pi/180)*x + np.cos(theta*np.pi/180)*vtx.y  
  return vtx

def rotateBox(box, theta):
  for fc in box.facet_list:
    for vtx in fc.pt_list:
      rotatePoint(vtx,theta)
  return box
def translatePointX(vtx,xmove):
  vtx.x = vtx.x+xmove
  return vtx
def translateBox(box, xmove):
  for fc in box.facet_list:
    for vtx in fc.pt_list:
      translatePointX(vtx,xmove)
  return box

def multiplySpans(box,num_spans):
  msgh = MultiSpanGH()  
  msgh.numSpans = num_spans
  msgh.box_list.append(box)
  for i in range(num_spans):
    msgh.add_box(translateBox(genGableGH(box.W,box.L,box.Hg,box.Hp),box.W*i))  
  return msgh
def rotateMSGH(msgh, theta):
  for box in msgh.box_list:
    for fc in box.facet_list:
      for vtx in fc.pt_list:
        rotatePoint(vtx,theta)
  return msgh

def plotBoxPoints(b1,W,L,H):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')  
  for fc in b1.facet_list:
    for vtx in fc.pt_list:
      ax.scatter(vtx.x,vtx.y,vtx.z,color='blue')
  ax.set_ylim(-L*1.1,L*1.1)
  ax.set_xlim(-L*1.1,L*1.1)
  ax.set_zlim(0,L*1.1)
  
def plotBoxLines(b1,W,L,H):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')  
  for fc in b1.facet_list:
    first_pt = True
    Xs=[]
    Ys=[]
    Zs=[]
    for vtx in fc.pt_list:
      if(first_pt):
        pt1 = vtx
        first_pt = False
      Xs.append(vtx.x)
      Ys.append(vtx.y)
      Zs.append(vtx.z)
    Xs.append(pt1.x)
    Ys.append(pt1.y)
    Zs.append(pt1.z)
    ax.plot(Xs[:],Ys[:],Zs[:],color='blue') 
  ax.set_ylim(-L*1.1,L*1.1)
  ax.set_xlim(-L*1.1,L*1.1)
  ax.set_zlim(0,L*1.1)
  
def getMSGHBounds(msgh):
  MINX = 1000
  MINY = 1000
  MINZ = 1000
  MAXX = -1000
  MAXY = -1000
  MAXZ = -1000
  for box in msgh.box_list:
    for facet in box.facet_list:
      for vtx in facet.pt_list:
        x = vtx.x
        y = vtx.y
        z = vtx.z
        if(x<MINX):
          MINX = x
        if(y<MINY):
          MINY = y
        if(z<MINZ):
          MINZ = z
        if(x>MAXX):
          MAXX = x
        if(y>MAXY):
          MAXY = y
        if(z>MAXZ):
          MAXZ = z
  return MINX, MINY, MINZ, MAXX, MAXY, MAXZ
#***************************************
def plotSpanLines(msgh,W,L,H):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')    
  for b1 in msgh.box_list:
    for fc in b1.facet_list:
      first_pt = True
      Xs=[]
      Ys=[]
      Zs=[]
      for vtx in fc.pt_list:
        if(first_pt):
          pt1 = vtx
          first_pt = False
        Xs.append(vtx.x)
        Ys.append(vtx.y)
        Zs.append(vtx.z)
      Xs.append(pt1.x)
      Ys.append(pt1.y)
      Zs.append(pt1.z)
      ax.plot(Xs[:],Ys[:],Zs[:],color='blue')
    MINX, MINY, MINZ, MAXX, MAXY, MAXZ= getMSGHBounds(msgh)    
    lb = min(MINX,MINY)
    ub = max(MAXX,MAXY)
    ax.set_ylim(1.1*lb,ub*1.1)
    ax.set_xlim(1.1*lb,ub*1.1)
    ax.set_zlim(0,MAXZ*2)
    ax.set_zticklabels([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])


    

    
