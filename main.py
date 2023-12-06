from pydub import AudioSegment
from gtts import gTTS
from io import BytesIO
from parseText import parseText


class Meditation:
    audio = AudioSegment.silent(duration=1000)

    # bgm是bgm.mp3的前5秒，降低12dB
    bgm = AudioSegment.from_mp3("bgm.mp3")[0:5000] - 12

    shortBgm = AudioSegment.from_mp3("bgm.mp3")[0:800] - 12

    def addSegment(self, text, time=0.0, withBgm=True):
        tts = gTTS(text=text, lang='zh-TW')
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        add = AudioSegment.from_mp3(mp3_fp)
        if withBgm:
            self.audio = self.audio + self.bgm
        else:
            self.audio = self.audio + self.shortBgm
        self.audio = self.audio + add
        if time > 0:
            silent = AudioSegment.silent(duration=int(time * 1000))
            self.audio = self.audio + silent

    def save(self, audioName):
        self.audio.export(audioName, format="mp3")


if __name__ == '__main__':
    m = Meditation()
    m.addSegment('找到舒服的姿势', 15)
    m.addSegment('开始深呼吸', 60)
    m.addSegment('开始环境冥想', 60)
    m.addSegment('开始身体扫描', 60)
    m.addSegment('开始感恩冥想', 60)
    m.addSegment('开始慈爱冥想', 120)
    m.addSegment('开始慈爱冥想2', 2)
    items = parseText()
    for item in items:
        m.addSegment(item[0], item[1], item[2])
    m.addSegment('开始专注冥想', 60)
    m.addSegment('开始放松意识', 60)
    m.addSegment('完成冥想')
    m.save("meditation.mp3")


