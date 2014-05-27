
Sample code for using jython with WEKA machine learning toolkit
for supervised learning classifiers on the iris dataset.


Requirements:  
java must be in path  
jython package should be installed.  For example:  apt-get install jython  


To run on linux, execute the script supervised.sh

For example:   
chmod 755 supervised.sh   
./supervised.sh  

Weka v3.6.11 is included

Sample output:

------------------------------------
MultilayerPerceptron

Correctly Classified Instances         148               98.6667 %  
Incorrectly Classified Instances         2                1.3333 %  
Kappa statistic                          0.98   
Mean absolute error                      0.0248  
Root mean squared error                  0.0911  
Relative absolute error                  5.5779 %  
Root relative squared error             19.3291 %  
Total Number of Instances              150  

------------------------------------
J48

Correctly Classified Instances         147               98      %  
Incorrectly Classified Instances         3                2      %  
Kappa statistic                          0.97   
Mean absolute error                      0.0233  
Root mean squared error                  0.108  
Relative absolute error                  5.2482 %  
Root relative squared error             22.9089 %  
Total Number of Instances              150  

------------------------------------
AdaBoostM1

Correctly Classified Instances         144               96      %  
Incorrectly Classified Instances         6                4      %  
Kappa statistic                          0.94   
Mean absolute error                      0.0587  
Root mean squared error                  0.1359  
Relative absolute error                 13.1994 %  
Root relative squared error             28.8203 %  
Total Number of Instances              150  

------------------------------------
LibSVM

Correctly Classified Instances         148               98.6667 %  
Incorrectly Classified Instances         2                1.3333 %  
Kappa statistic                          0.98   
Mean absolute error                      0.0089  
Root mean squared error                  0.0943  
Relative absolute error                  2      %  
Root relative squared error             20      %  
Total Number of Instances              150  

Kappa  
MultilayerPerceptron: 0.98  
J48: 0.97  
AdaBoostM1: 0.94  
LibSVM: 0.98  

![alt tag](https://raw.githubusercontent.com/omscs-georgia-tech/cs7641-weka-jython/master/iris-draftman-display.png)
