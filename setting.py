import time
import pprint # for pretty printing dictionaires

# This file contains different setup dictionaires for different download dataset
# Set All Orginal URL to .nc file, this can be alter in the download stage

# =================================== #
# init values
INIT_LAT_RANGE = [0,30]
INIT_LON_RANGE = [118,150]
INIT_ST_DATE = '(2022-04-25T12:00:00Z)'
INIT_ED_DATE = '(2022-04-30T12:00:00Z)'
# =================================== #
# Decorator function
#  3 layer of wrapper to take args --> control if there is a return function
def show_func_time(if_return:bool):
	def decorator(func):
		def wrapper(*args, **kwargs):

			if if_return:
				st = time.time()
				rt = func(*args, **kwargs)
				ed = time.time()
				print(f"Now use func:{func.__name__} with {round(ed-st,4)} seconds")
				return rt
			else:
				st = time.time()
				func(*args, **kwargs)
				ed = time.time()
				print(f"Now use func:{func.__name__} with {round(ed-st,4)} seconds")

		return wrapper
	return decorator

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
            'long_range':INIT_LON_RANGE
            }


# TBD : Add more dataset inside --> start from SWAN Guam


# =================================== #
# Print Pretty Dictionary
@show_func_time(if_return = False)
def pretty_dict(_dict):
	pprint.pprint(_dict)

# Example
pretty_dict(wrf_oa_dict)

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
               '',
               '',
               '',
               '',
               '',
               '',
               '',
               '',
               '']

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
               '',
               '',
               '',
               '',
               '',
               '',
               '',
               '',
               '']

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
               '',
               '',
               '',
               '',
               '',
               '',
               '',
               '',
               '']

# Code specify the code I defined here , it would not be exactly the same as in the ERDDAP website
support_df = {'Dataset':datasetName,
              'Information':Informations,
              'Code':datasetCode}

# Return pandas dataframe or just print pretty dictionary
# Do a number check for the support_df
@show_func_time(if_return = True)
def show_dataset(pandas_df = True):

	len_ds = len(datasetName)
	len_cd = len(datasetCode)
	len_if = len(Informations)
	#len_ds == len_cd and len_ds == len_if
	if not (len_ds == len_cd == len_if):
		print(f"Dataset:{len_ds} Informations:{len_if} Code:{len_cd}")
		raise ValueError("Inconsistent of supported dataset")

	if pandas_df:
		import pandas as pd
		df =  pd.DataFrame(support_df)
		df = df[df.Dataset != ''] # get rid of unfinish rows
		print(f"\n*Current supported dataset: {len(df)}")
		return df

	else:
		pretty_dict(support_df)

sup_df = show_dataset()
print(sup_df.head())
