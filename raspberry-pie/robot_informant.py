from command import Command
import json

class RobotInformant:
	def __init__(self, configPath : str) -> None:
		self._deserialize(configPath)
		if self.commands == []: raise CreatingRobotException()
		
	def __getitem__(self, key : str) -> str:
		result = None
		for command in self.commands:
			result = command if key == command.text else None
		return result

	def _deserialize(self, configPath : str) -> None:
		with open(configPath, encoding = "UTF-8") as file:
			self.__dict__.update(**json.loads(file.read()))
		self.commands = list(map(lambda arg: Command(**arg), self.commands))

class CreatingRobotException(BaseException):
	def __init__(self) -> None:
		self.message = "Creating robot exception"

	def __str__(self) -> str:
		return self.message
