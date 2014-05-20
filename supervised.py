import sys

import java.io.FileReader as FileReader
import java.lang.String as String
import java.lang.StringBuffer as StringBuffer
import java.lang.Boolean as Boolean

import weka.core.Instances as Instances
import weka.classifiers.trees.J48 as J48
import weka.classifiers.functions.LibSVM as LibSVM
import weka.core.neighboursearch.LinearNNSearch as LinearNNSearch
import weka.classifiers.meta.AdaBoostM1 as AdaBoostM1
import weka.classifiers.functions.MultilayerPerceptron as MultilayerPerceptron
import weka.classifiers.Evaluation as Evaluation
import weka.core.Range as Range

"""
A simple example of using Weka classifiers from within Jython.
Following classifiers are used:  J48, SVM, Boost, Perceptron

Commandline parameter(s):

    first parameter must be the ARFF file

"""

# check commandline parameters
if (not (len(sys.argv) == 2)):
    print "Usage: supervised.py <ARFF-file>"
    sys.exit()

# load data file
print "Loading data..."
file = FileReader(sys.argv[1])
data = Instances(file)

# set the class Index - the index of the dependent variable
data.setClassIndex(data.numAttributes() - 1)

# create the models and put them in a classifier list
my_classifiers = []
mlp = MultilayerPerceptron()
my_classifiers.append(mlp)
j48 = J48()
my_classifiers.append(j48)
boost = AdaBoostM1()
my_classifiers.append(boost)
svm = LibSVM()
my_classifiers.append(svm)

# train classifiers
print "Training classifiers..."
for obj in my_classifiers :
   obj.buildClassifier(data)

# evaluate classifiers and print a result summary
my_evaluations = []
for obj in my_classifiers :
   evaluation = Evaluation(data)
   buffer = StringBuffer()             # buffer for the predictions
   attRange = Range()                  # no additional attributes output
   outputDistribution = Boolean(False) # we don't want distribution
   evaluation.evaluateModel(obj, data, [buffer, attRange, outputDistribution])
   my_evaluations.append(evaluation)
   print "------------------------------------"
   print obj.__class__.__name__
   print evaluation.toSummaryString()

# example to collect an individual statistic for all evaluated classifiers
print "Kappa"
for index in range(len(my_classifiers)):
   evaluation = my_evaluations[index]
   classifier = my_classifiers[index]
   print classifier.__class__.__name__ + ": " + str(evaluation.kappa())
