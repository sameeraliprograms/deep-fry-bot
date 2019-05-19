import random
import sys


text = open("./input/topText.txt", "r", encoding='utf8', errors='ignore').read()
text = ''.join([i for i in text if not i.isdigit()]).replace("\n\n", " ").split(' ')

index = 1
chain = {}
count = 6


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


with open("./output/topOut.txt", "w") as file:
    file.write(message)
output = open("./output/topOut.txt","r")
print(output.read())
file.close