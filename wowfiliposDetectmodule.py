import os


import wowfilipDetectmodule_place as pl

t = pl.place

info = "system"
try:
   os.chdir("/etc/")
   info = "Linux"
   os.chdir(t)

except:
	del info
	info = "Windows"
	print("error")


try:
   print(info)

except:
	print("ay")
	
