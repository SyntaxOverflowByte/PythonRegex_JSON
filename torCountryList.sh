#!/bin/bash

#declare -r dt=$(date +%d%H%M%b%Y)
#declare -r TORdt="TORExitNodeList_$dt"
mkdir tmp
wget -O 'tmp/TORExitNodeList' https://check.torproject.org/exit-addresses
wget -O 'tmp/maxmindDB.mmdb.gz' http://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.mmdb.gz
gunzip tmp/maxmindDB.mmdb.gz
python3 torPython.py
