#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request

ext_id = input('Enter the ID of the extension: ')
save_name = input('Enter the name you want to save it by: ')

dl_url = "https://clients2.google.com/service/update2/crx?response=redirect&x=id%3D" + ext_id + "%26uc&prodversion=32"
print("Download URL: " + dl_url)

try:
	urllib.request.urlretrieve(dl_url, save_name + ".crx")
	print("Extension downloaded successfully: " + save_name + ".crx")

except Exception as e:
	print("Something went wrong!")
	print(e)
