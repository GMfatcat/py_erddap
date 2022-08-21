# py_erddap
Package contains handy and customize tool for downloading grid data from [ERDDAP website](https://pae-paha.pacioos.hawaii.edu/erddap/griddap) with API  
Inspired by my previous project:[ConvLSTM-CNN-for-tropical-cyclone](https://github.com/GMfatcat/ConvLSTM-CNN-for-tropical-cyclone)

## For those who want to try out:point_down: ##  
No need to install it , just add **download.py** and **download_setting.py** to your current working directory  
:point_right: Import in your script and it's ready to go ~  
`
from download import *
`

## For those who want to get a package:point_down: ## 
`
pip install https://github.com/GMfatcat/py_erddap.git
`

## :white_check_mark: Package Usage ##
Check **Example.ipynb** for dataset *without depth*, ex. `NOAA/NCEP Global Forecast System (GFS) Atmospheric Model`  
Check **Example_with_depth.ipynb** for dataset *with depth*, ex. `Simulating WAves Nearshore (SWAN) Regional Wave Model`  
:orange_book: define_url_and_output_filename() can also choose the file type to save, default to `.nc` 
`define_url_and_output_filename(saving_dir,suffix,filetype = '.nc',stride = 1)`

### New Features TODO LIST
[:x:] Asynico Download (Failed:bug:)
- [ ] Multiprocessing Download (Still Working:bicyclist:)
- [ ] Dataset without historic data (Still Working:bicyclist:)


