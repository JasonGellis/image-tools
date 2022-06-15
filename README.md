# image-tools
Custom tools for working with images.

These tools started off as experiments with OpenCV for the [Palaeoanalytics project.] (https://github.com/alan-turing-institute/Palaeoanalytics)

1) The Pixulator will transform the pixels of an image based on its PPI/DPI and an associated scale. The Pixulator function is part of the [PyLithics Software Package.] (https://zenodo.org/record/5898149)

2) Symmetry tester. This simple tool takes the perimeter contour of an image, fills it, and then calculates a ration between top and bottom, and left and right halves. 