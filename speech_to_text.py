import speech_recognition as sr
r= sr.Recognizer()
with sr.Microphone() as source:
    print('듣고 있어요')
    audio = r.listen(source)

try:
    # 구글 API 로 인식
    # 영어문장
    # text = r.recognize_google(audio, language='en-US')
    # print(text)

    # 한글 문장
    text = r.recognize_google(audio, language='ko')
    print(text)
    
except sr.UnknownValueError:
    print('인식 실패')
except sr.RequestError as e:
    print('요청 실패 : {0}'.format(e))