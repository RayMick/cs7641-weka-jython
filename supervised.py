import sys

import java.io.FileReader as FileReader
import java.lang.String as String
import java.lang.StringBuffer as StringBuffer
import java.lang.Boolean as Boolean
import java.util.Random as Random

import weka.core.Instances as Instances
import weka.classifiers.Evaluation as Evaluation
import weka.core.Range as Range
import weka.classifiers.functions.LibSVM as LibSVM
import weka.classifiers.bayes.NaiveBayes as NaiveBayes
import weka.classifiers.bayes.BayesNet as BayesNet
import weka.classifiers.functions.MultilayerPerceptron as MultilayerPerceptron
import weka.classifiers.meta.AdaBoostM1 as AdaBoostM1
import weka.classifiers.trees.J48 as J48
import weka.classifiers.trees.RandomForest as RandomForest
import weka.classifiers.rules.JRip as JRip
import weka.classifiers.lazy.KStar as KStar
import weka.core.neighboursearch.LinearNNSearch as LinearNNSearch
import weka.core.SelectedTag as SelectedTag
import weka.core.Tag as Tag

"""
A simple example of using Weka classifiers from within Jython.
See algo_keys variable for list of classifiers used.
Code depends on a classifier having a buildClassifier() method
K-Nearest Neighbor does not so it not included.

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

# define the algorithms to be used.
algo_list = [(NaiveBayes(), 'NaiveBayes'), (BayesNet(),'BayesNet'), (J48(),'J48'), (JRip(), 'JRip'),
                 (KStar(), 'KStar'), (RandomForest(), 'RandomForest'), (AdaBoostM1(),'AdaBoostM1'),
                 (MultilayerPerceptron(),'MultilayerPerceptron'), (LibSVM(), 'LibSVM')]
algo_dict = dict([(x[1], x[0]) for x in algo_list])
algo_keys = ['NaiveBayes', 'J48', 'BayesNet', 'JRip', 'RandomForest', 'KStar', 'AdaBoostM1', 'LibSVM', 'MultilayerPerceptron']

# example to set kernal type on libsvm.  Default is 2
algo = algo_dict['LibSVM']
tag = SelectedTag("1",algo.TAGS_KERNELTYPE)  # 0 = linear, 1 = polynomial, 2 = radial basis function, 3 = sigmoid
algo.setKernelType(tag)

# train classifiers
print "Training classifiers..."
for key in algo_keys :
   algo = algo_dict[key]
   algo.buildClassifier(data)

# evaluate classifiers and print a result summary including confusion matrix
my_evaluations = []
for key in algo_keys :
   evaluation = Evaluation(data)
   algo = algo_dict[key]
   buffer = StringBuffer()             # buffer for the predictions
   attRange = Range()                  # no additional attributes output
   outputDistribution = Boolean(False) # we don't want distribution
   evaluation.evaluateModel(algo, data, [buffer, attRange, outputDistribution])
   my_evaluations.append(evaluation)
   print "------------------------------------"
   print algo.__class__.__name__
   print evaluation.toSummaryString()
   confusion_matrix = evaluation.confusionMatrix()  # confusion matrix
   print "Confusion Matrix:"
   for l in confusion_matrix:
       print '** ', ','.join('%2d'%int(x) for x in l)

# example to collect an individual statistic for all evaluated classifiers
print "------------------------------------"
print "Example to collect an individual statistic for all evaluated classifiers"
print "Kappa"
for index in range(len(algo_keys)):
   evaluation = my_evaluations[index]
   key = algo_keys[index]
   algo = algo_dict[key]
   print algo.__class__.__name__ + ": " + str(evaluation.kappa())

# Example K fold cross validate model against training data
# NOTE:  This should be done against test data not training data.
print "Cross validation with 10 folds"
for index in range(len(algo_keys)):
   evaluation = my_evaluations[index]
   key = algo_keys[index]
   algo = algo_dict[key]
   rand = Random(1)
   buffer = StringBuffer()             # buffer for the predictions
   attRange = Range()                  # no additional attributes output
   outputDistribution = Boolean(False) # we don't want distribution
   evaluation.crossValidateModel(algo, data, 10, rand, [buffer, attRange, outputDistribution])
