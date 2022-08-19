# This file contains different setup dictionaires for different download dataset
# Set All Orginal URL to .nc file, this can be alter in the download stage

# =================================== #
# init values
INIT_LAT_RANGE = [0,30]
INIT_LON_RANGE = [118,150]
INIT_ST_DATE = '(2022-04-25T12:00:00Z)'
INIT_ED_DATE = '(2022-04-30T12:00:00Z)'
# Special Case: SWAN got depth
INIT_DEPTH = [0.0,0.0]
# =================================== #
# Support Format
plain_format = ['.csv','.html','.htmlTable','.json',
                 '.mat','.graph','.nccsv',
                 '.tsv','.xhtml']

binary_format = ['.nc','.geotif','.kml','.pdf',
                 '.smallPdf','.largePdf','.png',
                 '.largePng','.transparentPng']

# =================================== #

'''
Dataset Name: NOAA/NCEP Global Forecast System (GFS) Atmospheric Model
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ncep_global.html
===================================
tmpsfc (surface air temperature, K)
tmp2m (air temperature at 2m, K)
ugrd10m (eastward wind velocity at 10m, m/s)
vgrd10m (northward wind velocity at 10m, m/s)
pratesfc (rainfall rate, kg m-2 s-1)
rh2m (relative humidity at 2m, %)
prmslmsl (mean sea level pressure, Pa)
dlwrfsfc (net downward longwave radiation flux, W m-2)
dswrfsfc (net downward shortwave radiation flux, W m-2)
'''
gfs_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ncep_global.nc?'

