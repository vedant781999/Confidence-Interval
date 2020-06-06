# Confidence-Interval
This python code can be used to find 95% confidence interval of a dataset.

Here, we are given 5 files of data which contained 15 columns of relevant
data and were used to classify a column(bug) with bug=0 and bug>0 with
the help of the values given in 15 columns. 
Now our goal is to calculate the
95% CI for each column such that bug=0 and bug>0.

Algorithm to calculate CI:-

● First we do preprocessing of the files i.e., removing the irrelevant
columns and converting the file into appropriate data structure(numpy
array) so as to do calculations easily.

● Now for each column in the file, we divide the values of the column in
two lists based on the bug value( bug=0 and bug>0)

● Next we calculate the 95% CI range for both the lists based on the
formula given above and return the lower bound and upper bound of
the column that gives bug=0 and bug>0 for each column for that file.
