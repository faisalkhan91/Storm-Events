#!/usr/bin/python3

import sys
from datetime import datetime

storm_duration={}
#input data from STDIN
for line in sys.stdin:
        line = line.strip('')
        line = line.split('\t')

        cz_name = line[0]
        hours = float(line[1])
        #print(hours)
        if cz_name in storm_duration:
                storm_duration[cz_name] += hours                
        
        else:
                storm_duration[cz_name] = hours

for key in sorted(storm_duration, key = storm_duration.get, reverse = True):
        print('%s\t%f' % (key, storm_duration[key]))

