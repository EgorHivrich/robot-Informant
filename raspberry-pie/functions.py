import pyttsx3, speech_recognition, asyncio, time
	
def convert_speech_to_text() -> str:
	result, recognizer = "", speech_recognition.Recognizer()
	with speech_recognition.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source, duration = 0.2)
		result = recognizer.recognize_google(recognizer.listen())
	return result.lower()

def speak(message : str) -> None:
	driver = pyttsx3.init()
	pyttsx3.speak(message)
	
	driver.runAndWait()
