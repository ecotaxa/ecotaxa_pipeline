# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 09:41:34 2023

@author: Blandfor
"""

import os
import time
from datetime import datetime as dt
import shutil

from traceback import format_exc

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import cv2 as cv

import numpy as np

def auxFileHeader(ctdType = 'sbe37'):
    #this is an old file format, its no longer used
    Date  = 0
    Time  = 1
    Tempe = 2
    Cond = 3
    Press = 4
    Depth = 5
    Sal= 6
    S_Vel=7
    l_dens= 8
    return Date, Time, Tempe, Cond, Press, Depth, Sal, S_Vel, l_dens


def CreateCastOverView(pathAuxFile, currentFile):
    #creates daily files of the casts and calls the plotting routine to plot 
    #Depth vs time with the detected casts marked by vertical lines for 
    #quick and easy quality control
    
    Date, Time, Tempe, Cond, Press, Depth, Sal, S_Vel, l_dens = auxFileHeader()
    
    l_castEnd = []
    l_castStart = []
    l_time = []
    l_depth = []
    ll_ctd = []
    
    l_ctd = open(pathAuxFile).readlines()
    print('Processing: ', currentFile)
   
    for elements in l_ctd:
        #format the env data for further processing
        l_element = elements.replace(',', ' ').split()
        if len(l_element[0]) >= 12:
            #ignore lines that don't fit the format
            #print(l_element[0])
            pass
        elif len(l_element) != 9:
            #ignore lines with bogous data (happens at powercycles)
            pass
        else:   
            ll_ctd.append(elements.replace(',', ' ').split())        
    
    i = 0
    depth_last = 0.0
    flag_downcast = False
    flag_upcast = False
    for elements in ll_ctd:
        if ll_ctd[i][Time][6:8] == '60':
            print('Timedefect! Line will be modified: ', str(ll_ctd[i][Date] + ' ' + ll_ctd[i][Time]))
            #some timestamps have '60.000' seconds instead of a new minute
            l_time.append(dt.strptime(str(ll_ctd[i][Date] + ' ' + ll_ctd[i][Time][:6] + '00.000'), '%Y/%m/%d %H:%M:%S.%f'))
            pass
        else:
            l_time.append(dt.strptime(str(ll_ctd[i][Date] + ' ' + ll_ctd[i][Time]), '%Y/%m/%d %H:%M:%S.%f'))
        l_depth.append(float(ll_ctd[i][Depth]))
        if i < 11:
            pass
        elif l_depth[-10] >= 0.5 and depth_last >= l_depth[-10]:
            #print('DownCast')
            if not flag_downcast:
                flag_downcast = True
                l_castStart.append(l_time[-1])
        elif l_depth[-10] >= 50 and depth_last <= l_depth[-10]:
            #print('Upcast')
            flag_upcast = True
        if flag_downcast and flag_upcast and round(depth_last,0) == 0:
            #print('Cast completeted')
            flag_downcast = False
            flag_upcast  = False
            l_castEnd.append(l_time[-1])
            #print(l_castStart[-1])
            #print(l_castEnd[-1])             
        depth_last = l_depth[-1]
        i += 1 
    if not os.path.isdir('CastOverview'):
        os.mkdir('CastOverview')
    FileCasts = open(str('CastOverview\\CastList_' + currentFile), 'w')
    FileAllCasts = open(str('CastOverview\\CastList_all.txt'), 'a')
    i = 0
    for elements in l_castEnd:
        FileCasts.write(str(str(l_castStart[i]) + ',' + str(l_castEnd[i]) + ',' + '\n'))
        FileAllCasts.write(str(str(i) + ',' + dt.strftime(l_castStart[i],'%Y/%m/%d %H:%M:%S.%f') + ',' + dt.strftime(l_castEnd[i], '%Y/%m/%d %H:%M:%S.%f') + '\n'))
        i += 1
    FileCasts.close()  
    PlotCastOverview(l_time, l_depth, pathAuxFile, currentFile, l_castStart, l_castEnd)
    
def PlotCastOverview(l_time, l_depth, path, currentFile, l_castStart, l_castEnd):
    ##########################
    #####Plotting commands####
    ##########################
    fig, ax = plt.subplots()
    plt.xkcd()
    for elements in l_castStart:
        ax.axvline(x=elements, color='red')
    for elements in l_castEnd:
        ax.axvline(x=elements, color = 'black')
    if len(l_depth) != len(l_time):
        print('Smells like some kind of BULLSHIT')
        print('Nothing will be plottet for ', currentFile)
    else:
        ax.plot(l_time, l_depth)
        ax.xaxis.set_major_locator(mdates.HourLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        ax.grid(True)
        fig.autofmt_xdate()
        plt.xlabel('Time [UTC]')
        plt.ylabel('Depth [m]')
        fig.gca().invert_yaxis()
        dirpathpdf = 'CastOverview\\PDF'       
        dirpathpng = 'CastOverview\\PNG' 
        if os.path.isdir(dirpathpdf) != True:
            os.makedirs(dirpathpdf)
        if os.path.isdir(dirpathpng) != True:
            os.makedirs(dirpathpng)
        fig.savefig(str(dirpathpdf + '\\CastOverview_' + currentFile + '.pdf'))
        fig.savefig(str(dirpathpng + '\\CastOverview_' + currentFile + '.png'))
        plt.tight_layout()

    plt.close()   
    return True
     