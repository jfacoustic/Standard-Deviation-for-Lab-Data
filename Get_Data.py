#!/usr/bin/python
## The input for this should be a column of data
## Used in Standard_Deviation.py to calculate the standard deviation.

def getData(location, xData ):
    with open(location) as data:
        for line in data:

            tempNumAsStringX = ""

            for c in line:
                tempNumAsStringX += c

            xData.append( float(tempNumAsStringX) )

        return

## Copyright 2017 Joshua Mathews
## DWYWWI LICENSE:  THE DO WHATEVER YOU WANT WITH IT LICENSE MEANS YOU CAN
## DO WHATEVER YOU WANT WITH THIS CODE
