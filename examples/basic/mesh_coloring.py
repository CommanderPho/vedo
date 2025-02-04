"""Specify a colors for cells
and points of a Mesh"""
from vedo import *

##################################### add a cell array
man1 = Mesh(dataurl+"man_low.vtk").lineWidth(0.1)
nv = man1.NCells()                         # nr. of cells
scals = range(nv)                          # coloring by the index of cell

man1.celldata["mycellscalars"] = scals    # add an array of scalars to mesh
man1.cmap("Paired", scals, on='cells').addScalarBar("cell nr")
show(man1, __doc__, at=0, N=3, axes=11, elevation=-60)


##################################### Point coloring
man2 = Mesh(dataurl+"man_low.vtk")
scals = man2.points()[:, 0] + 37           # pick x coordinates of vertices

man2.cmap("hot", scals)
man2.addScalarBar(horizontal=True)
show(man2, "mesh.cmap()", at=1)


##################################### Cell coloring
man3 = Mesh(dataurl+"man_low.vtk")
scals = man3.cellCenters()[:, 2] + 37      # pick z coordinates of cells
man3.cmap("afmhot", scals, on='cells')

# add a fancier 3D scalar bar embedded in the scene
man3.addScalarBar3D(s=[None,3])
man3.scalarbar.rotateX(90).y(0.2)
show(man3, "mesh.cmap(on='cells')", at=2).interactive().close()
