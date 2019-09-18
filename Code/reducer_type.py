#!/usr/bin/python

import sys

storm_type = {}
#input data from STDIN
for line in sys.stdin:
        #print line
        line = line.strip()
	line = line.split("\t")
#in the dictionary storm_type, type name is the key, value is a dictionary with the times as value
        event_type = line[0]
	if event_type in storm_type:
		storm_type[event_type] +=1
	else:
		storm_type[event_type] =1

for key in sorted(storm_type, key = storm_type.get, reverse = True):
         print '%-20s\t%s' % (key,storm_type[key])


