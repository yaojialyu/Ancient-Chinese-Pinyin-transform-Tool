#encoding=utf-8
#author: lvyaojia
#date: 2012-03-24

def combine():
	dicFile = open('dicFile','a')
	spelling = [line.rstrip() for line in open("Spelling")] 
	words = [line.rstrip() for line in open("words")] 

	for line in range(3880):
		dicFile.write(words[line] + "*" + spelling[line] + '\n')

	spelling.close()
	words.close()
	dicFile.close()


def match(dicFile='dicFile', sourceFile="source", saveFile="result"):
	sourceFile = open(sourceFile).read().decode('utf-8')
	saveFile = open(saveFile,'a')
	dictoryRaw = open(dicFile).readlines()
	dictory = {}
	for line in dictoryRaw:
		temp = line.split('*')
		words,spelling = temp[0].decode('utf-8'), temp[1].rstrip()
		dictory.update({}.fromkeys(words, spelling))
	for character in sourceFile:
		tem =  dictory.get(character)
		if(tem!=None):
			saveFile.write(tem+" ")
			print character.encode('utf-8')," ",tem, 
		else:
			saveFile.write(character.encode('utf-8'))
			print character.encode('utf-8')
	saveFile.close()


if __name__ == '__main__':
	match()


