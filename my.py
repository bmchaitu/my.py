#! /usr/bin/python3
import os

print("helloWorld")

for folder,subfolder,files in os.walk('/media/chaitu/'):
		 for file in files:
		 	if file.endswith('.lnk'):
		 		print(os.path.join(folder,file))
		 		os.unlink(os.path.join(folder,file))
	