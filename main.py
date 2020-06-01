# -*- coding: utf-8 -*-
"""
Created on Sun May 31 17:08:36 2020

@author: me442
"""
import Greenhouse_gen as ghg


W = 10  # width of structure
L = 30  # length of structure
Hg, Hp = 5,8 # Gutter height, peak height
orientation = 45  # orientation of length relative to due north


#b1 = ghg.genBox(W,L,Hg)
b3 = ghg.genGableGH(W,L,Hg,Hp)
#bb3=ghg.rotateBox(b3,53.1)
#plotBoxPoints(rotateBox(b3,53.1),W,L,H)
#ghg.plotBoxLines(b3,W,L,Hg)

msgh = ghg.multiplySpans(b3,5)

ghg.removeWalls(msgh)
#msgh = ghg.rotateMSGH(msgh,53.1)
ghg.plotSpanLines(msgh,W,L,Hg)

ghg.countWalls(msgh)