gfs_dict = {'tmpsfc': True,
            'tmp2m': True,
            'ugrd10m': True,
            'vgrd10m':True,
            'pratesfc':True,
            'rh2m':True,
            'prmslmsl':True,
            'dlwrfsfc':True,
            'dswrfsfc':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #

'''
Dataset Name: NOAA Coral Reef Watch Monthly Global 5-km Satellite Coral Bleaching Monitoring Products
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/dhw_5km_monthly.html
===================================
CRW_DHW (degree heating week, Celsius weeks)
CRW_HOTSPOT (coral bleaching hotspot, Celsius)
CRW_SST (sea surface temperature, Celsius)
'''
dhw5_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/dhw_5km_monthly.nc?'

dhw5_dict = {'CRW_DHW': True,
            'CRW_HOTSPOT': True,
            'CRW_SST': True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #

'''
Dataset Name: NOAA Coral Reef Watch Monthly Global 5-km Satellite Coral Bleaching Monitoring Products, Lon0360
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/dhw_5km_monthly_lon360.html
===================================
CRW_DHW (degree heating week, Celsius weeks)
CRW_HOTSPOT (coral bleaching hotspot, Celsius)
CRW_SST (sea surface temperature, Celsius)
'''
dhw5_l360_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/dhw_5km_monthly_lon360.nc?'

dhw5_l360_dict = {'CRW_DHW': True,
            'CRW_HOTSPOT': True,
            'CRW_SST': True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #

'''
Dataset Name: Weather Research and Forecasting (WRF) Regional Atmospheric Model: Maui-Oahu
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/wrf_mo.html
===================================
Tair (air temperature at 2m, Celsius)
Uwind (u-wind component at 10m, meter second-1)
Vwind (v-wind component at 10m, meter second-1)
rain (rainfall rate, kilogram meter-2 second-1)
Qair (surface air relative humidity, %)
Pair (surface air pressure, millibar)
lwrad_down (net longwave radiation flux, Watts meter-2)
swrad (solar shortwave radiation flux, Watts meter-2)
'''
wrf_mo_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/wrf_mo.ns?'

wrf_mo_dict = {'Tair': True,
            'Uwind': True,
            'Vwind': True,
            'rain':True,
            'Qair':True,
            'Pair':True,
            'lwrad_down':True,
            'swrad':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #

'''
Dataset Name: Weather Research and Forecasting (WRF) Regional Atmospheric Model: Samoa
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/wrf_samoa.html
===================================
Tair (air temperature at 2m, Celsius)
Uwind (u-wind component at 10m, meter second-1)
Vwind (v-wind component at 10m, meter second-1)
rain (rainfall rate, kilogram meter-2 second-1)
Qair (surface air relative humidity, %)
Pair (surface air pressure, millibar)
lwrad_down (net longwave radiation flux, Watts meter-2)
swrad (solar shortwave radiation flux, Watts meter-2)
'''
wrf_samoa_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/wrf_samoa.ns?'

wrf_samoa_dict = {'Tair': True,
            'Uwind': True,
            'Vwind': True,
            'rain':True,
            'Qair':True,
            'Pair':True,
            'lwrad_down':True,
            'swrad':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #

'''
Dataset Name: Weather Research and Forecasting (WRF) Regional Atmospheric Model: Oahu
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/wrf_oa.html
===================================
Tair (air temperature at 2m, Celsius)
Uwind (u-wind component at 10m, meter second-1)
Vwind (v-wind component at 10m, meter second-1)
rain (rainfall rate, kilogram meter-2 second-1)
Qair (surface air relative humidity, %)
Pair (surface air pressure, millibar)
lwrad_down (net longwave radiation flux, Watts meter-2)
swrad (solar shortwave radiation flux, Watts meter-2)
'''
wrf_oa_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/wrf_oa.ns?'

wrf_oa_dict = {'Tair': True,
            'Uwind': True,
            'Vwind': True,
            'rain':True,
            'Qair':True,
            'Pair':True,
            'lwrad_down':True,
            'swrad':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #

'''
Dataset Name: Weather Research and Forecasting (WRF) Regional Atmospheric Model: Main Hawaiian Islands
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/wrf_hi.html
===================================
Tair (air temperature at 2m, Celsius)
Uwind (u-wind component at 10m, meter second-1)
Vwind (v-wind component at 10m, meter second-1)
rain (rainfall rate, kilogram meter-2 second-1)
Qair (surface air relative humidity, %)
Pair (surface air pressure, millibar)
lwrad_down (net longwave radiation flux, Watts meter-2)
swrad (solar shortwave radiation flux, Watts meter-2)
'''
wrf_hi_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/wrf_hi.ns?'

wrf_hi_dict = {'Tair': True,
            'Uwind': True,
            'Vwind': True,
            'rain':True,
            'Qair':True,
            'Pair':True,
            'lwrad_down':True,
            'swrad':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #

'''
Dataset Name: Weather Research and Forecasting (WRF) Regional Atmospheric Model: Guam
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/wrf_guam.html
===================================
Tair (air temperature at 2m, Celsius)
Uwind (u-wind component at 10m, meter second-1)
Vwind (v-wind component at 10m, meter second-1)
rain (rainfall rate, kilogram meter-2 second-1)
Qair (surface air relative humidity, %)
Pair (surface air pressure, millibar)
lwrad_down (net longwave radiation flux, Watts meter-2)
swrad (solar shortwave radiation flux, Watts meter-2)
'''
wrf_guam_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/wrf_guam.ns?'

wrf_guam_dict = {'Tair': True,
            'Uwind': True,
            'Vwind': True,
            'rain':True,
            'Qair':True,
            'Pair':True,
            'lwrad_down':True,
            'swrad':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #

'''
Dataset Name: Weather Research and Forecasting (WRF) Regional Atmospheric Model: CNMI
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/wrf_cnmi.html
===================================
Tair (air temperature at 2m, Celsius)
Uwind (u-wind component at 10m, meter second-1)
Vwind (v-wind component at 10m, meter second-1)
rain (rainfall rate, kilogram meter-2 second-1)
Qair (surface air relative humidity, %)
Pair (surface air pressure, millibar)
lwrad_down (net longwave radiation flux, Watts meter-2)
swrad (solar shortwave radiation flux, Watts meter-2)
'''
wrf_cnmi_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/wrf_cnmi.ns?'

wrf_cnmi_dict = {'Tair': True,
            'Uwind': True,
            'Vwind': True,
            'rain':True,
            'Qair':True,
            'Pair':True,
            'lwrad_down':True,
            'swrad':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #

'''
Dataset Name: NOAA Coral Reef Watch Operational Daily Near-Real-Time Global 5-km Satellite Coral Bleaching Monitoring Products
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/dhw_5km.html
===================================
CRW_BAA_mask (CRW_BAA pixel characteristics flag array, 1)
CRW_BAA_7D_MAX (bleaching alert area 7-day maximum composite, 1)
CRW_BAA_7D_MAX_mask (CRW_BAA_7D_MAX pixel characteristics flag array, 1)
CRW_DHW (degree heating week, Celsius weeks)
CRW_DHW_mask (CRW_DHW pixel characteristics flag array, 1)
CRW_HOTSPOT (coral bleaching hotspot, Celsius)
CRW_HOTSPOT_mask (CRW_HOTSPOT pixel characteristics flag array, 1)
CRW_SEAICE (sea ice fraction, 1)
CRW_SST (sea surface temperature, Celsius)
CRW_SSTANOMALY (sea surface temperature anomaly, Celsius)
CRW_SSTANOMALY_mask (CRW_SSTANOMALY pixel characteristics flag array, 1)
'''
dhw5km_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/dhw_5km.ns?'

dhw5km_dict = {'CRW_BAA_mask': True,
            'CRW_BAA_7D_MAX': True,
            'CRW_BAA_7D_MAX_mask': True,
            'CRW_DHW':True,
            'CRW_DHW_mask':True,
            'CRW_HOTSPOT':True,
            'CRW_HOTSPOT_mask':True,
            'CRW_SEAICE':True,
            'CRW_SST':True,
            'CRW_SSTANOMALY':True,
            'CRW_SSTANOMALY_mask':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

'''
Dataset Name: NOAA Coral Reef Watch Operational Daily Near-Real-Time Global 5-km Satellite Coral Bleaching Monitoring Products, Lon0360
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/dhw_5km_lon360.html
===================================
CRW_BAA_mask (CRW_BAA pixel characteristics flag array, 1)
CRW_BAA_7D_MAX (bleaching alert area 7-day maximum composite, 1)
CRW_BAA_7D_MAX_mask (CRW_BAA_7D_MAX pixel characteristics flag array, 1)
CRW_DHW (degree heating week, Celsius weeks)
CRW_DHW_mask (CRW_DHW pixel characteristics flag array, 1)
CRW_HOTSPOT (coral bleaching hotspot, Celsius)
CRW_HOTSPOT_mask (CRW_HOTSPOT pixel characteristics flag array, 1)
CRW_SEAICE (sea ice fraction, 1)
CRW_SST (sea surface temperature, Celsius)
CRW_SSTANOMALY (sea surface temperature anomaly, Celsius)
CRW_SSTANOMALY_mask (CRW_SSTANOMALY pixel characteristics flag array, 1)
'''
dhw5km_l360_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/dhw_5km_lon360.ns?'

dhw5km_l360_dict = {'CRW_BAA_mask': True,
            'CRW_BAA_7D_MAX': True,
            'CRW_BAA_7D_MAX_mask': True,
            'CRW_DHW':True,
            'CRW_DHW_mask':True,
            'CRW_HOTSPOT':True,
            'CRW_HOTSPOT_mask':True,
            'CRW_SEAICE':True,
            'CRW_SST':True,
            'CRW_SSTANOMALY':True,
            'CRW_SSTANOMALY_mask':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: NOAA/NCEP Global Forecast System (GFS) Atmospheric Model, Lon+/-180
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ncep_global_lon180.html
===================================
tmpsfc (surface air temperature, K)
tmp2m (air temperature at 2m, K)
ugrd10m (eastward wind velocity at 10m, m/s)
vgrd10m (northward wind velocity at 10m, m/s)
pratesfc (rainfall rate, kg m-2 s-1)
rh2m (relative humidity at 2m, %)
prmslmsl (mean sea level pressure, Pa)
dlwrfsfc (net downward longwave radiation flux, W m-2)
dswrfsfc (net downward shortwave radiation flux, W m-2)
'''
gfs_l180_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ncep_global_lon180.nc?'

gfs_l180_dict = {'tmpsfc': True,
            'tmp2m': True,
            'ugrd10m': True,
            'vgrd10m':True,
            'pratesfc':True,
            'rh2m':True,
            'prmslmsl':True,
            'dlwrfsfc':True,
            'dswrfsfc':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: NOAA/NCEP Global Forecast System (GFS) Atmospheric Model: Pacific
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ncep_pac.html
===================================
tmpsfc (surface air temperature, K)
tmp2m (air temperature at 2m, K)
ugrd10m (eastward wind velocity at 10m, m/s)
vgrd10m (northward wind velocity at 10m, m/s)
pratesfc (rainfall rate, kg m-2 s-1)
rh2m (relative humidity at 2m, %)
prmslmsl (mean sea level pressure, Pa)
dlwrfsfc (net downward longwave radiation flux, W m-2)
dswrfsfc (net downward shortwave radiation flux, W m-2)
'''
gfs_pac_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ncep_pac.nc?'

gfs_pac_dict = {'tmpsfc': True,
            'tmp2m': True,
            'ugrd10m': True,
            'vgrd10m':True,
            'pratesfc':True,
            'rh2m':True,
            'prmslmsl':True,
            'dlwrfsfc':True,
            'dswrfsfc':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: NOAA/NCEP Global Forecast System (GFS) Atmospheric Model: Pacific, Lon+/-180
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ncep_pac_lon180.html
===================================
tmpsfc (surface air temperature, K)
tmp2m (air temperature at 2m, K)
ugrd10m (eastward wind velocity at 10m, m/s)
vgrd10m (northward wind velocity at 10m, m/s)
pratesfc (rainfall rate, kg m-2 s-1)
rh2m (relative humidity at 2m, %)
prmslmsl (mean sea level pressure, Pa)
dlwrfsfc (net downward longwave radiation flux, W m-2)
dswrfsfc (net downward shortwave radiation flux, W m-2)
'''
gfs_pac_l180_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ncep_pac_lon180.nc?'

gfs_pac_l180_dict = {'tmpsfc': True,
            'tmp2m': True,
            'ugrd10m': True,
            'vgrd10m':True,
            'pratesfc':True,
            'rh2m':True,
            'prmslmsl':True,
            'dlwrfsfc':True,
            'dswrfsfc':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: Regional Ocean Modeling System (ROMS): CNMI: 2-D Variables
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_mari_ssh.html
===================================
zeta (free-surface, meter)
'''
roms2d_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_mari_ssh.nc?'

roms2d_dict = {'zeta': True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: Regional Ocean Modeling System (ROMS): CNMI: Data Assimilating: 2-D Variables
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_mari_assim_ssh.html
===================================
zeta (free-surface, meter)
'''
roms2d_as_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_mari_assim_ssh.nc?'

roms2d_as_dict = {'zeta': True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: Regional Ocean Modeling System (ROMS): CNMI: 3-D Variables
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_mari.html
===================================
temp (potential temperature, Celsius)
salt (salinity, 1e-3)
u (u-velocity component, meter second-1)
v (v-velocity component, meter second-1)
'''
roms3d_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_mari.nc?'

roms3d_dict = {'temp': True,
            'salt':True,
            'u':True,
            'v':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: Regional Ocean Modeling System (ROMS): CNMI: Data Assimilating: 3-D Variables
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_mari_assim.html
===================================
temp (potential temperature, Celsius)
salt (salinity, 1e-3)
u (u-velocity component, meter second-1)
v (v-velocity component, meter second-1)
'''
roms3d_as_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_mari_assim.nc?'

roms3d_as_dict = {'temp': True,
            'salt':True,
            'u':True,
            'v':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: Regional Ocean Modeling System (ROMS): Guam: 2-D Variables
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_marig_ssh.html
===================================
zeta (free-surface, meter)
'''
romsg2d_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_marig_ssh.nc?'

romsg2d_dict = {'zeta': True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: Regional Ocean Modeling System (ROMS): Guam: 3-D Variables
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_marig.html
===================================
temp (potential temperature, Celsius)
salt (salinity, 1e-3)
u (u-velocity component, meter second-1)
v (v-velocity component, meter second-1)
'''
romsg3d_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_marig.nc?'

romsg3d_dict = {'temp': True,
            'salt':True,
            'u':True,
            'v':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: Regional Ocean Modeling System (ROMS): Oahu South Shore: 2-D Variables
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiomsg_ssh.html
===================================
zeta (free-surface, meter)
'''
romsos2d_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiomsg_ssh.nc?'

romsos2d_dict = {'zeta': True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: Regional Ocean Modeling System (ROMS): Oahu South Shore: 3-D Variables
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiomsg.html
===================================
temp (potential temperature, Celsius)
salt (salinity, 1e-3)
u (u-velocity component, meter second-1)
v (v-velocity component, meter second-1)
'''
romsos3d_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiomsg.nc?'

romsos3d_dict = {'temp': True,
            'salt':True,
            'u':True,
            'v':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: Regional Ocean Modeling System (ROMS): Samoa: 2-D Variables
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_samoa_ssh.html
===================================
zeta (free-surface, meter)
'''
romssa2d_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_samoa_ssh.nc?'

romssa2d_dict = {'zeta': True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: Regional Ocean Modeling System (ROMS): Samoa: 3-D Variables
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_samoa.html
===================================
temp (potential temperature, Celsius)
salt (salinity, 1e-3)
u (u-velocity component, meter second-1)
v (v-velocity component, meter second-1)
'''
romssa3d_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_samoa.nc?'

romssa3d_dict = {'temp': True,
            'salt':True,
            'u':True,
            'v':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: Regional Ocean Modeling System (ROMS): Samoa: Data Assimilating: 2-D Variables
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_samoa_assim_ssh.html
===================================
zeta (free-surface, meter)
'''
romssa2d_as_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_samoa_assim_ssh.nc?'

romssa2d_as_dict = {'zeta': True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: Regional Ocean Modeling System (ROMS): Samoa: Data Assimilating: 3-D Variables
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_samoa_assim.html
===================================
temp (potential temperature, Celsius)
salt (salinity, 1e-3)
u (u-velocity component, meter second-1)
v (v-velocity component, meter second-1)
'''
romssa3d_as_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_samoa_assim.nc?'

romssa3d_as_dict = {'temp': True,
            'salt':True,
            'u':True,
            'v':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: Regional Ocean Modeling System (ROMS): Main Hawaiian Islands: 2-D Variables
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiig_ssh.html
===================================
zeta (free-surface, meter)
'''
romshi2d_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiig_ssh.nc?'

romshi2d_dict = {'zeta': True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: Regional Ocean Modeling System (ROMS): Main Hawaiian Islands: 3-D Variables
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiig.html
===================================
temp (potential temperature, Celsius)
salt (salinity, 1e-3)
u (u-velocity component, meter second-1)
v (v-velocity component, meter second-1)
'''
romshi3d_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiig.nc?'

romshi3d_dict = {'temp': True,
            'salt':True,
            'u':True,
            'v':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: Regional Ocean Modeling System (ROMS): Main Hawaiian Islands: Data Assimilating: 2-D Variables
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiig_assim_ssh.html
===================================
zeta (free-surface, meter)
'''
romshi2d_as_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiig_assim_ssh.nc?'

romshi2d_as_dict = {'zeta': True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: Regional Ocean Modeling System (ROMS): Main Hawaiian Islands: Data Assimilating: 3-D Variables
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiig_assim.html
===================================
temp (potential temperature, Celsius)
salt (salinity, 1e-3)
u (u-velocity component, meter second-1)
v (v-velocity component, meter second-1)
'''
romshi3d_as_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiig_assim.nc?'

romshi3d_as_dict = {'temp': True,
            'salt':True,
            'u':True,
            'v':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: Regional Ocean Modeling System (ROMS): Main Hawaiian Islands: Reanalysis: 2-D
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiig_reanalysis_ssh.html
===================================
zeta (free-surface, meter)
'''
romshi2d_re_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiig_reanalysis_ssh.nc?'

romshi2d_re_dict = {'zeta': True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: Regional Ocean Modeling System (ROMS): Main Hawaiian Islands: Reanalysis: 3-D
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiig_reanalysis.html
===================================
temp (potential temperature, Celsius)
salt (salinity, 1e-3)
u (u-velocity component, meter second-1)
v (v-velocity component, meter second-1)
'''
romshi3d_re_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiig_reanalysis.nc?'

romshi3d_re_dict = {'temp': True,
            'salt':True,
            'u':True,
            'v':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE
            }

# =================================== #
'''
Dataset Name: Simulating WAves Nearshore (SWAN) Regional Wave Model: Big Island
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_bigi.html
===================================
mdir (mean wave direction, degrees)
mper (mean wave period, second)
pdir (peak wave direction, degrees)
pper (peak wave period, second)
shgt (significant wave height, meters)
'''
swanbg_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_bigi.nc?'

swanbg_dict = {'mdir': True,
            'mper':True,
            'pdir':True,
            'pper':True,
            'shgt':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: Simulating WAves Nearshore (SWAN) Regional Wave Model: Guam
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_guam.html
===================================
mdir (mean wave direction, degrees)
mper (mean wave period, second)
pdir (peak wave direction, degrees)
pper (peak wave period, second)
shgt (significant wave height, meters)
'''
swangu_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_guam.nc?'

swangu_dict = {'mdir': True,
            'mper':True,
            'pdir':True,
            'pper':True,
            'shgt':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: Simulating WAves Nearshore (SWAN) Regional Wave Model: Guam: Apra Harbor
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_apra.html
===================================
mdir (mean wave direction, degrees)
mper (mean wave period, second)
pdir (peak wave direction, degrees)
pper (peak wave period, second)
shgt (significant wave height, meters)
'''
swanap_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_apra.nc?'

swanap_dict = {'mdir': True,
            'mper':True,
            'pdir':True,
            'pper':True,
            'shgt':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: Simulating WAves Nearshore (SWAN) Regional Wave Model: Kauai
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_kauai.html
===================================
mdir (mean wave direction, degrees)
mper (mean wave period, second)
pdir (peak wave direction, degrees)
pper (peak wave period, second)
shgt (significant wave height, meters)
'''
swanka_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_kauai.nc?'

swanka_dict = {'mdir': True,
            'mper':True,
            'pdir':True,
            'pper':True,
            'shgt':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: Simulating WAves Nearshore (SWAN) Regional Wave Model: Manua, American Samoa
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_manua.html
===================================
mdir (mean wave direction, degrees)
mper (mean wave period, second)
pdir (peak wave direction, degrees)
pper (peak wave period, second)
shgt (significant wave height, meters)
'''
swanma_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_manua.nc?'

swanma_dict = {'mdir': True,
            'mper':True,
            'pdir':True,
            'pper':True,
            'shgt':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: Simulating WAves Nearshore (SWAN) Regional Wave Model: Maui
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_maui.html
===================================
mdir (mean wave direction, degrees)
mper (mean wave period, second)
pdir (peak wave direction, degrees)
pper (peak wave period, second)
shgt (significant wave height, meters)
'''
swanmaui_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_maui.nc?'

swanmaui_dict = {'mdir': True,
            'mper':True,
            'pdir':True,
            'pper':True,
            'shgt':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: Simulating WAves Nearshore (SWAN) Regional Wave Model: Oahu
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_oahu.html
===================================
mdir (mean wave direction, degrees)
mper (mean wave period, second)
pdir (peak wave direction, degrees)
pper (peak wave period, second)
shgt (significant wave height, meters)
'''
swanoh_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_oahu.nc?'

swanoh_dict = {'mdir': True,
            'mper':True,
            'pdir':True,
            'pper':True,
            'shgt':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: Simulating WAves Nearshore (SWAN) Regional Wave Model: Rota, CNMI
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_rota.html
===================================
mdir (mean wave direction, degrees)
mper (mean wave period, second)
pdir (peak wave direction, degrees)
pper (peak wave period, second)
shgt (significant wave height, meters)
'''
swanro_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_rota.nc?'

swanro_dict = {'mdir': True,
            'mper':True,
            'pdir':True,
            'pper':True,
            'shgt':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: Simulating WAves Nearshore (SWAN) Regional Wave Model: Saipan, CNMI
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_saipan.html
===================================
mdir (mean wave direction, degrees)
mper (mean wave period, second)
pdir (peak wave direction, degrees)
pper (peak wave period, second)
shgt (significant wave height, meters)
'''
swansa_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_saipan.nc?'

swansa_dict = {'mdir': True,
            'mper':True,
            'pdir':True,
            'pper':True,
            'shgt':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: Simulating WAves Nearshore (SWAN) Regional Wave Model: Tutuila, American Samoa
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_tutuila.html
===================================
mdir (mean wave direction, degrees)
mper (mean wave period, second)
pdir (peak wave direction, degrees)
pper (peak wave period, second)
shgt (significant wave height, meters)
'''
swantu_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_tutuila.nc?'

swantu_dict = {'mdir': True,
            'mper':True,
            'pdir':True,
            'pper':True,
            'shgt':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: Surface CUrrents from a Diagnostic model (SCUD): Pacific
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/scud_pac.html
===================================
u (sea water velocity: eastward component, meter second-1)
v (sea water velocity: northward component, meter second-1)
'''
scudp_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/scud_pac.nc?'

scudp_dict = {'u': True,
            'v':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            }

# =================================== #
'''
Dataset Name: Surface CUrrents from a Diagnostic model (SCUD): Pacific, Lon+/-180
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/scud_pac_lon180.html
===================================
u (sea water velocity: eastward component, meter second-1)
v (sea water velocity: northward component, meter second-1)
'''
scudp180_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/scud_pac_lon180.nc?'

scudp180_dict = {'u': True,
            'v':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            }

# =================================== #
'''
Dataset Name: Tide Model (Barotropic) for the Pacific Ocean: Tidal Elevation
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/tide_pac.html
===================================
ssh (tidal elevation, meters)
'''
tidep_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/tide_pac.nc?'

tidep_dict = {'ssh': True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            }

# =================================== #
'''
Dataset Name: Tide Model (Barotropic) for the Pacific Ocean: Tidal Elevation, Lon+/-180
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/tide_pac_lon180.html
===================================
ssh (tidal elevation, meters)
'''
tidep180_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/tide_pac_lon180.nc?'

tidep180_dict = {'ssh': True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            }

# =================================== #
'''
Dataset Name: Tide Model (Barotropic) for the Pacific Ocean: Tidal Velocity
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/tide_pac_vel.html
===================================
u (u-velocity component, meter second-1)
v (v-velocity component, meter second-1)
'''
tidepv_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/tide_pac_vel.nc?'

tidepv_dict = {'u': True,
            'v':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: Tide Model (Barotropic) for the Pacific Ocean: Tidal Velocity, Lon+/-180
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/tide_pac_vel_lon180.html
===================================
u (u-velocity component, meter second-1)
v (v-velocity component, meter second-1)
'''
tidepv180_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/tide_pac_vel_lon180.nc?'

tidepv180_dict = {'u': True,
            'v':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: Tide Model for the Big Island of Hawaii: Tidal Elevation
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/tide_bi.html
===================================
ssh (tidal elevation, meters)
'''
tidebi_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/tide_bi.nc?'

tidebi_dict = {'ssh': True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            }

# =================================== #
'''
Dataset Name: Tide Model for the Hawaiian Islands: Main NW Islands: Tidal Elevation
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/tide_mhi.html
===================================
ssh (tidal elevation, meters)
'''
tidemhi_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/tide_mhi.nc?'

tidemhi_dict = {'ssh': True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            }

# =================================== #
'''
Dataset Name: WaveWatch III (WW3) Global Wave Model
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_global.html
===================================
Tdir (peak wave direction, degrees)
Tper (peak wave period, second)
Thgt (significant wave height, meters)
sdir (swell peak wave direction, degrees)
sper (swell peak wave period, seconds)
shgt (swell significant wave height, meters)
wdir (wind peak wave direction, degrees)
wper (wind peak wave period, seconds)
whgt (wind significant wave height, meters)
'''
ww3g_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_global.nc?'

ww3g_dict = {'Tdir': True,
            'Tper':True,
            'Thgt':True,
            'sdir':True,
            'sper':True,
            'shgt':True,
            'wdir':True,
            'wper':True,
            'whgt':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: WaveWatch III (WW3) Global Wave Model, Lon+/-180
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_global_lon180.html
===================================
Tdir (peak wave direction, degrees)
Tper (peak wave period, second)
Thgt (significant wave height, meters)
sdir (swell peak wave direction, degrees)
sper (swell peak wave period, seconds)
shgt (swell significant wave height, meters)
wdir (wind peak wave direction, degrees)
wper (wind peak wave period, seconds)
whgt (wind significant wave height, meters)
'''
ww3g180_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_global_lon180.nc?'

ww3g180_dict = {'Tdir': True,
            'Tper':True,
            'Thgt':True,
            'sdir':True,
            'sper':True,
            'shgt':True,
            'wdir':True,
            'wper':True,
            'whgt':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: WaveWatch III (WW3) Hawaii Regional Wave Model
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_hawaii.html
===================================
Tdir (peak wave direction, degrees)
Tper (peak wave period, second)
Thgt (significant wave height, meters)
sdir (swell peak wave direction, degrees)
sper (swell peak wave period, seconds)
shgt (swell significant wave height, meters)
wdir (wind peak wave direction, degrees)
wper (wind peak wave period, seconds)
whgt (wind significant wave height, meters)
'''
ww3h_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_hawaii.nc?'

ww3h_dict = {'Tdir': True,
            'Tper':True,
            'Thgt':True,
            'sdir':True,
            'sper':True,
            'shgt':True,
            'wdir':True,
            'wper':True,
            'whgt':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: WaveWatch III (WW3) Hawaii Regional Wave Model, Lon+/-180
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_hawaii_lon180.html
===================================
Tdir (peak wave direction, degrees)
Tper (peak wave period, second)
Thgt (significant wave height, meters)
sdir (swell peak wave direction, degrees)
sper (swell peak wave period, seconds)
shgt (swell significant wave height, meters)
wdir (wind peak wave direction, degrees)
wper (wind peak wave period, seconds)
whgt (wind significant wave height, meters)
'''
ww3h180_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_hawaii_lon180.nc?'

ww3h180_dict = {'Tdir': True,
            'Tper':True,
            'Thgt':True,
            'sdir':True,
            'sper':True,
            'shgt':True,
            'wdir':True,
            'wper':True,
            'whgt':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: WaveWatch III (WW3) Mariana Regional Wave Model
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_mariana.html
===================================
Tdir (peak wave direction, degrees)
Tper (peak wave period, second)
Thgt (significant wave height, meters)
sdir (swell peak wave direction, degrees)
sper (swell peak wave period, seconds)
shgt (swell significant wave height, meters)
wdir (wind peak wave direction, degrees)
wper (wind peak wave period, seconds)
whgt (wind significant wave height, meters)
'''
ww3ma_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_mariana.nc?'

ww3ma_dict = {'Tdir': True,
            'Tper':True,
            'Thgt':True,
            'sdir':True,
            'sper':True,
            'shgt':True,
            'wdir':True,
            'wper':True,
            'whgt':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: WaveWatch III (WW3) Northwestern Hawaiian Islands (NWHI) Regional Wave Model
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_nwhi.html
===================================
Tdir (peak wave direction, degrees)
Tper (peak wave period, second)
Thgt (significant wave height, meters)
sdir (swell peak wave direction, degrees)
sper (swell peak wave period, seconds)
shgt (swell significant wave height, meters)
wdir (wind peak wave direction, degrees)
wper (wind peak wave period, seconds)
whgt (wind significant wave height, meters)
'''
ww3nwhi_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_nwhi.nc?'

ww3nwhi_dict = {'Tdir': True,
            'Tper':True,
            'Thgt':True,
            'sdir':True,
            'sper':True,
            'shgt':True,
            'wdir':True,
            'wper':True,
            'whgt':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: WaveWatch III (WW3) Northwestern Hawaiian Islands (NWHI) Regional Wave Model, Lon+/-180
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_nwhi_lon180.html
===================================
Tdir (peak wave direction, degrees)
Tper (peak wave period, second)
Thgt (significant wave height, meters)
sdir (swell peak wave direction, degrees)
sper (swell peak wave period, seconds)
shgt (swell significant wave height, meters)
wdir (wind peak wave direction, degrees)
wper (wind peak wave period, seconds)
whgt (wind significant wave height, meters)
'''
ww3nwhi180_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_nwhi_lon180.nc?'

ww3nwhi180_dict = {'Tdir': True,
            'Tper':True,
            'Thgt':True,
            'sdir':True,
            'sper':True,
            'shgt':True,
            'wdir':True,
            'wper':True,
            'whgt':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: WaveWatch III (WW3) Samoa Regional Wave Model
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_samoa.html
===================================
Tdir (peak wave direction, degrees)
Tper (peak wave period, second)
Thgt (significant wave height, meters)
sdir (swell peak wave direction, degrees)
sper (swell peak wave period, seconds)
shgt (swell significant wave height, meters)
wdir (wind peak wave direction, degrees)
wper (wind peak wave period, seconds)
whgt (wind significant wave height, meters)
'''
ww3sa_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_samoa.nc?'

ww3sa_dict = {'Tdir': True,
            'Tper':True,
            'Thgt':True,
            'sdir':True,
            'sper':True,
            'shgt':True,
            'wdir':True,
            'wper':True,
            'whgt':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }

# =================================== #
'''
Dataset Name: WaveWatch III (WW3) Samoa Regional Wave Model, Lon+/-180
Index Information: https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_samoa_lon180.html
===================================
Tdir (peak wave direction, degrees)
Tper (peak wave period, second)
Thgt (significant wave height, meters)
sdir (swell peak wave direction, degrees)
sper (swell peak wave period, seconds)
shgt (swell significant wave height, meters)
wdir (wind peak wave direction, degrees)
wper (wind peak wave period, seconds)
whgt (wind significant wave height, meters)
'''
ww3sa180_org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_samoa_lon180.nc?'

ww3sa180_dict = {'Tdir': True,
            'Tper':True,
            'Thgt':True,
            'sdir':True,
            'sper':True,
            'shgt':True,
            'wdir':True,
            'wper':True,
            'whgt':True,
            'start_date':INIT_ST_DATE,
            'end_date':INIT_ED_DATE,
            'lat_range':INIT_LAT_RANGE,
            'long_range':INIT_LON_RANGE,
            'depth':INIT_DEPTH
            }
# TBD : Add more datasets inside --> Non-historic dataset

# =================================== #
# Support Dataset
datasetName = ['NOAA/NCEP Global Forecast System (GFS) Atmospheric Model',
               'NOAA Coral Reef Watch Monthly Global 5-km Satellite Coral Bleaching Monitoring Products',
               'NOAA Coral Reef Watch Monthly Global 5-km Satellite Coral Bleaching Monitoring Products Lon0360',
               'Weather Research and Forecasting (WRF) Regional Atmospheric Model: Maui-Oahu',
               'Weather Research and Forecasting (WRF) Regional Atmospheric Model: Samoa',
               'Weather Research and Forecasting (WRF) Regional Atmospheric Model: Oahu',
               'Weather Research and Forecasting (WRF) Regional Atmospheric Model: Main Hawaiian Islands',
               'Weather Research and Forecasting (WRF) Regional Atmospheric Model: Guam',
               'Weather Research and Forecasting (WRF) Regional Atmospheric Model: CNMI',
               'NOAA Coral Reef Watch Operational Daily Near-Real-Time Global 5-km Satellite Coral Bleaching Monitoring Products',
               'NOAA Coral Reef Watch Operational Daily Near-Real-Time Global 5-km Satellite Coral Bleaching Monitoring Products, Lon0360',
               'NOAA/NCEP Global Forecast System (GFS) Atmospheric Model, Lon+/-180',
               'NOAA/NCEP Global Forecast System (GFS) Atmospheric Model: Pacific',
               'NOAA/NCEP Global Forecast System (GFS) Atmospheric Model: Pacific, Lon+/-180',
               'Regional Ocean Modeling System (ROMS): CNMI: 2-D Variables',
               'Regional Ocean Modeling System (ROMS): CNMI: 3-D Variables',
               'Regional Ocean Modeling System (ROMS): CNMI: Data Assimilating: 2-D Variables',
               'Regional Ocean Modeling System (ROMS): CNMI: Data Assimilating: 3-D Variables',
               'Regional Ocean Modeling System (ROMS): Guam: 2-D Variables',
               'Regional Ocean Modeling System (ROMS): Guam: 3-D Variables',
               'Regional Ocean Modeling System (ROMS): Oahu South Shore: 2-D Variables',
               'Regional Ocean Modeling System (ROMS): Oahu South Shore: 3-D Variables',
               'Regional Ocean Modeling System (ROMS): Samoa: 2-D Variables',
               'Regional Ocean Modeling System (ROMS): Samoa: 3-D Variables',
               'Regional Ocean Modeling System (ROMS): Samoa: Data Assimilating: 2-D Variables',
               'Regional Ocean Modeling System (ROMS): Samoa: Data Assimilating: 3-D Variables',
               'Regional Ocean Modeling System (ROMS): Main Hawaiian Islands: 2-D Variables',
               'Regional Ocean Modeling System (ROMS): Main Hawaiian Islands: 3-D Variables',
               'Regional Ocean Modeling System (ROMS): Main Hawaiian Islands: Data Assimilating: 2-D Variables',
               'Regional Ocean Modeling System (ROMS): Main Hawaiian Islands: Data Assimilating: 3-D Variables',
               'Regional Ocean Modeling System (ROMS): Main Hawaiian Islands: Reanalysis: 2-D',
               'Regional Ocean Modeling System (ROMS): Main Hawaiian Islands: Reanalysis: 3-D',
               'Simulating WAves Nearshore (SWAN) Regional Wave Model: Big Island',
               'Simulating WAves Nearshore (SWAN) Regional Wave Model: Guam',
               'Simulating WAves Nearshore (SWAN) Regional Wave Model: Guam: Apra Harbor',
               'Simulating WAves Nearshore (SWAN) Regional Wave Model: Kauai',
               'Simulating WAves Nearshore (SWAN) Regional Wave Model: Manua, American Samoa',
               'Simulating WAves Nearshore (SWAN) Regional Wave Model: Maui',
               'Simulating WAves Nearshore (SWAN) Regional Wave Model: Oahu',
               'Simulating WAves Nearshore (SWAN) Regional Wave Model: Rota, CNMI',
               'Simulating WAves Nearshore (SWAN) Regional Wave Model: Saipan, CNMI',
               'Simulating WAves Nearshore (SWAN) Regional Wave Model: Tutuila, American Samoa',
               'Surface CUrrents from a Diagnostic model (SCUD): Pacific',
               'Surface CUrrents from a Diagnostic model (SCUD): Pacific, Lon+/-180',
               'Tide Model (Barotropic) for the Pacific Ocean: Tidal Elevation',
               'Tide Model (Barotropic) for the Pacific Ocean: Tidal Elevation, Lon+/-180',
               'Tide Model (Barotropic) for the Pacific Ocean: Tidal Velocity',
               'Tide Model (Barotropic) for the Pacific Ocean: Tidal Velocity, Lon+/-180',
               'Tide Model for the Big Island of Hawaii: Tidal Elevation',
               'Tide Model for the Big Island of Hawaii: Main NW Islands: Tidal Elevation',
               'WaveWatch III (WW3) Global Wave Model',
               'WaveWatch III (WW3) Global Wave Model, Lon+/-180',
               'WaveWatch III (WW3) Hawaii Regional Wave Model',
               'WaveWatch III (WW3) Hawaii Regional Wave Model, Lon+/-180',
               'WaveWatch III (WW3) Mariana Regional Wave Model',
               'WaveWatch III (WW3) Northwestern Hawaiian Islands (NWHI) Regional Wave Model',
               'WaveWatch III (WW3) Northwestern Hawaiian Islands (NWHI) Regional Wave Model, Lon+/-180',
               'WaveWatch III (WW3) Samoa Regional Wave Model',
               'WaveWatch III (WW3) Samoa Regional Wave Model, Lon+/-180']

Informations = ['https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ncep_global.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/dhw_5km_monthly.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/dhw_5km_monthly_lon360.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/wrf_mo.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/wrf_samoa.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/wrf_oa.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/wrf_hi.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/wrf_guam.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/wrf_cnmi.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/dhw_5km.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/dhw_5km_lon360.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ncep_global_lon180.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ncep_pac.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ncep_pac_lon180.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_mari_ssh.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_mari.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_mari_assim_ssh.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_mari_assim.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_marig_ssh.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_marig.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiomsg_ssh.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiomsg.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_samoa_ssh.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_samoa.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_samoa_assim_ssh.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_samoa_assim.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiig_ssh.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiig.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiig_assim_ssh.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiig_assim.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiig_reanalysis_ssh.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/roms_hiig_reanalysis.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_bigi.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_guam.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_apra.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_kauai.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_manua.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_maui.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_oahu.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_rota.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_saipan.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/swan_tutuila.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/scud_pac.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/scud_pac_lon180.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/tide_pac.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/tide_pac_lon180.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/tide_pac_vel.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/tide_pac_vel_lon180.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/tide_bi.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/tide_mhi.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_global.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_global_lon180.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_hawaii.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_hawaii_lon180.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_mariana.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_nwhi.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_nwhi_lon180.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_samoa.html',
               'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ww3_samoa_lon180.html']

datasetCode = ['gfs',
               'dhw5',
               'dhw5_l360',
               'wrf_mo',
               'wrf_samoa',
               'wrf_oa',
               'wrf_hi',
               'wrf_guam',
               'wrf_cnmi',
               'dhw5km',
               'dhw5km_l360',
               'gfs_l180',
               'gfs_pac',
               'gfs_pac_l180',
               'roms2d',
               'roms3d',
               'roms2d_as',
               'roms3d_as',
               'romsg2d',
               'romsg3d',
               'romsos2d',
               'romsos3d',
               'romssa2d',
               'romssa3d',
               'romssa2d_as',
               'romssa3d_as',
               'romshi2d',
               'romshi3d',
               'romshi2d_as',
               'romshi3d_as',
               'romshi2d_re',
               'romshi3d_re',
               'swanbg',
               'swangu',
               'swanap',
               'swanka',
               'swanma',
               'swanmaui',
               'swanoh',
               'swanro',
               'swansa',
               'swantu',
               'scudp',
               'scudp180',
               'tidep',
               'tidep180',
               'tidepv',
               'tidepv180',
               'tidebi',
               'tidemhi',
               'ww3g',
               'ww3g180',
               'ww3h',
               'ww3h180',
               'ww3ma',
               'ww3nwhi',
               'ww3nwhi180',
               'ww3sa',
               'ww3sa180']

# Code specify the code I defined here , it would not be exactly the same as in the ERDDAP website
support_df = {'Dataset':datasetName,
              'Information':Informations,
              'Code':datasetCode}