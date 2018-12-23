#! /usr/bin/env python
import os
import sys

from gtts import gTTS

# different microphones can return different level of signal
rms_multiplyer = 1
mp3_name = 'warning.mp3'
language = 'ru'

def get_message(rms):
    rms = int(rms)
    if rms < 4000:
        return 'Tише!'
    elif rms < 5000:
        return 'Тише! Вашу мать!!'
    elif rms < 7000:
        return 'Тише! Ёб Вашу мать!'
    else:
        return 'Да Вы совсем ахуели!'

def main():
    try:
        rms = sys.argv[1] * rms_multiplyer
    except IndexError:
        print('no rms')
        rms = "4000"

    mytext = get_message(rms)
    tts = gTTS(text=mytext, lang=language, slow=False)
    tts.save(mp3_name)

    from sys import platform as _platform
    if _platform == "linux" or _platform == "linux2":
        pass
    elif _platform == "darwin":
        os.system("afplay " + mp3_name)

if __name__ == "__main__":
    main()
