#!/bin/sh
# Simple example command line calls to weka
# for 5 different supervised learning methods
export CLASSPATH=./lib/weka.jar:./lib/libsvm.jar:$CLASSPATH
jython supervised.py data/iris.arff
