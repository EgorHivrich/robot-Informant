import pyttsx3, speech_recognition, asyncio

"""Add recognition, and I should make async speaking"""

async def speak(message : str) -> None:
	driver = pyttsx3.init()
	await pyttsx3.speak(message)
	
def recognize_speech() -> str: 
	pass
