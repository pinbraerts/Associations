from random import uniform, choice
from DataWriterReader import *

words = {}

def getRandom(word):
	if words[word][0] <= 0: return choice([i for i in words.keys()])
	r = uniform(0, words[word][0])
	s = 0
	k = None
	for k, v in words[word][1].items():
		s += v
		if r < s:
			return k
	return k


def proceedCmd(cmd, k, lastWordsDict, askForAdd=lambda k, word: True):
	if cmd == "выйти":
		return -1
	if cmd == 'пропустить':
		return choice([i for i in words.keys()])
	if cmd == 'продолжить':
		return ""
	if cmd not in words:
		if askForAdd(k, cmd):
			words[cmd] = [0, {}]
		else:
			return lastWordsDict[k]
	if lastWordsDict[k] is not None:
		if cmd in words[lastWordsDict[k]][1]:
			words[lastWordsDict[k]][1][cmd] += 1
		else:
			words[lastWordsDict[k]][1][cmd] = 1
		words[lastWordsDict[k]][0] += 1
	return getRandom(cmd)


def main(askForAdd=
            lambda k, word:
				input('Мне неизвестно слово "' + word + '". Добавить его в базу? (д/н) ').strip().lower() == 'д',
        waitWord=lambda k, lastWordsDict: input().strip(),
        acceptWord=lambda k, word: print('Моё слово:', word, "\nВаш ход: ", end=""),
        lastWordsDict=None, term=True):
	readWords(words)
	try:
		if lastWordsDict is None:
			lastWordsDict = {0: None}
		while True:
			for k in dict(lastWordsDict).keys():
				word = waitWord(k, lastWordsDict)
				lastWord = proceedCmd(word, k, lastWordsDict, askForAdd)
				if lastWord is -1:
					del lastWordsDict[k]
				elif lastWord:
					lastWordsDict[k] = lastWord
					acceptWord(k, lastWordsDict[k])
			if term and len(lastWordsDict) == 0:
				break
			while len(lastWordsDict) == 0:
				waitWord(None, lastWordsDict)
			writeWords(words)
	finally:
		writeWords(words)


if __name__ == '__main__':
	print("Ваш ход: ", end="")
	main()
