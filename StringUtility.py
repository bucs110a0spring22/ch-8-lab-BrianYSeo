class StringUtility:
	def __init__(self, string):
		"""
			sets the parameter variable to an instance of the class
			args: self(object), string(string that is passed in from main)
			return: None
		"""
		self.original = string


	def __str__(self):
		"""
			returns the internal string itself, unchanged
			args: self(object)
			return: original(string)
		"""
		return self.original

	def vowels(self):
		"""
			counts the number of vowels in each string
			args: self(object)
			return: count(as a string, number of vowels)
		"""
		vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
		count = 0
		for ch in self.original:
			if ch in vowels:
				count += 1
		if count < 5:
			return str(count)
		else:
			return "many"

	def bothEnds(self):
		"""
			creates a string made up of the first and last two letters in the given strings
			args: self(object)
			return: string
		"""
		#if len(self.original) > 2:
			#return self.original[0] + self.original[1] + self.original[-2] + self.original[-1]
		#else:
			#return ""
		return self.original[0] + self.original[1] + self.original[-2] + self.original[-1] if len(self.original) > 2 else ""

	def fixStart(self):
		"""
			changes all instqances of the first letter in the string to stars except for the first letter
			args: self(object)
			return: string
		"""
		if len(self.original) > 1:
			new = self.original[0]
			firstLetter = self.original[0]
			for ch in self.original[1: len(self.original): 1]:
				if ch == firstLetter:
					new += "*"
				else:
					new += ch
			return new
		else:
			return self.original

	def asciiSum(self):
		"""
			adds up the ascii values of all the letters in the given string
			args: self(object)
			return: int(sum of ascii values)
		"""
		sums = 0
		for ch in self.original:
			sums += ord(ch)
		return sums

	def cipher(self):
		"""
			changes each letter in the string to the letter than is the length of the string number away from the letter in the alphabet
			args: self(object)
			return: string
		"""
		if len(self.original) > 0:
			upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
			lower = "abcdefghijklmnopqrstuvwxyz"
			new = ""
			for ch in self.original:
				if ch != ' ':
					if ord(ch) > 96:
						new += lower[(lower.index(ch) + len(self.original)) % 26]
					else:
						new += upper[(upper.index(ch) + len(self.original)) % 26]
				else:
					new += ch
			return new
		else:
			return self.original