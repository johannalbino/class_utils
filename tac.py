class TreatingAccentsCharacters(object):

	def __init__(self):
		self.__a = ['ã', 'â', 'á', 'à', 'ä']
		self.__e = ['ê', 'é', 'è', 'ë']
		self.__i = ['î', 'í', 'ì', 'ï']
		self.__o = ['õ', 'ô', 'ó', 'ò', 'ö']
		self.__u = ['û', 'ú', 'ù', 'ü']
		self.__c = ['ç']
		self.__n = ['ñ']
		self.__character_special = {'a': self.__a, 'e': self.__e, 'i': self.__i, 'o': self.__o, 'u': self.__u, 'c': self.__c, 'n': self.__n}


	def tac(self, text):
		for k, v in self.__character_special.items():
			for letter in v:
				if k == 'a':
					text = text.replace(letter, 'a')
				if k == 'e':
					text = text.replace(letter, 'e')
				if k == 'i':
					text = text.replace(letter, 'i')
				if k == 'o':
					text = text.replace(letter, 'o')
				if k == 'u':
					text = text.replace(letter, 'u')
				if k == 'c':
					text = text.replace(letter, 'c')
				if k == 'n':
					text = text.replace(letter, 'n')

		return text
