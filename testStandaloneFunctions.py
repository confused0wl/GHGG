# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:25:17 2020

@author: me442
"""

import Greenhouse_gen as ghg
W = 4
H = 6
L = 10
a = ghg.Vertex(0,2,3)
b = ghg.Vertex(0,2,3)

R1 = ghg.Facet()
r1v1 =ghg.Vertex(0,0,0)
r1v2 = ghg.Vertex(W,0,0)
r1v3 = ghg.Vertex(W,0,H)
r1v4 = ghg.Vertex(0,0,H)
r1_list = [r1v1,r1v2,r1v3,r1v4]
R1.add_list_vtxs(r1_list)

R2 = ghg.Facet()
r2v1 =ghg.Vertex(0,0,0)
r2v2 = ghg.Vertex(W,0,0)
r2v3 = ghg.Vertex(W,0,H)
r2v4 = ghg.Vertex(0,0,H)
r2_list = [r2v1,r2v2,r2v3,r2v4]
R2.add_list_vtxs(r2_list)
#print(ghg.comparePoints(b,a))
ghg.compareFacets(R1,R1)


