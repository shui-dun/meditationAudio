from pydub import AudioSegment
from gtts import gTTS
from io import BytesIO


class Meditation:
    audio = AudioSegment.silent(duration=1000)

    def addSegment(self, text, time=0.0):
        tts = gTTS(text=text, lang='zh-tw')
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        add = AudioSegment.from_mp3(mp3_fp)
        silent = AudioSegment.silent(duration=int(time * 1000 * 60))
        self.audio = self.audio + add + silent

    def save(self, audioName):
        self.audio.export(audioName, format="mp3")


def meditation1():
    m = Meditation()
    m.addSegment('找到舒服的姿势', 5 / 60)
    m.addSegment('开始深呼吸', 1)
    m.addSegment('开始环境冥想', 2)
    m.addSegment('开始视觉冥想', 4)
    m.addSegment('开始感恩冥想', 4)
    m.addSegment('开始慈爱冥想', 2)
    m.addSegment('开始放松意识', 4)
    m.addSegment('开始环境冥想', 2)
    m.addSegment('完成冥想')
    m.save("meditation1.mp3")


def meditation2():
    m = Meditation()
    m.addSegment('找到舒服的姿势', 5 / 60)
    m.addSegment('开始深呼吸', 1)
    m.addSegment('开始环境冥想', 2)
    m.addSegment('开始身体扫描', 3)
    m.addSegment('开始慈悲冥想', 3)
    m.addSegment('开始专注冥想', 4)
    m.addSegment('开始放松意识', 4)
    m.addSegment('开始环境冥想', 2)
    m.addSegment('完成冥想')
    m.save("meditation2.mp3")


if __name__ == '__main__':
    meditation1()
    meditation2()
