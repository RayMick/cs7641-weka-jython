
Scripting framework that will perform the following tasks for a dataset in the weka .arff file format:  
  * Split data into a fixed test set (1/3) and training set (2/3)
  * Evaluate data points
  * Generate plots of data
  * Create overall report that includes plots and references

[Here is a sample report](https://github.com/omscs-georgia-tech/cs7641-weka-jython/raw/master/sample/iris.pdf)

Uses Weka 3.7 which is included in the lib directory.   

Requirements (Sample for ubuntu installation given):  
java 1.7+ must be in path  
jython package should be installed.  (apt-get install jython)  
R is needed to generate plots.  (apt-get install r-base)  
Graphviz is used to generate the tree graph for j48.  (apt-get install graphviz)  
Latex is needed to generate the latex report. (apt-get install install texlive-full)   
Bibtex is used for references.  (apt-get install texlive-bibtex-extra)  

It is recommended you run through this tutorial with the iris dataset before attempting to use your own dataset.
When using your own dataset,  remove the iris.arff file and replace with your own .arff file.  It will process multiple .arff files in the data directroy into multiple reports.

Run split.sh to split your data into a training and testing set.  
For example:  
```
chmod 755 split.sh  
./split.sh  
```

This should create a split test and train dataset in the data/split directory.  The data records are randomized prior to the split.  It is not recommended to run the split multiple times as it will change your results.

Run gendata.sh to generate plot data.  
For example:   
```
chmod 755 gendata.sh   
./gendata.sh   
```

This script runs each supervised learning algorithm simultanously as a background process.  
NOTE: You need to check that the unix java processes terminate prior to moving on to the 
plotting step.

Run genplot.sh to generate plots  
For example:  
```
chmod 755 genplot.sh  
./genplot.sh  
```

Run genreport.sh to generate the latex pdf report  
For example:  
```
chmod 755 genreport.sh  
./genreport.sh  
```

Here are some sample images generated:

Visualizing a decision tree:

![alt text](https://raw.githubusercontent.com/omscs-georgia-tech/cs7641-weka-jython/master/sample/j48_tree_tunable_iris2_0.25.png "Graphical Decision Tree")

Finding an optimal K when using the K-Nearest Neighbors algorithm.

![alt text](https://raw.githubusercontent.com/omscs-georgia-tech/cs7641-weka-jython/master/sample/k_nearest_neighbor_tunable_iris_rmse.png "Finding Optimal K")
