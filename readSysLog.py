# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 15:52:29 2023

@author: Blandfor
"""

import os
import time
from datetime import datetime as dt
import datetime
  

def extractFrameRate(l_syslogentries):
    #theis function takes the list of syslogentries created by 'readsyslogFile'
    #and creates a list of timebins with associated frmaerate
    # The line we are looking for in the syslogfile looks like this:
    # '2022/08/09 13:39:44.080  msg  ---> CPICS Elapsed Time: 00:05:03  Total Images: 3028  Total ROIs: 0  Saved ROIS: 0  Saved FF: 1'
    Date = 0
    Time = 1
    msg = 2
    CPICS = 6
    ElapsedTime = 9
    Total = 10
    TotalImages =10
    TotalRois = 13
    
    firstEntryFlag = True
    
    l_fps = []
    for line in l_syslogentries:
        l_line = line.split()
        if 'Total' in l_line:
            if len(l_line) > 19:

                currentNumberOfImages = l_line[TotalImages]

                currentTime = dt.strptime(l_line[Time][:-4], '%H:%M:%S')
                if firstEntryFlag:
                    lastNumberOfImages = currentNumberOfImages
                    lastTime = currentTime
                    firstEntryFlag = False
                else:
                    deltaTime = currentTime - lastTime
                    deltaNumberOfImages = int(currentNumberOfImages) - int(lastNumberOfImages)
                    fps = int(deltaNumberOfImages) / deltaTime.seconds
                    if fps <= 0:
                        print('NoNegs')
                        continue
                    meantime = lastTime + datetime.timedelta(seconds = deltaTime.seconds/2)

                    entryTime = dt.strftime(meantime, '%H:%M:%S')
                    
                    lastNumberOfImages = currentNumberOfImages
                    lastTime = currentTime
                    l_fps.append(str(entryTime + '\t' + str(fps)))
    return l_fps
                

def extractParamters(l_syslogentries):
    #thisfunctions extracts the paramters used for ROI extraction and returns 
    #them as a list of dictionaries. every change gets a new dictionary and is appended to the list
    # Example of the lines in the syslog file with changed parameters
    #2022/08/11 13:32:32.979  msg  CfgFile: ptgrey_cpics.cfg
    #2022/08/11 13:32:32.979  msg      IntThresh=2, AreaThresh=100, FocusThresh=0.7, ImgPadding=0.3
    #2022/08/11 13:32:32.980  msg      FrameRate=10, ShutterAutoMode=1, ShutterValue=10, GainAutoMode=0, GainValue=23, Gamma=0.5, Brightness=0.5, WhiteBalanceAutoMode=0, WhiteBalanceRed=600, WhiteBalanceBlue=850, SharpnessAutoMode=1, Sharpness=1000, StrobeDuration=.01
    #2022/08/11 13:32:32.980  msg      CalibPS=4.54, CalibDOF=12, CalibType=linear, CalibM=-2.4892, CalibB=2.3013, calcDDOF=0.559, calcVolume=0.069, calcSampleRate=0.690
    #2022/08/11 13:32:32.980  msg      AuxInstPortPwr=1, LogAuxInstData=1,  UVledPwr=1,  UVcameraPwr=1
    
    l_parameters = []
    Date = 0
    Time = 1    
    cfgFlag = False
    lineCount = 0
    parameterIndex = 3
    
    for line in l_syslogentries:
        l_line = line.split()
        print(lineCount)
        #print(l_line)
        if 'ptgrey_cpics.cfg' in l_line:
            cfgFlag = True
            print('found a cfg entry')
            i = 0
            lineCount = 0
            continue
            
        if cfgFlag:
            if lineCount == 0:
                print('firstLine')
                date = l_line[Date]
                print(l_line)
                print(l_line[Date])
                time = l_line[Time]
                i = parameterIndex
                print(l_line)
                IntThresh = l_line[i].split('=')[1].replace(',','')

                i += 1
                AreaThresh = l_line[i].split('=')[1].replace(',','') 
                i += 1
                FocusThresh= l_line[i].split('=')[1].replace(',','') 
                i += 1
                ImgPadding = l_line[i].split('=')[1].replace(',','')
                            
            if lineCount == 1:
                print('secondLine')
                print(l_line)
                i = parameterIndex
                FrameRate = l_line[i].split('=')[1].replace(',','')
                i += 1
                ShutterAutoMode = l_line[i].split('=')[1].replace(',','')
                i += 1
                ShutterValue = l_line[i].split('=')[1].replace(',','')
                i += 1
                GainAutoMode = l_line[i].split('=')[1].replace(',','')
                i += 1
                GainValue = l_line[i].split('=')[1].replace(',','')
                i += 1
                Gamma = l_line[i].split('=')[1].replace(',','')
                i += 1
                Brightness = l_line[i].split('=')[1].replace(',','')
                i += 1
                WhiteBalanceAutoMode = l_line[i].split('=')[1].replace(',','')
                i += 1
                WhiteBalanceRed = l_line[i].split('=')[1].replace(',','')
                i += 1
                WhiteBalanceBlue  = l_line[i].split('=')[1].replace(',','')
                i += 1
                SharpnessAutoMode = l_line[i].split('=')[1].replace(',','')
                i += 1
                Sharpness = l_line[i].split('=')[1].replace(',','')
                i += 1
                print(l_line)
                StrobeDuration = l_line[i].split('=')[1].replace(',','')
                              
            if lineCount == 2:
                print('thirdLine')
                i = parameterIndex
                CalibPS = l_line[i].split('=')[1].replace(',','')
                i += 1
                CalibDOF = l_line[i].split('=')[1].replace(',','')
                i += 1
                CalibType = l_line[i].split('=')[1].replace(',','')
                i += 1
                CalibM = l_line[i].split('=')[1].replace(',','')
                i += 1
                CalibB = l_line[i].split('=')[1].replace(',','')
                i += 1
                calcDDOF = l_line[i].split('=')[1].replace(',','')
                i += 1
                calcVolume = l_line[i].split('=')[1].replace(',','')
                i += 1
                calcSampleRate = l_line[i].split('=')[1].replace(',','')
                
                
            if lineCount == 3:
                print('fourthLine')

                i = parameterIndex
                AuxInstPortPwr = l_line[i].split('=')[1].replace(',','')
                i += 1
                LogAuxInstData = l_line[i].split('=')[1].replace(',','')
                i += 1
                UVledPwr = l_line[i].split('=')[1].replace(',','')
                i += 1
                UVcameraPwr = l_line[i].split('=')[1].replace(',','')
                cfgFlag = False
                
                dic_Paramters = {'Date':l_line[Date],
                                    'Time':l_line[Time],
                                    'IntThresh':IntThresh,
                                    'AreaThresh': AreaThresh,
                                    'FocusThresh':FocusThresh, 
                                    'ImgPadding':ImgPadding, 
                                    'FrameRate':FrameRate,
                                    'ShutterAutoMode':ShutterAutoMode,
                                    'ShutterValue':ShutterValue,
                                    'GainAutoMode':GainAutoMode,
                                    'GainValue':GainValue,
                                    'Gamma':Gamma,
                                    'Brightness':Brightness,
                                    'WhiteBalanceAutoMode':WhiteBalanceAutoMode,
                                    'WhiteBalanceRed':WhiteBalanceRed,
                                    'WhiteBalanceBlue':WhiteBalanceBlue, 
                                    'SharpnessAutoMode':SharpnessAutoMode,
                                    'Sharpness':Sharpness,
                                    'StrobeDuration':StrobeDuration,                             
                                    'CalibPS':CalibPS,
                                    'CalibDOF':CalibDOF,
                                    'CalibType':CalibType,
                                    'CalibM':CalibM,
                                    'CalibB': CalibB,
                                    'calcDDOF':calcDDOF,
                                    'calcVolume':calcVolume,
                                    'calcSampleRate':calcSampleRate,
                                    'AuxInstPortPwr':AuxInstPortPwr,
                                    'LogAuxInstData':LogAuxInstData,
                                    'UVledPwr':UVledPwr,
                                    'UVcameraPwr':UVcameraPwr} 
                l_parameters.append(dic_Paramters)
            lineCount += 1
    return l_parameters

def readSyslogFile(pathToSyslogFile):
    
    #this function will read  the given syslog file in the specified location and 
    #create an overview of the image segmentation parameters found and the 
    #fps per minute 
    #it requires os as import
    l_syslogentries = open(pathToSyslogFile).readlines()
    l_framerate = extractFrameRate(l_syslogentries)
    l_paramters = extractParamters(l_syslogentries)
    return l_paramters, l_framerate
        
# if __name__ == '__main__':
#     pathToSyslogs = os.path.join('G:\\','LOV', '2022_Disko', 'cpics', 'logs')
#     pathToSyslogFile = os.path.join(pathToSyslogs, '20220815.syslog.txt')
#     l_paramters, l_framerate  = readSyslogFile(pathToSyslogFile)
    