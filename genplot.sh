#!/bin/bash
export CLASSPATH=./lib/weka3.7.11.jar:./lib/LibSVM1.0.6.jar:./lib/libsvm3.18.jar:$CLASSPATH
export LOGDIR=logs
mkdir -p image
mkdir -p $LOGDIR

# plot neural network data instances vs error
for dataset in `ls data/plot/*neural_network*instances*`
do
    R CMD BATCH "--args $dataset image/$(basename \"$dataset\" .csv\").png" scripts/instances_error.r $LOGDIR/$(basename \"$dataset\" .csv\")_plot.log
done

# plot neural network training time vs datasize
for dataset in `ls data/plot/*neural_network*traintime*`
do
    R CMD BATCH "--args $dataset image/$(basename \"$dataset\" .csv\").png" scripts/instances_time.r $LOGDIR/$(basename \"$dataset\" .csv\")_plot.log
done

# plot neural network training time vs datasize
for dataset in `ls data/plot/*neural_network*wall*`
do
    R CMD BATCH "--args $dataset image/$(basename \"$dataset\" .csv\").png" scripts/neural_network_wall.r $LOGDIR/$(basename \"$dataset\" .csv\")_plot.log
done

# plot neural network data
for dataset in `ls data/plot/*neural_network*rmse*`
do
    R CMD BATCH "--args $dataset image/$(basename \"$dataset\" .csv\").png" scripts/neural_network.r $LOGDIR/$(basename \"$dataset\" .csv\")_plot.log
done

# plot j48_tree instances vs error
for dataset in `ls data/plot/*j48_tree*instances*`
do
    R CMD BATCH "--args $dataset image/$(basename \"$dataset\" .csv\").png" scripts/instances_error.r $LOGDIR/$(basename \"$dataset\" .csv\")_plot.log
done

# plot j48_tree
for dataset in `ls data/plot/*j48_tree*rmse*`
do
    R CMD BATCH "--args $dataset image/$(basename \"$dataset\" .csv\").png" scripts/j48_tree.r $LOGDIR/$(basename \"$dataset\" .csv\")_plot.log
done

# plot k nearest neighbor instance vs error
for dataset in `ls data/plot/*k_nearest_neighbor*instances*`
do
    R CMD BATCH "--args $dataset image/$(basename \"$dataset\" .csv\").png" scripts/k_nearest_neighbor_instances.r $LOGDIR/$(basename \"$dataset\" .csv\")_plot.log
done

# plot k nearest neighbor
for dataset in `ls data/plot/*k_nearest_neighbor*rmse*`
do
    R CMD BATCH "--args $dataset image/$(basename \"$dataset\" .csv\").png" scripts/k_nearest_neighbor.r $LOGDIR/$(basename \"$dataset\" .csv\")_plot.log
done

# plot support vector machine instances vs error
for dataset in `ls data/plot/*support_vector_machine*instances*`
do
    R CMD BATCH "--args $dataset image/$(basename \"$dataset\" .csv\").png" scripts/support_vector_machine_instances.r $LOGDIR/$(basename \"$dataset\" .csv\")_plot.log
done

# plot support vector machine
for dataset in `ls data/plot/*support_vector_machine*rmse*`
do
    R CMD BATCH "--args $dataset image/$(basename \"$dataset\" .csv\").png" scripts/support_vector_machine.r $LOGDIR/$(basename \"$dataset\" .csv\")_plot.log
done

# plot ada boost instances vs error
for dataset in `ls data/plot/*ada_boost*instances*`
do
    R CMD BATCH "--args $dataset image/$(basename \"$dataset\" .csv\").png" scripts/instances_error.r $LOGDIR/$(basename \"$dataset\" .csv\")_plot.log
done

# plot ada boost time vs datasize
for dataset in `ls data/plot/*ada_boost*traintime*`
do
    R CMD BATCH "--args $dataset image/$(basename \"$dataset\" .csv\").png" scripts/instances_time.r $LOGDIR/$(basename \"$dataset\" .csv\")_plot.log
done

# plot ada boost time vs datasize
for dataset in `ls data/plot/*ada_boost*wall*`
do
    R CMD BATCH "--args $dataset image/$(basename \"$dataset\" .csv\").png" scripts/ada_boost_wall.r $LOGDIR/$(basename \"$dataset\" .csv\")_plot.log
done

# plot ada boost
for dataset in `ls data/plot/*ada_boost*rmse*`
do
    R CMD BATCH "--args $dataset image/$(basename \"$dataset\" .csv\").png" scripts/ada_boost.r $LOGDIR/$(basename \"$dataset\" .csv\")_plot.log
done

# Generate png from file file
for dotfile in `ls image/*.dot`
do
   dot -Tpng $dotfile > image/$(basename \"$dotfile\" .dot\").png
done
