#!/usr/local/bin/python

import sys
import ds1054z
import time
import ds1054z.discovery
from ds1054z import DS1054Z


devices = ds1054z.discovery.discover_devices()

if len(devices) == 0:
    print "can't find scope"
    sys.exit(-1)
    
print devices[0]['ip']
scope = DS1054Z(devices[0]['ip'])
print scope.idn

while 1 == 1:

    # collect vmin and vmax from the first two channels on the scope
    # every 30 seconds.
    vmax1 = scope.get_channel_measurement(1,"vmax",type='CURRent')
    vmin1 = scope.get_channel_measurement(1,"vmin",type='CURRent')
    vmax2 = scope.get_channel_measurement(2,"vmax",type='CURRent')
    vmin2 = scope.get_channel_measurement(2,"vmin",type='CURRent')
    
    f = open("out.csv", "a+")
    print "%d,%s,%s,%s,%s" % (time.time() , vmin1, vmax2, vmin2, vmax2)
    print >> f, "%d,%s,%s,%s,%s" % (time.time() , vmin1, vmax1, vmin2, vmax2)
    f.close()

    time.sleep(30)
