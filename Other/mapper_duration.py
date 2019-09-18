#!/usr/bin/python3

#Created on Apr 16, 2017
#This file contains the mapper step for the storm csv file
#@author: shenshuyin

import sys
from datetime import datetime 

id_list = set()
#input data from STDIN
for line in sys.stdin:
        line = line.strip().replace('"','')
        line = line.split(",")
        ID = line[6]
#        print("ID: ", ID)
        if ID in id_list:
                continue
        else:
                if line[8] =="CONNECTICUT":
                        id_list.add(ID)
                        
                        cz_name = line[15]
                        begin_time = datetime.strptime(line[17], '%m/%d/%Y %H:%M')
                        end_time = datetime.strptime(line[19], '%m/%d/%Y %H:%M')
                        duration = (end_time - begin_time).total_seconds()
                        hours = duration/3600
                        print ('%s\t%s' % (cz_name, hours))


