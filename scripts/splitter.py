import sys
import os
import time

import java.io.FileReader as FileReader
import java.io.File as File
import java.lang.String as String
import java.lang.StringBuffer as StringBuffer
import java.lang.Boolean as Boolean
import java.util.Random as Random

import weka.core.Instances as Instances
import weka.classifiers.Evaluation as Evaluation
import weka.core.Range as Range
import weka.core.SelectedTag as SelectedTag
import weka.core.Tag as Tag
import weka.classifiers.meta.FilteredClassifier as FilteredClassifier
import weka.filters.unsupervised.attribute.Remove as Remove
import weka.classifiers.evaluation.output.prediction.PlainText as PlainText
import weka.core.Utils.splitOptions as splitOptions
import weka.core.converters.ArffSaver as ArffSaver

"""
Commandline parameter(s):

    first parameter must be the ARFF file

"""

# check commandline parameters
if (not (len(sys.argv) == 2)):
    print "Usage: supervised.py <ARFF-file>"
    sys.exit()

# load data file
print "Loading data..."
datafile = FileReader(sys.argv[1])
data = Instances(datafile)
rand = Random()              # seed from the system time
data.randomize(rand)         # randomize data with number generator

# open output files
bufsize=0
dataname = str(os.path.splitext(os.path.basename(sys.argv[1]))[0])

# loop for different amounts of data with fixed test set
datasize = data.numInstances()
limit = (datasize*2)/3   # loop until we use 2/3 data as training set
testset = Instances(data,limit,datasize-limit)   # create training set using the last 1/3 of data
testset.setClassIndex(testset.numAttributes() - 1)

saver = ArffSaver()
saver.setInstances(testset)
testsetfile = "./data/files/" + dataname + "-" + "test.arff"
file = File(testsetfile)
saver.setFile(file)
saver.writeBatch()

trainset = Instances(data,0,limit)   # create training set
saver = ArffSaver()
saver.setInstances(trainset)
trainsetfile = "./data/files/" + dataname + "-" + "train.arff"
file = File(trainsetfile)
saver.setFile(file)
saver.writeBatch()
