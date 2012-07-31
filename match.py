#encoding=utf-8
#author: lvyaojia

def combine():
	dicFile = open('dicFile','a')
	spelling = [line.rstrip() for line in open("Spelling")] 
	words = [line.rstrip() for line in open("words")] 

	for line in range(3880):
		dicFile.write(words[line] + "*" + spelling[line] + '\n')

	spelling.close()
	words.close()
	dicFile.close()


def match(f = 'dicFile',openFrom = "source",saveTo = "save"):
	demoFile = open(openFrom).read().decode('utf-8')
	saveFile = open(saveTo,'a')
	Dic = open(f).readlines()
	dic = {}
	for line in Dic:
		temp = line.split('*')
		words,spelling = temp[0].decode('utf-8'), temp[1].rstrip()
		dic.update({}.fromkeys(words, spelling))
	for character in demoFile:
		tem =  dic.get(character)
		if(tem!=None):
			saveFile.write(tem+" ")
			print character.encode('utf-8')," ",tem, 
		else:
			saveFile.write(character.encode('utf-8'))
			print character.encode('utf-8')
	saveFile.close()


if __name__ == '__main__':
	match()


