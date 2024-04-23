from command import Command
from deserializer import Deserializer

import functions

class CreatingRobotException(Exception):
	def __init__(self) -> None:
		self.message = "Creating robot exception"

	def __str__(self) -> str:
		return self.message

class Robot:
	def __init__(self, deserializer : Deserializer) -> None:
		self.commands = deserializer.decode()
		if commands == []:
			raise CreatingCommandException()
		print(self.commands)
		
	def __getitem__(self, key : str) -> None:
		for command in self.commands:
			result = command if key == command.text else None
		functions.speak(result)
