import sys
import os
import time

import java.io.FileReader as FileReader
import java.io.File as File
import java.lang.String as String
import java.lang.StringBuffer as StringBuffer
import java.lang.Boolean as Boolean
import java.util.Random as Random
from java.lang import System as javasystem

import weka.core.Instances as Instances
import weka.classifiers.Evaluation as Evaluation
import weka.core.Range as Range
import weka.core.SelectedTag as SelectedTag
import weka.core.Tag as Tag
import weka.classifiers.meta.FilteredClassifier as FilteredClassifier
import weka.filters.unsupervised.attribute.Remove as Remove
import weka.classifiers.evaluation.output.prediction.PlainText as PlainText
import weka.core.converters.ArffSaver as ArffSaver

import weka.classifiers.trees.J48 as J48

"""
Commandline parameter(s):

    first parameter must be the ARFF file

"""

# check commandline parameters
if (not (len(sys.argv) == 3)):
    print "Usage: supervised.py <ARFF-file> <Validation>"
    sys.exit()
crossvalidate = sys.argv[2]
rand = Random()              # seed from the system time

# load data file
print "Loading data..."
trainfile = FileReader(sys.argv[1] + "-train.arff")
print "Loading " + sys.argv[1] + "-train.arff"
testfile = FileReader(sys.argv[1] + "-test.arff")
print "Loading " + sys.argv[1] + "-test.arff"
fulltrainset = Instances(trainfile)
fulltrainset.setClassIndex(fulltrainset.numAttributes() - 1)
testset = Instances(testfile)
testset.setClassIndex(testset.numAttributes() - 1)

# open output files
bufsize=0
classifiername = str(os.path.splitext(os.path.basename(__file__))[0])
dataname = str(os.path.splitext(os.path.basename(sys.argv[1]))[0])
datafilelimit = "data/plot/" + classifiername + "_" + dataname + crossvalidate + "_instances.csv"
filelimit=open(datafilelimit, 'w', bufsize)
filelimit.write("instances,pctincorrecttest,pctincorrecttrain\n")
logfile = "logs/" + classifiername + "_" + dataname + crossvalidate + ".log"
log=open(logfile, 'w', bufsize) # open general log file

for num in range(10,fulltrainset.numInstances(),50):
   filelimit.write(str(num))
   trainset = Instances(fulltrainset,0,num)   # create training set 
   trainset.setClassIndex(trainset.numAttributes() - 1)
   log.write("---------------------------------\nTraining Set Size: " + str(trainset.numInstances()) + ", Test Set Size: " + str(testset.numInstances()) + ", Full data set size: " + str(fulltrainset.numInstances()) + "\n")
   for dataset in [testset, fulltrainset]:   
       algo = J48()
       algo.buildClassifier(trainset)
       evaluation = Evaluation(trainset)
       output = PlainText()  # plain text output for predictions
       output.setHeader(trainset)
       buffer = StringBuffer() # buffer to use
       output.setBuffer(buffer)
       attRange = Range()                  # no additional attributes output
       outputDistribution = Boolean(False) # we don't want distribution
       x = time.time()
       if (int(crossvalidate)):
           evaluation.crossValidateModel(algo, dataset, 10, rand, [output, attRange, outputDistribution])
       else:
           evaluation.evaluateModel(algo, dataset, [output, attRange, outputDistribution])
       log.write("Time to evaluate model: " + str(time.time() - x) + "\n")
       log.write(evaluation.toSummaryString())
       filelimit.write("," + str(evaluation.pctIncorrect()))
   filelimit.write("\n")
filelimit.close()
log.close()
