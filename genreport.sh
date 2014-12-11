#!/bin/bash
# get the name of the dataset
for dataset in `ls data/*.arff`
do
    dataset=$(basename $dataset)
    dataset="${dataset%.*}"
    cp template/template.latex sample/$dataset.latex
    cp template/Master.bib sample/Master.bib
    sed -i -e "s/@dataset@/${dataset}/g" sample/$dataset.latex
    latex sample/$dataset.latex
    bibtex sample/$dataset.aux
    pdflatex sample/$dataset.latex
    mv $dataset* sample
done
