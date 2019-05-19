from PIL import Image
import deep, asyncio
import memegenerator as meme
import grabber as gr
from random import randint
import random
import sys
import facebook
import numpy
text = open("./input/bottomText.txt", "r", encoding='utf8', errors='ignore').read()
text = ''.join([i for i in text if not i.isdigit()]).replace("\n\n", " ").split(' ')

index = 1
chain = {}
count = (randint(1, 8))


for word in text[index:]: 
    key = text[index - 1]
    if key in chain:
        chain[key].append(word)
    else:
        chain[key] = [word]
    index += 1

word1 = random.choice(list(chain.keys())) 
message = word1.capitalize()


while len(message.split(' ')) < count:
    word2 = random.choice(chain[word1])
    word1 = word2
    message += ' ' + word2



with open("./output/botOut.txt", "w") as file:
    file.write(message)
output = open("./output/botOut.txt","r")
print(output.read())
file.close

exec(open("markovtop.py").read());


topText = open("./output/topOut.txt", "r", encoding='utf8', errors='ignore')

botText = open("./output/botOut.txt", "r", encoding='utf8', errors='ignore')


topString = (topText.read())
bottomString = (botText.read())
filename = './images/down.png'

meme.make_meme(topString, bottomString, filename)
async def main():
    img = Image.open('./finale/temp.png')
    deep.main('finale', 'final/')
    img.save('./final/result.png')
loop = asyncio.get_event_loop()
loop.run_until_complete(main())


# bruh momento 

page_access_token = "EAACVS6jUj0QBAKVZAWepw2sVqnjIHw4ZCyGQUgcrV88MBy6CZCLjiDNicsaKbXxsa5QfOpKV6iOFmlKF376G18pvOEZBZCTLhkkq123Fd35zJI81mfE1b99P8x1ZB288PPQ1ELOX8wjGmW6cfYxPWornSRaupYKvds7b8bDjVSUQeLoZAxNtLGn"
graph = facebook.GraphAPI(page_access_token)
facebook_page_id = "2045764118879252"
graph.put_photo(image=open('./final/temp-fry.png', 'rb'), message='meme bruh')
