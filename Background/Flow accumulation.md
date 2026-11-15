# Flow accumulation

---

In geographic information systems (GIS), **flow accumulation** is a grid computed from a digital elevation model (DEM) in which each cell holds the number of cells, or the total weight of the cells, whose water flows through it. It is computed from a flow direction grid, which says where water leaves each cell. Cells with high values lie along stream channels, and cells with a value of zero lie on ridges, so a threshold on flow accumulation gives a map of the drainage network.

The basic method, called D8, sends all the flow of a cell to the one of its eight neighbors with the steepest drop. Jenson and Domingue described this approach in 1988. Later methods split the flow between several neighbors: multiple flow direction (MFD) methods share it among all lower neighbors, and Tarboton's D-infinity method of 1997 shares it between two neighbors along a single angle of steepest descent.

**Contents**

- 1 Definition
- 2 Flow direction
- 3 Methods that split flow
- 4 Drainage networks
- 5 References

## Definition

Esri's documentation defines accumulated flow as the accumulated weight of all cells that flow into each downslope cell.[1] If no weight grid is given, each cell has a weight of one, and the value of a cell is the number of cells that flow into it.[1] Jenson and Domingue gave the same definition in 1988: each cell is assigned a value equal to the number of cells that flow to it.[2]

Cells with high flow accumulation are areas of concentrated flow and can be used to identify stream channels.[1] Cells with a flow accumulation of zero are local high points and can be used to identify ridges.[1] In the r.watershed module of GRASS GIS, the accumulation output holds the amount of overland flow that passes through each cell, and negative values mark cells that may receive runoff from outside the mapped region.[3]

## Flow direction

The flow direction of a cell is the direction in which water flows out of it.[2] In the D8 method, there are eight possible directions, one to each adjacent cell.[4] The chosen direction is the one of steepest descent, or maximum drop, from the cell, and the distance used to compute the drop is measured between cell centers, so diagonal neighbors are farther away.[4] Jenson and Domingue encoded each of the eight directions as a power of two.[2] Esri states that its D8 tool follows the approach of Jenson and Domingue.[4]

Depressions in the DEM break this method. If two cells flow into each other, they are sinks and have no defined flow direction, so Esri advises filling the sinks before the flow direction is computed.[4] Jenson and Domingue described depressions as "the nemesis" of flow direction methods, and their method first raises each depression to the lowest point on its rim.[2] The Priority-Flood algorithm of Barnes, Lehman and Mulla can set flow directions as part of filling, either by small increases in elevation or by carving through depressions.[5]

## Methods that split flow

D8 sends all flow in one direction, and Tarboton wrote in 1997 that restricting flow to eight possible directions introduces a bias from the grid.[6] In MFD methods, flow is shared among all downslope neighbors; Esri cites Qin and others, 2007, for its MFD option.[4] GRASS GIS offers both single flow direction (SFD, the same as D8) and MFD, and it recommends a convergence factor of 5, citing Holmgren (1994).[3] Lower convergence values spread the flow more widely, and higher values concentrate it, so that the result becomes more like SFD.[3]

Tarboton's D-infinity method represents flow direction as one angle, taken as the steepest downward slope on eight triangular facets centered on each grid point.[6] The flow is then shared between the two downslope cells according to how close the angle is to the direction of each cell.[6] Tarboton argued that this avoids both the grid bias of eight directions and the unrealistic spreading of methods that share flow according to slope.[6] The TauDEM software stores the angle in radians, counterclockwise from east.[7]

## Drainage networks

A drainage network is found by selecting the cells whose flow accumulation is above a threshold.[2] As the threshold value is increased, the network becomes less dense.[2] Jenson and Domingue found that when depressions are filled first, the selected cells form a fully connected network.[2]

## References

1. ["How Flow Accumulation works"](https://doc.esri.com/en/arcgis-pro/latest/tool-reference/spatial-analyst/how-flow-accumulation-works.html). *ArcGIS Pro documentation*. Esri. Retrieved November 15, 2026.
2. Jenson, S. K.; Domingue, J. O. (1988). ["Extracting Topographic Structure from Digital Elevation Data for Geographic Information System Analysis"](https://www.asprs.org/wp-content/uploads/pers/1988journal/nov/1988_nov_1593-1600.pdf). *Photogrammetric Engineering and Remote Sensing*. 54 (11): 1593–1600.
3. ["r.watershed"](https://grass.osgeo.org/grass-stable/manuals/r.watershed.html). *GRASS GIS 8.5 Documentation*. GRASS Development Team. Retrieved November 15, 2026.
4. ["How Flow Direction works"](https://doc.esri.com/en/arcgis-pro/latest/tool-reference/spatial-analyst/how-flow-direction-works.html). *ArcGIS Pro documentation*. Esri. Retrieved November 15, 2026.
5. Barnes, Richard; Lehman, Clarence; Mulla, David (2014). ["Priority-flood: An optimal depression-filling and watershed-labeling algorithm for digital elevation models"](https://doi.org/10.1016/j.cageo.2013.04.024). *Computers & Geosciences*. 62: 117–127. doi:10.1016/j.cageo.2013.04.024.
6. Tarboton, David G. (1997). ["A new method for the determination of flow directions and upslope areas in grid digital elevation models"](https://doi.org/10.1029/96WR03137). *Water Resources Research*. 33 (2): 309–319. doi:10.1029/96WR03137.
7. ["D-Infinity Flow Directions"](https://hydrology.usu.edu/taudem/taudem5/help53/DInfinityFlowDirections.html). *TauDEM Tool Documentation*. Utah State University. Retrieved November 15, 2026.

*Categories: Geographic information systems | Hydrology | Terrain algorithms*
