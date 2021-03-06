'''
Higher Dimensional Visualization Tool created by Kristen Bean June 15, 2018

A tool that allows for data to be visualized as it changes in dimensions beyond 3D. "Frames" are constructed
that allow for the user to select up three dimensional vectors, a label and a viewing range.

'''

import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

##from frame import Frame
##from event import *
##from vector import Vector
from hoppertransform import hopperTransform
from plot import twodimplot
from plot import threedimplot

vectors = []
events = []

##Write welcome to the program

def loadData():
    filename = input("Location of csv file to pull data from?\n")
    
    with open(filename, 'r') as rawdata:
        reader = csv.reader(rawdata, delimiter=',')
        for row in reader:
            tempRow = []
            for j in row:
                tempRow.append(int(j))
            vectors.append(tempRow)


def status():
    ##Check the status of vectors, frames and events
    print("Vectors found: ", len(vectors))
    counter = 1
    for i in vectors:
        print(counter, "\t", i[0:3])
        counter+=1
    print(len(events), " events found.")
    for j in events:
        print(j)

def frameStatus():
    print(len(frames), " frames found.")
    counter = 1
    for i in frames:
        print(counter, "\t", frames[0:5])
        i+=1

def createFrame():
    pass

def assignVariables():
    indInput = input("Input the independent variable(s) you wish to use (i.e. xyz or abc): ")
    indVar = list(indInput)
    print("Assign vectors (by their number, reference above) to independent variables:")
    i = 0
    while i < len(indVar):
        vecSelect = input(str(indVar[i]) + " = ")
        tempList = []
        tempList.append(indVar[i])
        tempList.append(vecSelect)
        indVar[i] = tempList
        i+=1
    depInput = input("Input the dependent variable(s) you wish to use: ")
    depVar = list(depInput)
    return(indVar, depVar)
   

def locateVariables(eq, varlist):
    ##Locate variables within the equation
    ##Returns the variables and locations in the format
    ##      [var, loc1, loc2, ...]
    locTrack = []
    for i in varlist:
        tempLoc = []
        tempLoc.append(i)
        j = 0
        while j < len(eq):
            if i == eq[j]:
                tempLoc.append(j)
                j+=1
            else:
                j+=1
        locTrack.append(tempLoc)
        print("temp location of var:", tempLoc)
    print("all locations found:", locTrack)
    return(locTrack)

def equationformat(eq):
    neweq = []
    for i in eq:
        try:
            i = int(i)
            neweq.append(i)
        except:
            neweq.append(i)
    return(neweq)

def createEvent():
    newevent = []
    print("Vectors that are currently available:")
    counter = 1
    for i in vectors:
        print(counter, "\t", i[0:5])
    variables = assignVariables()
    print(variables)
    indVar = variables[0]
    depVar = variables[1]
    ##eqInput = input("Your equation:")
    ##equationRaw = equationformat(eqInput)
    ##print(equationRaw)
    ##indVarLoc = locateVariables(equationRaw, indVar)
    ##depVarLoc = locateVariables(equationRaw, depVar)
    ##hopperTransform(indVarLoc, eqInput)
    if len(indVar) == 2:
        var = variables[0]
        xvar = var[0]
        yvar = var[1]
        xvec = int(xvar[1])-1
        yvec = int(yvar[1])-1
        twodimplot(vectors[xvec], vectors[yvec])
    elif len(indVar) == 3:
        ##threedimplot(variables)
        var = variables[0]
        xvar = var[0]
        yvar = var[1]
        zvar = var[2]
        xvec = int(xvar[1])-1
        yvec = int(yvar[1])-1
        zvec = int(zvar[1])-1
        print("xvec: ", vectors[xvec], "yvec: ", vectors[yvec], "zvec: ", vectors[zvec])
        threedimplot(xvec, yvec, zvec)
    else:
        pass


def interface():
        comm = input(">>>")
        if comm == "load data":
            loadData()
            interface()
        elif comm == "status":
            status()
            interface()
        elif comm == "help":
            appHelp()
            interface()
        elif comm == "create event":
            ##Creates a new event through the event function then adds it to the existing list of events
            newevent = createEvent()
            events.append(newevent)
            interface()
        elif comm == "delete event":
            deleteEvent()
            interface()
        elif comm == "run event":
            runEvent()
            interface()
        elif comm == "quit":
            print("Quitting program... \n")
        else:
            print("Command not understood, type 'help' for documentation")
            interface()

interface()
