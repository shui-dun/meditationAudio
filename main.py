from pydub import AudioSegment
from gtts import gTTS
from io import BytesIO
import os
import time as t

audio = AudioSegment.silent(duration=1000)


def addSegment(text, time=0):
    global audio
    tts = gTTS(text=text, lang='zh-tw')
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    add = AudioSegment.from_mp3(mp3_fp)
    silent = AudioSegment.silent(duration=int(time * 1000 * 60))
    audio = audio + add + silent


def save(audioName):
    audio.export(audioName, format="mp3")


def meditation1():
    addSegment('找到舒服的姿势', 1 / 60)
    addSegment('开始深呼吸', 1)
    addSegment('开始环境冥想', 2)
    addSegment('开始视觉冥想', 4)
    addSegment('开始感恩冥想', 4)
    addSegment('开始慈爱冥想', 2)
    addSegment('开始放松意识', 4)
    addSegment('开始环境冥想', 2)
    addSegment('完成冥想')
    save("meditation1.mp3")


def meditation2():
    addSegment('找到舒服的姿势', 1 / 60)
    addSegment('开始深呼吸', 1)
    addSegment('开始环境冥想', 2)
    addSegment('开始身体扫描', 3)
    addSegment('开始慈悲冥想', 3)
    addSegment('开始专注冥想', 4)
    addSegment('开始放松意识', 4)
    addSegment('开始环境冥想', 2)
    addSegment('完成冥想')
    save("meditation2.mp3")


if __name__ == '__main__':
    start = t.time()
    meditation2()
    print(t.time() - start)
