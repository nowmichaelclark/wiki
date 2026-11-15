# Surface nets

---

In computer graphics, **surface nets** are a method for building a triangle mesh of a surface from a three-dimensional grid of values, such as a medical scan or a signed distance field. Instead of placing triangles inside each grid cell, as marching cubes does, the method places one vertex in each cell that the surface crosses and joins the vertices of neighboring cells. Sarah Gibson introduced the method in 1998 to make smooth models of anatomy from segmented medical images.

Surface nets belong to the dual contouring family of methods, and Frisken has described them as possibly the first dual contouring method. In the original form, the vertices are moved in steps toward the average position of their neighbors to smooth the surface, while each vertex stays inside its own cell. Surface nets are available in the Visualization Toolkit and in open-source libraries that mesh grids in chunks.

**Contents**

- 1 History
- 2 Method
- 3 Relation to other methods
- 4 Implementations
- 5 References

## History

Sarah F. F. Gibson presented constrained elastic surface nets at the MICCAI 1998 conference on medical image computing, in a paper published in Springer's Lecture Notes in Computer Science.[1] A longer version appeared in 1999 as a technical report of Mitsubishi Electric Research Laboratories (MERL).[2] The report addresses the need of surgical simulation and computer-assisted surgery for computer models of patient anatomy.[2] Its input is binary segmented data, in which each grid point is marked as inside or outside a structure.[2] The report states that marching cubes surfaces built from such data still show terracing artifacts, even after the data is low-pass filtered.[2]

In 2022, Frisken, writing from Brigham and Women's Hospital, published a version of SurfaceNets for segmentations with many labels in the *Journal of Computer Graphics Techniques*.[3] That paper keeps sharp boundaries between labeled regions.[3]

## Method

A surface net starts with one node at the center of each surface cube, a grid cell that the surface passes through.[2] Each node can have up to six links, one to each of its right, left, top, bottom, front and back neighbors.[2] In the 2022 description, a vertex is created for each cell that intersects the surface.[3]

The net is then relaxed to reduce its energy. Each step moves a node toward a position equally far from its linked neighbors.[2] In the basic algorithm, each vertex moves in turn toward the average position of its neighbors.[3] A constraint keeps each node inside its original surface cube during this smoothing.[2] In Frisken's 2022 tests, total times ranged from under a second for hundreds of quads to 3.5 seconds for 800,000 quads.[3]

## Relation to other methods

Marching cubes, published by William Lorensen and Harvey Cline in 1987, builds triangle models of surfaces of constant density from 3D medical data.[4] It processes the data in scan-line order, uses a case table to set the triangles in each cell, and places triangle vertices by linear interpolation.[4] Surface nets instead place one vertex in each cell and connect the vertices of neighboring cells.[3] Frisken cites de Bruin and others (2000), who found that SurfaceNets gives smoother surfaces with better quality triangles than marching cubes.[3]

Dual contouring, described by Tao Ju, Frank Losasso, Scott Schaefer and Joe Warren in 2002, contours a signed grid whose edges carry Hermite data: the exact points where the surface crosses each edge, and the surface normals there.[5] It does not need to find and handle sharp features explicitly, and it can simplify the result with an octree without patching cracks.[5] Frisken notes that SurfaceNets is technically a dual contouring method, but unlike those methods it does not require Hermite data.[3]

## Implementations

The fast-surface-nets library for the Rust programming language, licensed under the MIT or Apache-2.0 licenses, meshes a signed distance field stored in a grid.[6] Its example meshes a chunk of 16 by 16 by 16 cells with one cell of padding on each side, in a grid of 18 by 18 by 18 samples.[6] The meshes of neighboring chunks fit together without gaps, because the library skips the faces on the positive boundaries of each chunk.[6] It estimates surface normals from the derivatives of the distance field.[6] Its documentation reports about 20 million triangles per second on one core of a 2.5 GHz Intel Core i7.[6]

The Visualization Toolkit (VTK) also offers SurfaceNets. The PyVista library uses it to extract the contours of labeled regions with sharp boundaries, with optional smoothing to reduce the staircase look, and this feature requires VTK 9.3.0 or later.[7]

## References

1. Gibson, Sarah F. F. (1998). ["Constrained elastic surface nets: Generating smooth surfaces from binary segmented data"](https://doi.org/10.1007/BFb0056277). *Medical Image Computing and Computer-Assisted Intervention — MICCAI'98*. Lecture Notes in Computer Science: 888–898. doi:10.1007/BFb0056277.
2. Gibson, Sarah F. F. (1999). ["Constrained Elastic Surface Nets: Generating Smooth Models from Binary Segmented Data"](https://www.merl.com/publications/docs/TR99-24.pdf). *Mitsubishi Electric Research Laboratories*. TR99-24.
3. Frisken, Sarah F. (2022). ["SurfaceNets for Multi-Label Segmentations with Preservation of Sharp Boundaries"](http://jcgt.org/published/0011/01/03/). *Journal of Computer Graphics Techniques*. 11 (1): 34–54.
4. Lorensen, William E.; Cline, Harvey E. (1987). ["Marching cubes: A high resolution 3D surface construction algorithm"](https://doi.org/10.1145/37402.37422). *ACM SIGGRAPH Computer Graphics*. 21 (4): 163–169. doi:10.1145/37402.37422.
5. Ju, Tao; Losasso, Frank; Schaefer, Scott; et al. (2002). ["Dual contouring of hermite data"](https://doi.org/10.1145/566654.566586). *ACM Transactions on Graphics*. 21 (3): 339–346. doi:10.1145/566654.566586.
6. ["fast_surface_nets"](https://docs.rs/fast-surface-nets/latest/fast_surface_nets/). *Docs.rs*. Retrieved November 15, 2026.
7. ["pyvista.ImageDataFilters.contour_labeled"](https://docs.pyvista.org/api/core/_autosummary/pyvista.imagedatafilters.contour_labeled). *PyVista documentation*. Retrieved November 15, 2026.

*Categories: Computer graphics | Isosurface algorithms | Mesh generation*
