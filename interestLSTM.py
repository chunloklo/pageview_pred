from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from datetime import date

import inspect
import time

import numpy as np
import tensorflow as tf

import csv

#check time taken
import time
start_time = time.time()

#reads data, opens csv file
csvfile =  open('TimeSeriesPredictionTrain.csv')
reader = csv.reader(csvfile, delimiter=',')
startDate = date(1,1,1)

#initialize date arrays
deltaArr = np.empty([0, 2])
#for the number of rows in dates
for row in reader:
    #initialize dates
    prev_date = startDate
    for col in row:
        #for each date, split
        dat = col.split('|')
        dateArr = dat[0].split('-')

        #create current date object
        curr_date = date(int(dateArr[0]), int(dateArr[1]), int(dateArr[2]))


        #skip if it is the first date
        if (prev_date == startDate):
            prev_date = curr_date
            prev_views = dat[1]
            continue

        #add to views arr
        delta = curr_date - prev_date
        deltaArr = np.vstack([deltaArr, [delta.days, prev_views]])
        prev_date = curr_date
        prev_views = dat[1]

print(deltaArr)
print("--- %s seconds ---" % (time.time() - start_time))
#transform into data
# deltaArr = np.transpos(deltaArr)
# view = np.transpose(views)
# dat = np.vstack((deltaArr, views))



