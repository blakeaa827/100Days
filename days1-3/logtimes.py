'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('.', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    '''
       Given a log line extract its timestamp and convert it to a datetime object. 
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    timestamp = line.split(' ')[1]
    time_str = '%Y-%m-%dT%H:%M:%S'
    # timestamp = [int(x) for x in re.split(r'-|T|:', timestamp)]
    return datetime.strptime(timestamp, time_str)


def time_between_shutdowns(loglines):
    '''
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
       timedelta between the first and last one. 
       Return this datetime.timedelta object.'''
    timestamps = [convert_to_datetime(line) for line in loglines if 'Shutdown initiated' in line]
    return timestamps[-1] - timestamps[0]
