# import pyttsx3		#pip install pyttsx3
#
#
# #Инициализация голосового "движка" при старте программы
# #
# #Голос берется из системы, первый попавшийся
# #
# #Доп материал:
# #https://pypi.org/project/pyttsx3/
# #https://pyttsx3.readthedocs.io/en/latest/
# #https://github.com/nateshmbhat/pyttsx3
# #На Linux-ax, скорее всего нужно еще:
# #sudo apt update && sudo apt install espeak ffmpeg libespeak1
#
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)				#скорость речи
# engine.setProperty('voice', 'ru')
#
#
# def speaker(text):
# 	'''Озвучка текста'''
# 	engine.say(text)
# 	engine.runAndWait()


from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play


def speaker(text):
    tts = gTTS(text=text, lang='ru', slow=False)
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    audio = AudioSegment.from_file(mp3_fp, format="mp3")
    play(audio)