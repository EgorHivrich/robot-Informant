from robot_informant import *

def main() -> None:
	robot = RobotInformant("config.json")
	
	print(robot.commands[0].text)
	
if __name__ == "__main__":
	main()
