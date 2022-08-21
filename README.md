# py_erddap
![Status](https://img.shields.io/badge/xarray-needed-brightgreen)
![Status](https://img.shields.io/badge/netCDF4-needed-brightgreen)
![Status](https://img.shields.io/badge/requests-needed-critical)
![Status](https://img.shields.io/badge/aiohttp-needed-brightgreen)  
Package contains handy and customize tool for downloading grid data from [ERDDAP website](https://pae-paha.pacioos.hawaii.edu/erddap/griddap) with API  
Inspired by my previous project:[ConvLSTM-CNN-for-tropical-cyclone](https://github.com/GMfatcat/ConvLSTM-CNN-for-tropical-cyclone)  
Package Icon:<a href="https://www.vecteezy.com/free-vector/dolphin-icon">Dolphin Icon Vectors by Vecteezy</a>

## For those who want to try out:point_down: ##  
No need to install it , just add **download.py** and **download_setting.py** to your current working directory  
:point_right: Import in your script and it's ready to go ~  
`
git clone https://github.com/GMfatcat/py_erddap.git
`  
`
from download import *
`

## For those who want to get a package:point_down: ##
*More functional pip package will be release later (I wish to release at least until Multiprocessing Download works fine)*  
`pip install py-erddap==1.0.1`

## :white_check_mark: Package Usage ##
Check **Example.ipynb** for dataset *without depth*, ex. `NOAA/NCEP Global Forecast System (GFS) Atmospheric Model`  
Check **Example_with_depth.ipynb** for dataset *with depth*, ex. `Simulating WAves Nearshore (SWAN) Regional Wave Model`  

-------  

:orange_book: define_url_and_output_filename() can also choose the file type to save, default to `.nc` 
`define_url_and_output_filename(saving_dir,suffix,filetype = '.nc',stride = 1)`  

:warning:All defaults are **inherit from the gfs dataset**, you need to modify when downloading other dataset  
:warning:You **Should Always Check your downlaod setting** before run the downloader, since initial values varys in every dataset  
:warning:You got a **big chance to get nothing in random setting** :trollface:  

### New Features TODO LIST
[:x:] Asynico Download (Failed:bug:)
- [ ] Multiprocessing Download (Still Working:bicyclist:)
- [ ] Dataset without historic data (Still Working:bicyclist:)

## Bugs and feature requests

Have a bug or a feature request? Please first search for existing and closed issues.  
If your problem or idea is not addressed yet, please open a new issue.  


## Creator

**GMfatcat**

- <https://github.com/GMfatcat>
- <http://homepage.ntu.edu.tw/~r10521801/>


## Copyright and license

Code released under the [MIT License](https://reponame/blob/master/LICENSE).

Enjoy :metal:
