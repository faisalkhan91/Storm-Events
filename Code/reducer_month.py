#!/usr/bin/python

import sys

storm_month = {}
#input data from STDIN
for line in sys.stdin:
	#print line
	line = line.strip()
	line = line.split("\t")
	
#in the dictionary storm_month, state name is the key, value is a dictionary with the month name of the key
	state = line[0]
	month = line[1]
	m = 0
	if month == 'January':
                m  =1
        elif month == 'February':
        	m = 2
        elif month == 'March':       
                m = 3
        elif month == 'April':
		m = 4       
        elif month == 'May':
		m = 5
	elif month == 'June':
		m = 6
	elif month == 'July':
		m = 7
        elif month == 'August':
		m = 8
        elif month == 'September':
		m = 9
        elif month == 'October':
		m = 10
        elif month == 'November':
		m = 11
        elif month == 'December':
		m = 12
	if state in storm_month:
		storm_month[state][0] +=1
		storm_month[state][m] +=1
	else:
		storm_month[state]=[1,0,0,0,0,0,0,0,0,0,0,0,0]
		storm_month[state][m] = 1

for key in sorted(storm_month):
	print '%s\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d' % (key,storm_month[key][0],storm_month[key][1],storm_month[key][2],storm_month[key][3],storm_month[key][4],storm_month[key][5],storm_month[key][6],storm_month[key][7],storm_month[key][8],storm_month[key][9],storm_month[key][10],storm_month[key][11],storm_month[key][12])
