from pydub import AudioSegment
import os
import time
from sha256 import sha256
from parseText import parseText
from openai_tts import tts
# from baidu_tts import tts
from rewrite_text import rewrite_text

class Meditation:
    audio = AudioSegment.silent(duration=1000)

    # bgm是bgm.mp3的前5秒，降低12dB
    bgm = AudioSegment.from_mp3("bgm.mp3")[0:5000] - 12

    shortBgm = AudioSegment.from_mp3("bgm.mp3")[0:800] - 12

    cacheRoot = "cache/"

    def addSegment(self, text, isTitle, longBgm=False):
        """
        :param text: 文本
        :param delay: 朗读文本后的延迟，单位秒
        :param withBgm: 是否使用bgm，否则使用短bgm
        """
        delay = 0 if isTitle else 5
        if not isTitle:
            text = rewrite_text(text)
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
            time.sleep(15)
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

def generateMeditation(simple, output):
    """
    simple: 是否使用简化版
    output: 输出文件名
    """
    meditation = Meditation()
    items = parseText(simple)
    for item in items:
        try:
            meditation.addSegment(item[0], item[1])
        except Exception as e:
            print(e)
    meditation.save(output)

if __name__ == '__main__':
    generateMeditation(False, "meditation.mp3")
    generateMeditation(True, "meditation_simple.mp3")
