from __future__ import annotations
# 用于显示进度条

# 用于发起网络请求
import requests
# 用于多线程操作
import multitasking
import signal
# 导入 retry 库以方便进行下载出错重试
from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from retry import retry

signal.signal(signal.SIGINT, multitasking.killall)

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
# 定义 1 MB 多少为 B
MB = 1024 ** 2


def split(start: int, end: int, step: int) -> list[tuple[int, int]]:
    # 分多块
    parts = [(start, min(start + step, end))
             for start in range(0, end, step)]
    return parts


def get_file_size(url: str, raise_error: bool = False) -> int:
    '''
    获取文件大小
    Parameters
    ----------
    url : 文件直链
    raise_error : 如果无法获取文件大小，是否引发错误
    Return
    ------
    文件大小（B为单位）
    如果不支持则会报错
    '''
    response = requests.head(url)
    file_size = response.headers.get('Content-Length')
    if file_size is None:
        if raise_error is True:
            raise ValueError('该文件不支持多线程分段下载！')
        return file_size
    return int(file_size)

class MultiDownloader(QObject):
    # 用来更新进度条的信号
    progressSignal = QtCore.pyqtSignal(int, int)

    def __init__(self,parent=None):
        super().__init__(parent)
        pass




    def download(self,url: str, file_name: str, retry_times: int = 3, each_size=16 * MB, callback=None) -> None:
        '''
        根据文件直链和文件名下载文件
        Parameters
        ----------
        url : 文件直链
        file_name : 文件名
        retry_times: 可选的，每次连接失败重试次数
        Return
        ------
        None
        '''
        f = open(file_name, 'wb')
        file_size = get_file_size(url)

        @retry(tries=retry_times)
        @multitasking.task
        def start_download(start: int, end: int) -> None:
            '''
            根据文件起止位置下载文件
            Parameters
            ----------
            start : 开始位置
            end : 结束位置
            '''
            _headers = headers.copy()
            # 分段下载的核心
            _headers['Range'] = f'bytes={start}-{end}'
            # 发起请求并获取响应（流式）
            response = session.get(url, headers=_headers, stream=True)
            # 每次读取的流式响应大小
            chunk_size = 128
            # 暂存已获取的响应，后续循环写入
            chunks = []
            for chunk in response.iter_content(chunk_size=chunk_size):
                # 暂存获取的响应
                chunks.append(chunk)
                # 更新进度条
                self.progressSignal.emit(chunk_size, file_size)

            f.seek(start)
            for chunk in chunks:
                f.write(chunk)
            # 释放已写入的资源
            del chunks

        session = requests.Session()
        # 分块文件如果比文件大，就取文件大小为分块大小
        each_size = min(each_size, file_size)

        # 分块
        parts = split(0, file_size, each_size)
        print(f'分块数：{len(parts)}')
        # 创建进度条

        for part in parts:
            start, end = part
            start_download(start, end)
        # 等待全部线程结束
        multitasking.wait_for_tasks()
        f.close()


def update(chunkSize, totalsize):
    print(chunkSize, ' / ', totalsize)


if "__main__" == __name__:
    # url = 'https://mirrors.tuna.tsinghua.edu.cn/pypi/web/packages/0d/ea/f936c14b6e886221e53354e1992d0c4e0eb9566fcc70201047bb664ce777/tensorflow-2.3.1-cp37-cp37m-macosx_10_9_x86_64.whl#sha256=1f72edee9d2e8861edbb9e082608fd21de7113580b3fdaa4e194b472c2e196d0'
    url = 'http://8.218.13.217:8080/server/api/core/bitstreams/45846ed5-4e5e-4d9f-9d1f-0c0931706aba/content'
    file_name = 'temp.zip'
    # 开始下载文件
    MultiDownloader().download(url, file_name, callback=update)
