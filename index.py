#import the gTTS module
from gtts import gTTS  #pyttsx3
#import thid module to play converted audio
from playsound import playsound


text_fil='Enter what you want me to say'


language = 'en'
obj = gTTS(
    text=text_fil,
    lang=language,
    slow=False
)
#save the file
obj.save('exam.mp3')

#play the file
playsound('exam.mp3')

