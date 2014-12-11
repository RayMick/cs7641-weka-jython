#!/bin/bash
set -x
export CLASSPATH=./lib/weka3.7.11.jar:./lib/LibSVM1.0.6.jar:./lib/libsvm3.18.jar:$CLASSPATH
dataset=$1
crossvalidate=$2

# train as a function of datasize using a fixed testset
# argument one is the dataset and argument two is 1 if we want to cross validate and 0 otherwise
jython scripts/ada_boost.py $dataset $crossvalidate
jython scripts/j48_tree.py $dataset $crossvalidate
jython scripts/k_nearest_neighbor.py $dataset $crossvalidate
jython scripts/support_vector_machine.py $dataset $crossvalidate
jython scripts/neural_network.py $dataset $crossvalidate
