from command import Command
from functions import speak, convert_speech_to_text

import json

class RobotInformant:
	def __init__(self, configPath : str) -> None:
		with open(configPath, encoding = "UTF-8") as file:
			self.commands = json.loads(file.read())["commands"]
		None if self.commands == [] else None
		
	def __getitem__(self, key : str) -> str:
		for command in self.commands:
			result = command if key == command.text else None
		return result

class CreatingRobotException(BaseException):
	def __init__(self) -> None:
		self.message = "Creating robot exception"

	def __str__(self) -> str:
		return self.message
