"""Probe a voxel dataset at specified points
and plot a histogram of the values"""
from vedo import *
from vedo.pyplot import histogram
import numpy as np

vol = Volume(dataurl+'embryo.slc')

pts = np.random.rand(5000, 3)*256

mpts = probePoints(vol, pts).pointSize(3)

mpts.print()
# valid = mpts.pointdata['vtkValidPointMask']
scals = mpts.pointdata['SLCImage']

his = histogram(scals,  xtitle='probed voxel value', xlim=(5,100))

show([(vol, Axes(vol), mpts, __doc__), his], N=2, sharecam=False).close()
