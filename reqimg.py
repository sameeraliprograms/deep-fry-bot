from urllib import request
from io import BytesIO
import requests
def reqImg():
	r= requests.get("https://www.shitpostbot.com/api/randsource")
	img_url = "https://www.shitpostbot.com/"
	content = str(r.content)[2:-1:]
	content = content.replace('null', '0')
	img_url += eval(content)['sub']['img']['full'].replace('\\', '')
	return img_url