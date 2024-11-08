from pydub import AudioSegment
import os
from sha256 import sha256
from parseText import parseText
from openai_tts import tts


class Meditation:
    audio = AudioSegment.silent(duration=1000)

    # bgm是bgm.mp3的前5秒，降低12dB
    bgm = AudioSegment.from_mp3("bgm.mp3")[0:5000] - 12

    shortBgm = AudioSegment.from_mp3("bgm.mp3")[0:800] - 12

    cacheRoot = "cache/"

    def addSegment(self, text, delay=0.0, longBgm=False):
        """
        :param text: 文本
        :param delay: 朗读文本后的延迟，单位秒
        :param withBgm: 是否使用bgm，否则使用短bgm
        """
        # 如果不存在cache目录，则生成
        if not os.path.exists(self.cacheRoot):
            os.mkdir(self.cacheRoot)
        # 计算文本的sha256值
        textHash = sha256(text)
        # 缓存文件
        cacheFile = os.path.join(self.cacheRoot, textHash + ".mp3")
        # 如果不存在，则调用tts生成
        if not os.path.exists(cacheFile):
            tts(text, cacheFile)
            # time.sleep(30)
        else:
            print("cache hit: " + text)
        # 读取缓存文件
        add = AudioSegment.from_mp3(cacheFile)
        if longBgm:
            self.audio = self.audio + self.bgm
        else:
            self.audio = self.audio + self.shortBgm
        self.audio = self.audio + add
        if delay > 0:
            silent = AudioSegment.silent(duration=int(delay * 1000))
            self.audio = self.audio + silent

    def save(self, audioName):
        self.audio.export(audioName, format="mp3")


if __name__ == '__main__':
    m = Meditation()
    items = parseText()
    for item in items:
        m.addSegment(item[0], item[1])
    m.addSegment('完成冥想')
    m.save("meditation.mp3")
