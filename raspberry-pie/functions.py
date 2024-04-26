import pyttsx3, speech_recognition, asyncio, time

"""Add recognition, and I should make async speaking"""

async def speak(message : str) -> None:
	driver = pyttsx3.init()
	pyttsx3.speak(message)
	
	driver.runAndWait()
	
	await input_async()
	
async def convert_speech_to_text() -> str: 
	pass
	
	
async def input_async() -> None:
	result = input()
	print(result)
