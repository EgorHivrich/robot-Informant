from robot_informant import *
import functions

def main() -> None:
	robot = RobotInformant("config.json")
	command_text = functions.convert_speech_to_text()
	
	functions.speak(robot[command_text].getRandomCallback())
	
if __name__ == "__main__":
	main()
