import pyttsx3, speech_recognition, asyncio, time
	
def convert_speech_to_text() -> str:
	result, recognizer = "", speech_recognition.Recognizer()
	with speech_recognition.Microphone() as source:
		result = recognizer.listen(source)
	return recognizer.recognize_google(result, language = "ru-RU").lower()

def speak(message : str) -> None:
	driver = pyttsx3.init()
	pyttsx3.speak(message)
	
	driver.runAndWait()
