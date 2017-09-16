def pair(stream):
	a = True
	b = None
	for i in stream:
		if a:
			b = i
		else:
			yield b, i
		a = not a


def readWords(words, fileName=None):
	if fileName is None: fileName = 'words.txt'
	with open(fileName, encoding='utf-8') as wordsFile:
		for line in wordsFile:
			arr = line.split()
			if len(arr) < 2:
				words[arr[0]] = [0, {}]
			else:
				words[arr[0]] = [int(arr[1]), { i: int(j) for i, j in pair(arr[2:]) }]


def writeWords(words, fileName=None):
	if fileName is None: fileName = 'words.txt'
	with open(fileName, 'w', encoding='utf-8') as f:
		for k, v in words.items():
			f.write(k + ' ' + str(v[0]))
			for k2, v2 in v[1].items():
				f.write(' ' + k2 + ' ' + str(v2))
			f.write('\n')
