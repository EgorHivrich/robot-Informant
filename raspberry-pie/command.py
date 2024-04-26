from random import randint

class Command:
	def __init__(self, text : str, callbacks : [str]) -> None:
		if text.isspace() or callbacks == []:
			raise CreatingCommandException()
		self.text = text
		self.callbacks = callbacks
		
	def __str__(self) -> str:
		return "{0} - {1}".format(self.text, self.callbacks)
		
	def getRandomCallback(self) -> str:
		index = randint(0, len(self.callbacks) - 1)
		return self.callbacks[index]
		
class CreatingCommandException(BaseException):
	def __init__(self) -> None:
		self.message = "creating command exception"
		
	def __str__(self) -> str:
		return self.message
