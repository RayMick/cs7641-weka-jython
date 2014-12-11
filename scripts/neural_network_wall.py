import sys
import os
import time

import java.io.FileReader as FileReader
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

import weka.classifiers.functions.MultilayerPerceptron as MultilayerPerceptron

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
datafile = FileReader(sys.argv[1] + ".arff")
data = Instances(datafile)
rand = Random()              # seed from the system time
data.randomize(rand)         # randomize data with number generator

# open output files
bufsize=0

datafile = "data/plot/" + str(os.path.splitext(os.path.basename(__file__))[0]) + "_" + \
   str(os.path.splitext(os.path.basename(sys.argv[1]))[0]) + "_rmse.csv"
file=open(datafile, 'w', bufsize)  # open a file for rmse data
file.write("epochs,rmse\n")

logfile = "logs/" + str(os.path.splitext(os.path.basename(__file__))[0]) + "_" + \
   str(os.path.splitext(os.path.basename(sys.argv[1]))[0]) + "_tunable.log"
log=open(logfile, 'w', bufsize) # open general log file

# loop for different number of training epochs
data.setClassIndex(data.numAttributes() - 1)
for num in range(1,1000,50):
   log.write("---------------------------------\nEpoch: " + str(num) + "\n")
   algo = MultilayerPerceptron()
   algo.setTrainingTime(num)
   x = time.time()
   algo.buildClassifier(data) 
   log.write("Time to build classifier: " + str(time.time() - x) + "\n")
   evaluation = Evaluation(data)
   output = PlainText()  # plain text output for predictions
   output.setHeader(data)
   buffer = StringBuffer() # buffer to use
   output.setBuffer(buffer)
   attRange = Range()                  # no additional attributes output
   outputDistribution = Boolean(False) # we don't want distribution
   x = time.time()
   #evaluation.evaluateModel(algo, data, [output, attRange, outputDistribution])
   evaluation.crossValidateModel(algo, data, 10, rand, [output, attRange, outputDistribution])
   log.write("Time to evaluate model: " + str(time.time() - x) + "\n")
   log.write(evaluation.toSummaryString())
   file.write(str(num) + "," + str(evaluation.rootMeanSquaredError()) + "\n")
file.close()
log.close()
