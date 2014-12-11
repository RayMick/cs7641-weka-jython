
Sample code for using jython with WEKA machine learning toolkit  
for supervised learning classifiers on the iris dataset.  

Uses Weka 3.7.   

Requirements:  
java must be in path  
jython package should be installed.  For example:  apt-get install jython  
R is needed to generate plots 
Latex is needed to generate the latex report 

It is recommended you run through this tutorial with the iris dataset
before attempting to use your own dataset.  When using your own dataset,
remove the iris.arff file and replace with your own .arff file.

Run split.sh to split your data into a training and testing set. 
For example:
chmod 755 split.sh
./split.sh

This should create a split test and train dataset in the data/split directory.
The data records are randomized prior to the split.  It is not recommeneded to 
run the split multiple times as it will change your results.

Run gendata.sh to generate plot data.
For example:   
chmod 755 gendata.sh   
./gendata.sh  

This script runs each supervised learning algorithm simultanously as a background process. 
NOTE: You need to check that the unix java processes terminate prior to moving on to the 
plotting step

Run genplot.sh to generate plots 
For example: 
chmod 755 genplot.sh 
./genplot.sh 

Run genreport.sh to generate the latex pdf report 
For example: 
chmod 755 genreport.sh 
./genreport.sh 

