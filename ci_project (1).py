import pandas as pd
import numpy as np
import math
from math import sqrt

file_1 = pd.read_csv('1.csv')
file_2 = pd.read_csv('2.csv')
file_3 = pd.read_csv('3.csv')
file_4 = pd.read_csv('4.csv')
file_5 = pd.read_csv('5.csv')

#Drop the unnecessary columns
file_1.drop(file_1.columns[[0,1,2]], axis=1, inplace=True)
file_2.drop(file_2.columns[[0,1,2]], axis=1, inplace=True)
file_3.drop(file_3.columns[[0,1,2]], axis=1, inplace=True)
file_4.drop(file_4.columns[[0,1,2]], axis=1, inplace=True)
file_5.drop(file_5.columns[[0,1,2]], axis=1, inplace=True)

#Convert to numpy 
file_1 = file_1.values
file_2 = file_2.values
file_3 = file_3.values
file_4 = file_4.values
file_5 = file_5.values

def calculate_conf_interval(file_1):
  lower_boundclass0 = []
  lower_boundclass1 = []
  upper_boundclass1 =  []
  upper_boundclass0 = []
  class0=[]
  class1=[]
  for i in range(0,len(file_1)):
    if(file_1[i,20]==0):
      class0.append(i)
    else:
      class1.append(i)

  for i in range(0,len(file_1[0])-1):
    n0= len(class0)
    n1 = len(class1)
    class0_mean = 0
    class1_mean = 0
    for x in range(len(file_1)):
      if x in class0:
        class0_mean = class0_mean + file_1[x,i]
      else:
        class1_mean = class1_mean + file_1[x,i]
    
    #s_std is the standard deviation of the population 
    # class_mean is the mean of the corresponding samples of the 2 classes
    class0_mean = class0_mean/n0
    class1_mean = class1_mean/n1
    s_std = np.std(file_1[:,i])
    #1.96 is the value at confidence of 95%
    # These specify the ranges of confidence interval for both the samples of class 0 and class1.
    lower_boundclass0.append(class0_mean - 1.96*s_std/(n0**0.5))
    lower_boundclass1.append(class1_mean - 1.96*s_std/(n1**0.5))
    upper_boundclass0.append(class0_mean + 1.96*s_std/(n0**0.5))
    upper_boundclass1.append(class1_mean + 1.96*s_std/(n1**0.5))

calculate_conf_interval(file_2) # call the function with appropriate file argument