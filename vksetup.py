import vk
from UniAPI import main

key = '079586b44efde2f44c71b59686cf1d17fefb37996117bc6610564a3e4f4c213c4d13790b88f4cf3d577d5'
session = vk.Session(access_token=key)
api = vk.API(session)


def inputMessage(k, lastWordsDict):
	res = api.messages.getDialogs(unanswered=True)
	if res[0] > 0:
		for i in res[1:]:
			if i['uid'] not in lastWordsDict:
				lastWordsDict[i['uid']] = None
			elif i['uid'] == k:
				return i['body'].strip().lower()
	return 'продолжить'


def askForAdd(k, word):
	api.messages.send(user_id=k, message='Я не знаю слова "' + word + '". Ходи опять!')
	return False


def acceptWord(k, word):
	api.messages.send(user_id=k, message='Моё слово: ' + word + '. Твой ход!')


if __name__ == '__main__':
	lwd = {}
	inputMessage(None, lwd)  # get unread dialogs
	main(askForAdd, inputMessage, acceptWord, lwd, False)
