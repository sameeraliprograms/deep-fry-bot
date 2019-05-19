import urllib.request
import reqimg as req

from io import BytesIO

def dl_jpg(url, filePath, fileName):
	fullPath = filePath + file_name + '.png'
	urllib.request.urlretrieve(url, fullPath)

url = req.reqImg()
file_name = 'down'

dl_jpg(url, 'images/', file_name)
