# //how to scrape youtube videos?

from bs4 import BeautifulSoup
import requests
from pytube import YouTube
import os
import urllib3
import download

url = 'https://www.youtube.com/@s-respect'

title = download.vidownload(url)
      
str(title)
print(title)
i =0
path="/videos/"
for filename in os.listdir(path):
	my_dest ="new" + str(i) + ".jpg"
	my_source =path + filename
	my_dest =path + my_dest
	# rename() function will
	# rename all the files
	os.rename(my_source, my_dest)
	i += 1
os.system(f"python -u upload_video.py --file /videos/newvideo.mp4 --title respect_video")
os.remove("newvideo.mp4")
   # for name in entry.find_all("name"):
   #    print(name.text)
   # for pub in entry.find_all("published"):
   #    print(pub.text)

# print (link["href"])


# videodownload()