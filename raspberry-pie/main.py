from command import Command, CreatingCommandException
from deserializer import Deserializer

def main() -> None:
	command = Command("hello", ["hello", "hi"])
	print(command)
	
	deserializer = Deserializer("config.json")
	print(deserializer)
	
	try:
		error = Command("", [])
	except CreatingCommandException as exception:
		print(exception)
	
if __name__ == "__main__":
	main()
