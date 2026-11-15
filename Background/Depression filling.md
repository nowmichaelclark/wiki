# Depression filling

---

In geographic information systems (GIS), **depression filling** is the step that removes depressions from a digital elevation model (DEM), a grid of ground heights, so that water routed across the grid can always flow off its edge. A depression, also called a pit or sink, is an area surrounded by higher ground with no outlet to lower ground. Some depressions are errors in the data and some are real, and the usual tools raise each one to the level at which it would spill.

The method was described by Jenson and Domingue in 1988, who raised the cells of each depression to the lowest point on its rim. Later work made the step faster. The Priority-Flood algorithm of Barnes, Lehman and Mulla, published in 2014, floods the grid inward from its edges with a priority queue, and it can also give each cell a small slope so that flat filled areas still drain. Other tools avoid filling and route flow through depressions with a least-cost search instead.

**Contents**

- 1 Definition
- 2 History
- 3 Priority-Flood
- 4 Alternatives to filling
- 5 References

## Definition

A depression in a DEM is an area surrounded by higher terrain, with no outlet to lower areas.[1] Jenson and Domingue called depressions "the nemesis" of methods that find the direction in which water flows across a DEM.[2] Esri's documentation for its Fill tool states that sinks and peaks are often errors caused by the resolution of the data or by rounding elevations to the nearest integer, and that sinks should be filled so that basins and streams can be delineated correctly.[3] The TauDEM documentation of Utah State University describes pits as low areas completely surrounded by higher terrain, and removes them by raising their elevation until they just drain off the domain.[4]

Filling a depression makes it level, as a fluid would fill it if the terrain did not let water soak in.[1] This is often a necessary step in preparing a DEM for analysis.[1] Not every depression is an error, and TauDEM treats pit removal as optional when the pits are real features of the landscape.[4]

## History

Jenson and Domingue, of the EROS Data Center in Sioux Falls, published a method in 1988 in which a conditioning phase produces three data sets from a DEM.[2] In that method, the cells inside each depression are raised to the lowest elevation on the rim of the depression.[2] The result is a depressionless DEM, in which every cell has a path to the edge of the data set.[2]

Planchon and Darboux published another algorithm in the journal *Catena* in 2002.[5] It is based on the approach of inundating, or flooding, the landscape.[6] John Lindsay's Whitebox GAT software implements the Planchon and Darboux method to fill all depressions and remove flat areas, and its documentation states that the method is less efficient than the one Wang and Liu proposed in 2006.[6]

Esri's Fill tool repeats its work until every sink within a chosen depth limit, called the z limit, is filled.[3] With a z limit of 100, for example, only sinks less than 100 meters deep are filled.[3] The same tool can also remove peaks, which are cells much higher than the surrounding surface suggests.[3]

## Priority-Flood

Barnes, Lehman and Mulla published Priority-Flood in *Computers & Geosciences* in 2014, as an algorithm that unifies and improves earlier work by several authors.[1] It floods the DEM inward from its edges, and a priority queue chooses the next cell to flood.[1] The output has no depressions and no digital dams, and every cell is guaranteed to drain.[1]

The authors describe the algorithm as optimal for both integer and floating-point data.[1] It takes time proportional to n for integer heights and to n log2 n for floating-point heights, where n is the number of cells.[1] A variation that fills the cells of a depression from a plain queue once the depression is found reaches m log2 m time, where m is never more than n, and it ran up to 37% faster than the original in their tests.[1] The paper's pseudocode is 20 lines long, and its C++ reference implementation is under a hundred lines.[1]

Priority-Flood works on irregular meshes and on grids where each cell has 4, 6, 8 or more neighbors.[1] It can also label watersheds and set flow directions, either by small increases in elevation or by carving through depressions.[1] In the reference implementation, the variant that fills with an increment raises each filled cell by an extra amount that is just enough to direct flow toward the edge of the DEM.[7] Another variant finds, for each cell, the cell on the edge of the DEM to which it drains.[7]

## Alternatives to filling

Filling changes the heights of the DEM, so some tools route water through depressions without raising them. The r.watershed module of GRASS GIS uses a least-cost search called A^T, and its manual states that the elevation map therefore does not need to be sink-filled.[8] The method comes from a 1989 paper by Ehlschlaeger on using the A^T search to build hydrologic models from elevation data.[8] Priority-Flood can also carve through depressions to set flow directions instead of filling them.[1]

## References

1. Barnes, Richard; Lehman, Clarence; Mulla, David (2014). ["Priority-flood: An optimal depression-filling and watershed-labeling algorithm for digital elevation models"](https://doi.org/10.1016/j.cageo.2013.04.024). *Computers & Geosciences*. 62: 117–127. doi:10.1016/j.cageo.2013.04.024.
2. Jenson, S. K.; Domingue, J. O. (1988). ["Extracting Topographic Structure from Digital Elevation Data for Geographic Information System Analysis"](https://www.asprs.org/wp-content/uploads/pers/1988journal/nov/1988_nov_1593-1600.pdf). *Photogrammetric Engineering and Remote Sensing*. 54 (11): 1593–1600.
3. ["How Fill works"](https://doc.esri.com/en/arcgis-pro/latest/tool-reference/spatial-analyst/how-fill-works.html). *ArcGIS Pro documentation*. Esri. Retrieved November 15, 2026.
4. ["D-Infinity Flow Directions"](https://hydrology.usu.edu/taudem/taudem5/help53/DInfinityFlowDirections.html). *TauDEM Tool Documentation*. Utah State University. Retrieved November 15, 2026.
5. Planchon, Olivier; Darboux, Frédéric (2002). ["A fast, simple and versatile algorithm to fill the depressions of digital elevation models"](https://doi.org/10.1016/S0341-8162(01)00164-3). *Catena*. 46 (2–3): 159–176. doi:10.1016/S0341-8162(01)00164-3.
6. Lindsay, John (2012). ["Fill depressions (Planchon and Darboux)"](https://jblindsay.github.io/ghrg/Whitebox/Help/FillDepressionsPandD.html). *Whitebox GAT help*. Retrieved November 15, 2026.
7. Barnes, Richard. ["Barnes2013-Depressions"](https://github.com/r-barnes/Barnes2013-Depressions). *GitHub*. Retrieved November 15, 2026.
8. ["r.watershed"](https://grass.osgeo.org/grass-stable/manuals/r.watershed.html). *GRASS GIS 8.5 Documentation*. GRASS Development Team. Retrieved November 15, 2026.

*Categories: Geographic information systems | Hydrology | Terrain algorithms*
