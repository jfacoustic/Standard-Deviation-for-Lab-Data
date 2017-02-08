#!/usr/bin/python

import Get_Data as Data
import numpy as np

xData = []

dataFile = ""
dataFile = raw_input('Enter the name of the datafile to find the standard deviation (Blank for \'data.txt\'): \n')

if (dataFile == ""):
    dataFile = "data.txt"

Data.getData(dataFile, xData)

tempAvg = 0.0
count = 0
for n in xData:
    tempAvg += n
    count += 1
avg = tempAvg / count

tempSum = 0.0
count = 0
for n in xData:
    tempSum += pow(avg - n, 2)
    count += 1
stdDev = pow(tempSum / (count - 1), 0.5)

print avg
print stdDev
