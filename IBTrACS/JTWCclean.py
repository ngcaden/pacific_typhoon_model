#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 14:04:45 2017

@author: theorashid
"""

import numpy as np
from netCDF4 import Dataset

#-----------------------------------------------------------------------------------------#
START_YEAR                  = 1951 
END_YEAR                    = 2010 
MAX_WIND_threshold_lifetime = 64 # unit: kt
MAX_WIND_threshold          = 0
#------------------------------------------------------------------------------------------#

nc_ibtracs = 'Allstorms.ibtracs_all.v03r09.nc'
ibt = Dataset(nc_ibtracs)

name = ibt.variables['name'][:]
genesis_basin = ibt.variables['genesis_basin'][:]
season = ibt.variables['season'][:]
time_record = ibt.variables['source_time'][:]
lat = ibt.variables['source_lat'][:]
lon = ibt.variables['source_lon'][:]
max_wind = ibt.variables['source_wind'][:] # dimensions (12755, 191, 26)
min_pres = ibt.variables['source_pres'][:]

# only JTWC data
for INDEX_RECORD_SOURCE in [10]:
    LAT = np.nan * np.ones(shape=(np.size(lat,0),np.size(lat,1)))
    LON = np.nan * np.ones(shape=(np.size(lat,0),np.size(lat,1)))
    MAX_WIND = np.nan * np.ones(shape=(np.size(lat,0),np.size(lat,1)))
    TIME_RECORD = np.nan * np.ones(shape=(np.size(lat,0),np.size(lat,1)))
    LAT      [:,:] = lat[:,:,INDEX_RECORD_SOURCE] # LAT 2 dims, JTWC data
    LON      [:,:] = lon[:,:,INDEX_RECORD_SOURCE]
    MAX_WIND [:,:] = max_wind[:,:,INDEX_RECORD_SOURCE] # dimensions (12755, 191)
    TIME_RECORD = time_record.data[:]
print LAT