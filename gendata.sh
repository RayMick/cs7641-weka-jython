#!/bin/bash
set -x
export CLASSPATH=./lib/weka3.7.11.jar:./lib/LibSVM1.0.6.jar:./lib/libsvm3.18.jar:$CLASSPATH
mkdir -p data/plot logs image
for dataset in `ls data/*train.arff`
do
   dataname=${dataset%-*}
   ./gendatatunableone.sh $dataname &
   ./gendataone.sh $dataname 0 &
   ./gendataone.sh $dataname 1 &
done
