#!/bin/sh
# example to convert an aarf file to csv and then make a draftman's plot of the data
# a png file is generated in the local directory
export CLASSPATH=./lib/weka.jar:./lib/libsvm.jar:$CLASSPATH
java -Xmx1500m weka.core.converters.CSVSaver -i data/iris.arff -o data/iris.csv
r < graph.r
