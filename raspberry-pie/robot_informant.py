from command import Command
import json

class RobotInformant:
	def __init__(self, configPath : str) -> None:
		with open(configPath, encoding = "UTF-8") as file:
			self.__dict__.update(**json.loads(file.read()))
		if self.commands == []: raise CreatingRobotException()
		
	def __getitem__(self, key : str) -> str:
		for command in self.commands:
			result = command if key == command.text else None
		return result

class CreatingRobotException(BaseException):
	def __init__(self) -> None:
		self.message = "Creating robot exception"

	def __str__(self) -> str:
		return self.message
