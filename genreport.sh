#!/bin/sh
# get the name of the dataset
# sed ...
latex templates/template.latex
bibtex templates/template.aux
pdflatex templates/template.latex
