# TTS (Text To Speech)
# STT (Speech To Text)

from gtts import gTTS
from playsound import playsound

# 영어 문장
# text = 'Imagine that you have just arrived at a hotel after a tiring 7-hour overnight flight.'
# tts_en = gTTS(text=text, lang='en')
file_name = 'sample.mp3'
# tts_en.save(file_name)

# 한글 문장
# text = '해그리드는 친구가 있다.'
# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save(file_name)
# playsound(file_name)

# 긴 문장
with open('sample.txt', 'r', encoding='utf-8') as f:
    text = f.read()

tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)
playsound(file_name)