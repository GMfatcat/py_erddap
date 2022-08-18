# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 12:28:57 2022

@author: GMfatcat
"""
# =================================== #
# Import Packages
import time
import pprint # for pretty printing dictionaires
import pandas as pd
import requests
import os
from download_setting import * # Initial Settings
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
				print(f"Excecute time(function): {func.__name__} with {round(ed-st,4)} seconds")
				return rt
			else:
				st = time.time()
				func(*args, **kwargs)
				ed = time.time()
				print(f"Excecute time(function): {func.__name__} with {round(ed-st,4)} seconds")

		return wrapper
	return decorator

# =================================== #
# Print Pretty Dictionary
def pretty_dict(_dict):
	if not isinstance(_dict,dict):
		raise TypeError("_dict must be a dictionary!")

	pprint.pprint(_dict)

# Example
#pretty_dict(wrf_oa_dict) #wrf_oa_dict is defined in download_setting.py

# =================================== #
@show_func_time(if_return = False)
def show_support_format():
	sup_format = binary_format + plain_format
	print("Support Format:")
	print(sorted(sup_format))
	print("default = '.nc'")
	print("Usage: <Code>_dict & <Code>_org_url to get default dataset setting ,where Code can been find with function: show_dataset()")

# =================================== #
# Return pandas dataframe or just print pretty dictionary
# Do a number check for the support_df
@show_func_time(if_return = True)
def show_dataset(pandas_df = True):

	len_ds = len(datasetName)
	len_cd = len(datasetCode)
	len_if = len(Informations)
	if not (len_ds == len_cd == len_if):
		print(f"Dataset:{len_ds} Informations:{len_if} Code:{len_cd}")
		raise ValueError("Inconsistent of supported dataset")

	if pandas_df:
		df = pd.DataFrame(support_df)
		#df = df[df.Dataset != ''] # get rid of unfinish rows --> onl used in developing stage
		print(f"\nCurrent supported dataset: {len(df)} --> Not support for dataset with depth for now")
		return df

	else:
		pretty_dict(support_df)


@show_func_time(if_return = False)
def last_check_before_download(downloader):
	print("======Current Downloader Settings======")
	pretty_dict(downloader.__dict__)
	print("=======================================")

# =================================== #
# Define Downloader Class
class Downloader:
	def __init__(self,name):
		self.name = name
		self.if_set_up = False
		self.ready = False # Ready to download or not
		self.asyncio = False # asyncio download is experimental, still testing
		print(f'{self.name} has been created')

	@show_func_time(if_return = False)
	def set_up(self,targetDataset_dictionary,targetDataset_org_url):
		self.target_dict = targetDataset_dictionary
		self.target_org_url = targetDataset_org_url
		# Show Result
		print("======Current Dict Settings======")
		pretty_dict(self.target_dict)
		print("=================================")
		# Set flag to true to move on to define define_url_and_output_filename
		self.if_set_up = True

	def check_filetype(self, filetype,url):
		# binary mode with open() --> use 'wb' mode
		if filetype in binary_format:
			self.saveflag = 'wb'
		else:
			self.saveflag = 'w'
		new_url = url.replace('.nc',filetype)
		self.filetype = filetype # Set up filetype in order to make output filename later
		return new_url

	# Ex: name = start_date_end_date_lat_range_long_range_gfs.nc
	def define_filename(self,cond_full_url,file_suffix):
		name = cond_full_url.replace("%5D%5B","")
		name = name.replace(")%5D","")
		name = name.replace("%5B(","")
		name = name.replace(":1:","")
		name = name.replace(":00Z)","")
		name = name.replace("-","_")
		name = name.replace(":","_")
		name = name.replace("(","_")
		name = name.replace(")","_")
		name = name.replace("__","_")
		name = name + f'_{file_suffix}' + self.filetype
		return name

	@show_func_time(if_return = True)
	def generate_condiction_url(self, new_org_url, def_stride, file_suffix):
		org_url = new_org_url
		output_url = ''
		# Generate condition url part
		condition_dict = self.target_dict
		START_DATE = condition_dict.get('start_date')
		END_DATE = condition_dict.get('end_date')
		MIN_LAT = str(condition_dict.get('lat_range')[0])
		MAX_LAT = str(condition_dict.get('lat_range')[1])
		MIN_LONG = str(condition_dict.get('long_range')[0])
		MAX_LONG = str(condition_dict.get('long_range')[1])
		cond_url_date = '%5B' + START_DATE + f':{def_stride}:' + END_DATE
		cond_url_loc = '%5D%5B(' + MIN_LAT + ')'+ f':{def_stride}:' +'(' + MAX_LAT +')%5D%5B(' + MIN_LONG + ')'+ f':{def_stride}:'+ '(' + MAX_LONG + ')%5D'
		cond_full_url = cond_url_date + cond_url_loc

		# Generate output filename
		output_filename = self.define_filename(cond_full_url,file_suffix)

		# If statement to add url
		First_index_added = False # Inorder to decide whether or not add ',' in front of index, only the first index after .nc? doesn't need to add ','
		keys_list = [*condition_dict]  # get list of key name of dict

		# Send index into loop for condition check except the last four keywords: time & location
		for i in range(len(condition_dict)-4):
			if condition_dict.get(keys_list[i]):
				if First_index_added:
				    output_url += ',' + keys_list[i] + cond_full_url  # since first index involved, just add ','
				else:
					First_index_added = True
					output_url += org_url + keys_list[i] + cond_full_url

		return output_url,output_filename

	@show_func_time(if_return = False)
	def define_url_and_output_filename(self,saving_dir,suffix,filetype = '.nc',stride = 1):
		if not self.if_set_up:
			raise ValueError("You must set up the downloader before defining the url and output filename")

		self.saving_dir = saving_dir
		# Start define url
		#org_url = 'https://pae-paha.pacioos.hawaii.edu/erddap/griddap/ncep_global.nc?'
		org_url = self.target_org_url
		# check if filetype is valid and return org_url with defined filetype
		new_org_url = self.check_filetype(filetype, url = org_url)
		output_url,filename = self.generate_condiction_url(new_org_url = new_org_url, def_stride = stride, file_suffix = suffix)
		self.download_url = output_url
		self.filename = filename
		self.ready = True

	# Start download process
	def run(self,return_filepath = True):
		if not self.ready:
			raise Exception("You must define url and output_filename before downloading")

		print("Request Status | Filename | Finish Time")
		t0 = time.time()
		try:
			r = requests.get(self.download_url)
			if r.status_code == requests.codes.ok:
				print("Request OK...",end=' ')
				file = os.path.join(self.saving_dir,self.filename)
				# saveflag: 'wb' or 'w'
				with open(file, self.saveflag) as f:
					f.write(r.content)
					print(self.filename, 'in',round(time.time() - t0,2),'sec')
					if return_filepath:
						self.filepath = file

		except Exception as e:
			print('Exception in downloading:', e)

