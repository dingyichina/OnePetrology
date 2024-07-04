from aip import AipSpeech
from wave import open as wave_open
from pydub import AudioSegment
""" 你的 APPID AK SK """
APP_ID = '67832249'
API_KEY = 'Lq2LrRXGNevdUifgPxQdO0TS'
SECRET_KEY = '0WFSWlbOCyh97qxiwueSicW3hKrWvCbD'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()



# 识别本地文件
rtn = client.asr(get_file_content('test-audio-file.wav'), 'wav', 16000)

print(rtn)

