from command import Command
from json import loads

class Deserializer:
    def __init__(self, filePath : str) -> None:
        with open(filePath, encoding = "UTF-8") as file:
            self.data = loads(file.read())
        print(self)	
		
    def __str__(self) -> str:
        return self.data.__str__()

    def decode(self) -> [Command]:
        result = []
        for item in self.data["robot_commands"]:
            result.append(Command(item["text"], item["callbacks"]))
        return result
