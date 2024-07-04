import os

import flet as ft
import flet.fastapi as flet_fastapi
from flet.fastapi import FletStaticFiles
from fastapi.responses import FileResponse
from baiduxueshu import main as baiduxueshu


app = flet_fastapi.FastAPI()

# 设置环境变量
os.environ['FLET_FORCE_WEB_SERVER'] = 'true'  # 强制后台服务无窗口

# app.mount(path="/export", app=FletStaticFiles("."))

@app.get("/ref/export/{filename}")  #此时也需要带上应用的上下文
def download(filename: str):
    file_name = os.path.basename(filename)
    return FileResponse(path="./export/"+file_name,media_type="application/octet-stream")
    response.headers["Content-Disposition"] = 'attachment; filename*=UTF-8\'\'' + file_name



app.mount("/ref", flet_fastapi.app(baiduxueshu,assets_dir="D:/code/DDE/11-python/爬虫/assets"))


# 运行 FastAPI 应用
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)