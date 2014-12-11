#!/bin/bash
set -x
export CLASSPATH=./lib/weka3.7.11.jar:./lib/LibSVM1.0.6.jar:./lib/libsvm3.18.jar:$CLASSPATH
dataset=$1

# train as a function of datasize using a fixed testset
jython scripts/ada_boost_tunable.py $dataset
jython scripts/j48_tree_tunable.py $dataset
jython scripts/k_nearest_neighbor_tunable.py $dataset
jython scripts/support_vector_machine_tunable.py $dataset
jython scripts/neural_network_tunable.py $dataset
