#!/usr/bin/python3

# This program is designed to check IP Address from TOR Exit Node List against maxmind country list and output the list w/ DTG and Country

import re
import os
import datetime
import geoip2.database

#TODO Current DTG

def DTG(fname, fmt='%Y%m%d_%H:%M:%S{fname}'):
	return (datetime.datetime.now().strftime(fmt).format(fname=fname)

#TODO Go out and get the TOR Exit nodes list called 'torexnode'

str1 = ''
with open('tmp/TORExitNodeList','r') as f:
	for line in f:
		str1 += line

#TODO Parse the TOR Exit Node list to times and IPs (using RegEx)

pobj = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
mobj = re.findall(pobj, str1)


#TODO Check TOR Exit Node list against maxmind database

str2 = ''
reader = geoip2.database.Reader('tmp/maxmindDB.mmdb')
for i in range(len(mobj)):
	response = reader.country(mobj[i])
	iso = response.country.iso_code
	str2 += '%s : %s\n' %(iso, mobj[i])
with open(DTG('outFile1'),'a') as fout:
	fout.write(str2)

#TODO Output Node IP, DTG, and country to DTG_List


#TODO Remove all files created

os.remove('tmp/TORExitNodeList')
os.remove('tmp/maxmindDB.mmdb')
os.removedirs('tmp/')
