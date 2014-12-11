#!/bin/bash
set -x
export CLASSPATH=./lib/weka3.7.11.jar:./lib/LibSVM1.0.6.jar:./lib/libsvm3.18.jar:$CLASSPATH
mkdir -p data/plot logs image
for dataset in `ls data/*.arff`
do
   if [[ $dataset == *-train* ]]
   then
      echo "Do not process: $string"
   elif [[ $dataset == *-test* ]]
   then
      echo "Do not process: $string"
   else   
      jython ./scripts/splitter.py $dataset &
      echo "Processed $string"
   fi
   cp $dataset data/split
done
