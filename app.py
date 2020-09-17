import speech_recognition as sr 

r = sr.Recognizer()

with sr.Microphone() as source:
	print("Speak Anything : ")
	audio = r.listen(source)

	try:
		text = r.Recognize_google(audio)
		print("You said: {}".format(text))

	except:
		print("sorry voice is not Recognize !")