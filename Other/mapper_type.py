#!/usr/bin/python

#Created on Apr 16, 2017
#This file contains the mapper step for the storm csv file
#@author: shenshuyin

import sys

id_list = set()
#input data from STDIN
for line in sys.stdin:
        line = line.strip().replace('"','')
        line = line.split(",")
	ID = line[6]
	if ID in id_list:
		continue
	else:
        	if line[12]!="EVENT_TYPE":
                	id_list.add(ID)
			event_type = line[12]
                	print '%s' % (event_type)

