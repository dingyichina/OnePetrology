import logging
import os
import re
import threading
import time
import zipfile
from datetime import  datetime

import flet as ft
import requests
from playwright.sync_api import Playwright, sync_playwright
from starlette.responses import FileResponse

logging.basicConfig(level=logging.INFO)

def download_file(url, local_filename):
    # 发送HTTP GET请求
    with requests.get(url, stream=True) as r:
        r.raise_for_status()  # 确保请求成功
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)


def make_valid_dir_name(s):
    # Windows不允许的字符：<>:"/\|?*
    invalid_chars = re.compile(r'[<>:"/\\|?*]')
    # 替换为下划线
    s = invalid_chars.sub('_', s)

    # 将空格替换为下划线
    s = s.replace(' ', '_')

    # 确保字符串不以点或空格结尾（这也是不允许的）
    while s.endswith(('.', '_')):
        s = s[:-1]
    # 如果超长，取最左边的10个
    # 获取当前时间戳
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    # 将时间戳添加到字符串末尾
    dir_name = f"{s[:10]}_{timestamp}"
    return dir_name

def zip_directory(directory_path, zip_file_path):
    # 创建一个zip文件写入对象
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # 遍历目录下的所有文件和子目录
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                # 构造文件的全路径
                file_path = os.path.join(root, file)
                # 将文件添加到zip文件中
                # arcname参数是文件在zip中的名字，这里我们使用相对路径
                zipf.write(file_path, arcname=os.path.relpath(file_path, start=directory_path))
def main(page: ft.Page):
    page.title = "OnePetrology 参考文献补全工具"
    page.tooltip = "DDE OnePetrology by xugang & dingyi"



    def theme_changed( e):
        if e.control.icon == ft.icons.BRIGHTNESS_2:
            page.theme_mode = ft.ThemeMode.DARK
            e.control.icon = ft.icons.BRIGHTNESS_HIGH
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            e.control.icon = ft.icons.BRIGHTNESS_2
        page.update()
    page.appbar = ft.AppBar(
        leading=ft.Image(src="/images/DDE-logo.png"),
        leading_width=40,
        title=ft.Text("OnePetrology 参考文献补全工具（依据百度学术）"),  # ft.Row([ft.Image(src="/images/DDE-logo.png"),ft.Text("OnePetrology")]),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[

            ft.IconButton(
                icon=ft.icons.BRIGHTNESS_2,
                tooltip="Toggle brightness",
                on_click=theme_changed,
            ),
            # ft.IconButton(icon=ft.icons.MORE_VERT),
        ],
    )
    txtSearch = ft.TextField(width=600,label="关键词或者百度学术链接", hint_text="请输入关键词或者百度学术完整参数链接")
    c1 = ft.Checkbox(label="导出BibTeX", value=False)
    c2 = ft.Checkbox(label="导出EndNote", value=False)
    c3 = ft.Checkbox(label="导出RefMan", value=True)
    c4 = ft.Checkbox(label="导出NoteFirst", value=False)
    c5 = ft.Checkbox(label="导出NoteExpress", value=False)
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    btnSearch = ft.ElevatedButton(text="搜索", icon=ft.icons.START)
    logging.basicConfig(format='%(asctime)s | %(levelname)s : %(message)s', level=logging.INFO)


    def handle(request, response):
        if response is not None:
            # print(response)
            # response url 是网站请求数据的url
            if response.url.startswith('https://xueshu.baidu.com'):
                pass
                # print(response)
                # handle_json(response.json())
    # 临时变量，记录当前目录


    def getRef(page, dstPath="export"):  # 出现多页结果
        # 查找所有引用的组件
        rtn = []  # 返回数组
        mylocator = page.get_by_title('引用', exact=True)
        mycount = 0
        for i in range(0, mylocator.count()):
            mylocator.nth(i).click()
            # 此时需要定位弹出窗口
            # with page.expect_popup() as popup_info:
            # 此时通过弹出窗口提取信息
            # print(popup_info.value)

            gbt = page.text_content(
                "#sc_quote_wr > div.sc_quote_content > div.sc_quote_list > div:nth-child(1) > div.sc_quote_list_item_r > p")
            mla = page.text_content(
                "#sc_quote_wr > div.sc_quote_content > div.sc_quote_list > div:nth-child(2) > div.sc_quote_list_item_r > p")
            apa = page.text_content(
                "#sc_quote_wr > div.sc_quote_content > div.sc_quote_list > div:nth-child(3) > div.sc_quote_list_item_r > p")
            paperid = page.locator(
                "#sc_quote_wr > div.sc_quote_content > div.sc_quote_citi > a:nth-child(3)").last.get_attribute(
                'data-paperid')
            # 输出
            lv.controls.append(ft.Text("[{0}] {1}".format(len(lv.controls)+1,gbt[3:])))
            lv.update()
            # 导出BibTeX
            if c1.value:
                subdir = dstPath+ "/BibTeX"
                if not os.path.exists(subdir):
                    os.mkdir(subdir)
                url = "https://xueshu.baidu.com/u/citation?type=bib&paperid={0}".format(paperid)
                filename = "{0}/[{1}]{2}.bib".format(subdir,len(lv.controls),paperid)
                download_file(url,filename)
            if c2.value:
                subdir = dstPath+ "/EndNote"
                if not os.path.exists(subdir):
                    os.mkdir(subdir)
                url = "https://xueshu.baidu.com/u/citation?type=enw&paperid={0}".format(paperid)
                filename = "{0}/[{1}]{2}.enw".format(subdir,len(lv.controls), paperid)
                download_file(url, filename)
            if c3.value:
                subdir = dstPath+ "/RefMan"
                if not os.path.exists(subdir):
                    os.mkdir(subdir)
                url = "https://xueshu.baidu.com/u/citation?type=ris&paperid={0}".format(paperid)
                filename = "{0}/[{1}]{2}.ris".format(subdir, len(lv.controls),paperid)
                download_file(url, filename)
                # 如果是ris，则拼接一个完整的文件

                # 读取源文件内容
                with open(filename, 'r',encoding='utf-8') as source_file:
                    content = source_file.read()

                filepath = dstPath + "/all.ris"
                with open(filepath, 'a', encoding='utf-8') as file:
                    # 写入一个空行
                    file.write(os.linesep)
                    # 写入源文件的内容
                    file.write(content)
            if c4.value:
                subdir = dstPath + "/NoteFirst"
                if not os.path.exists(subdir):
                    os.mkdir(subdir)
                url = "https://xueshu.baidu.com/u/citation?type=txt&paperid={0}".format(paperid)
                filename = "{0}/[{1}]{2}.txt".format(subdir, len(lv.controls),paperid)
                download_file(url, filename)
            if c5.value:
                subdir = dstPath + "/NoteExpress"
                if not os.path.exists(subdir):
                    os.mkdir(subdir)
                url = "https://xueshu.baidu.com/u/citation?type=txt&paperid={0}".format(paperid)
                filename = "{0}/[{1}]{2}.net".format(subdir, len(lv.controls),paperid)
                download_file(url, filename)
            # print("PaperId:",paperid)
            # print("GB/T 7714-2015 :", gbt)
            # print("MLA :", mla)
            # print("APA :", apa)
            filepath = dstPath+"/gbt.txt"
            with open(filepath, 'a', encoding='utf-8') as file:
                file.writelines("[{0}] {1} \n".format(len(lv.controls),gbt[3:]))  # 使用writelines追加多行
            filepath = dstPath + "/mla.txt"
            with open(filepath, 'a', encoding='utf-8') as file:
                file.writelines("[{0}] {1} \n".format(len(lv.controls), mla[3:]))
            filepath = dstPath + "/apa.txt"
            with open(filepath, 'a', encoding='utf-8') as file:
                file.writelines("[{0}] {1} \n".format(len(lv.controls), apa[3:]))

            page.click("#sc_quote_wr > div.sc_quote_top > a")
            obj = {"paperid": paperid, "gbt": gbt, "mla": mla, "apa": apa}
            rtn.append(obj)
        return rtn

    def getArticleInfo(page, dstPath="export"):  # 直接跳转到了文献的详情页
        locator = page.locator("#dtl_l > div.main-info > div.dtl_subinfo > div > a.paper_q")
        print("ArticleInfo:", locator.count())
        if locator.count() == 1:
            locator.nth(0).click()
            # 此时需要定位弹出窗口
            # with page.expect_popup() as popup_info:
            # 此时通过弹出窗口提取信息
            # print(popup_info.value)

            gbt = page.text_content(
                "#sc_quote_wr > div.sc_quote_content > div.sc_quote_list > div:nth-child(1) > div.sc_quote_list_item_r > p")
            mla = page.text_content(
                "#sc_quote_wr > div.sc_quote_content > div.sc_quote_list > div:nth-child(2) > div.sc_quote_list_item_r > p")
            apa = page.text_content(
                "#sc_quote_wr > div.sc_quote_content > div.sc_quote_list > div:nth-child(3) > div.sc_quote_list_item_r > p")
            paperid = page.locator(
                "#sc_quote_wr > div.sc_quote_content > div.sc_quote_citi > a:nth-child(2)").last.get_attribute(
                "data-paperid")
            # rtn = {"paperid": paperid, "gbt": gbt, "mla": mla, "apa": apa}

            print("PaperId:", paperid)
            print("GB/T 7714-2015 :", gbt)
            print("MLA :", mla)
            print("APA :", apa)
            page.click("#sc_quote_wr > div.sc_quote_top > a")

            # 输出
            lv.controls.append(ft.Text("[{0}] {1}".format(len(lv.controls) + 1, gbt[3:])))
            lv.update()
            # 导出BibTeX
            if c1.value:
                subdir = dstPath + "/BibTeX"
                if not os.path.exists(subdir):
                    os.mkdir(subdir)
                url = "https://xueshu.baidu.com/u/citation?type=bib&paperid={0}".format(paperid)
                filename = "{0}/[{1}]{2}.bib".format(subdir, len(lv.controls), paperid)
                download_file(url, filename)
            if c2.value:
                subdir = dstPath + "/EndNote"
                if not os.path.exists(subdir):
                    os.mkdir(subdir)
                url = "https://xueshu.baidu.com/u/citation?type=enw&paperid={0}".format(paperid)
                filename = "{0}/[{1}]{2}.enw".format(subdir, len(lv.controls), paperid)
                download_file(url, filename)
            if c3.value:
                subdir = dstPath + "/RefMan"
                if not os.path.exists(subdir):
                    os.mkdir(subdir)
                url = "https://xueshu.baidu.com/u/citation?type=ris&paperid={0}".format(paperid)
                filename = "{0}/[{1}]{2}.ris".format(subdir, len(lv.controls), paperid)
                download_file(url, filename)
                # 如果是ris，则拼接一个完整的文件

                # 读取源文件内容
                with open(filename, 'r', encoding='utf-8') as source_file:
                    content = source_file.read()

                filepath = dstPath + "/all.ris"
                with open(filepath, 'a', encoding='utf-8') as file:
                    # 写入一个空行
                    file.write(os.linesep)
                    # 写入源文件的内容
                    file.write(content)
            if c4.value:
                subdir = dstPath + "/NoteFirst"
                if not os.path.exists(subdir):
                    os.mkdir(subdir)
                url = "https://xueshu.baidu.com/u/citation?type=txt&paperid={0}".format(paperid)
                filename = "{0}/[{1}]{2}.txt".format(subdir, len(lv.controls), paperid)
                download_file(url, filename)
            if c5.value:
                subdir = dstPath + "/NoteExpress"
                if not os.path.exists(subdir):
                    os.mkdir(subdir)
                url = "https://xueshu.baidu.com/u/citation?type=txt&paperid={0}".format(paperid)
                filename = "{0}/[{1}]{2}.net".format(subdir, len(lv.controls), paperid)
                download_file(url, filename)
            # print("PaperId:", paperid)
            # print("GB/T 7714-2015 :", gbt)
            # print("MLA :", mla)
            # print("APA :", apa)
            filepath = dstPath + "/gbt.txt"
            with open(filepath, 'a', encoding='utf-8') as file:
                file.writelines("[{0}] {1} \n".format(len(lv.controls), gbt[3:]))  # 使用writelines追加多行
            filepath = dstPath + "/mla.txt"
            with open(filepath, 'a', encoding='utf-8') as file:
                file.writelines("[{0}] {1} \n".format(len(lv.controls), mla[3:]))
            filepath = dstPath + "/apa.txt"
            with open(filepath, 'a', encoding='utf-8') as file:
                file.writelines("[{0}] {1} \n".format(len(lv.controls), apa[3:]))

            obj = {"paperid": paperid, "gbt": gbt, "mla": mla, "apa": apa}

            return obj
        else:
            return {}

    def run(playwright: Playwright, keywords="Magmatics",outpath=".") -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(ignore_https_errors=True)

        # Open new page
        web_page = context.new_page()

        web_page.on("request", lambda request: handle(request=request, response=None))
        web_page.on("request", lambda request: handle(request=request, response=None))
        web_page.on("response", lambda response: handle(response=response, request=None))
        # url是网页加载的URL
        url = ''
        if keywords.startswith('https://xueshu.baidu.com'):
            url = keywords
        else:

            url = 'https://xueshu.baidu.com/s?wd=' + keywords.replace(' ',
                                                                  '+') + '&rsv_bp=0&tn=SE_baiduxueshu_c1gjeupa&rsv_spt=3&ie=utf-8&f=8&rsv_sug2=1&sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&rsv_n=2'  # 'https://xueshu.baidu.com/'
        web_page.goto(url)
        # 在输入框输入关键词
        # page.fill("#kw",keywords)
        # page.click("#su")
        rtn = []  # 返回数组
        # 监测是直接找到了一篇文章还是找到了列表
        mylocator = web_page.locator("#dtl_l > div.main-info > h3 > a")
        # print("查到的结果：",mylocator.count())
        if mylocator.count() > 0:
            # 此时找到的是一篇文章
            print("文章详情")
            article = getArticleInfo(web_page,dstPath=outpath)
            rtn.append(article)

            pass
        else:
            print("列表")
            start = 0

            # 此时找到的是列表
            while btnSearch.text == "停止":

                # page.update()
                rtn.extend(getRef(web_page,dstPath=outpath))
                # 如果有下一页，则点击
                if web_page.locator("#page > a.n").count() > start:
                    start = 1
                    web_page.locator("#page > a.n").last.click()
                    time.sleep(5)  # 休眠两秒,等待网络反应
                    continue
                else:
                    break  # 此时没有下一页，退出
        # 关闭窗口
        # 然后之前看到有说道网站动态加载，拖动的问题。playwright可以直接用page.mouse.wheel(0, 300)解决
        web_page.wait_for_timeout(5000)  # 这个时间根据网速调整
        # ---------------------
        context.close()
        web_page.close()
        browser.close()
        # 下载完成后处理
        btnSearch.icon = ft.icons.SEARCH
        btnSearch.text = "搜索"
        page.update()
        # 压缩结果成一个文件，供下载
        zip_directory(page.session.get("cur_oper_dir"),"{0}.zip".format(page.session.get("cur_oper_dir")))
        # 显示

        show_download(True)
        return rtn

    def seachonline():
        keywords = txtSearch.value
        if keywords.startswith('https://xueshu.baidu.com'):
            keywords = '自定义搜索'
        # 建目录
        if not os.path.exists("export"):
            os.mkdir("export")
        if not page.session.contains_key("cur_oper_dir") :
            dstpath = "export/" + make_valid_dir_name(keywords)
            page.session.set("cur_oper_dir",dstpath)
        else:
            dstpath = page.session.get("cur_oper_dir")
        if not os.path.exists(dstpath):
            os.mkdir(dstpath)
        with sync_playwright() as playwright:
            try:
                run(playwright, txtSearch.value, outpath=dstpath)
            except Exception as e:
                print(e)
                btnSearch.icon=ft.icons.SEARCH
                btnSearch.text = "搜索"
                show_download(True)
                dlg = ft.AlertDialog(
                    title=ft.Text("错误信息"), content=ft.Text(str(e)),on_dismiss=lambda e: print("对话框已关闭！")
                )
                page.dialog = dlg
                dlg.open = True
                page.update()
    def doSearch(e):


        if btnSearch.text == "停止":
            btnSearch.icon = ft.icons.SEARCH
            btnSearch.text = "搜索"
            btnSearch.update()
        else:
            if txtSearch.value.strip() == "":
                dlg = ft.AlertDialog(
                    title=ft.Text("错误信息"), content=ft.Text("请输入搜索内容！"),
                    on_dismiss=lambda e: print("对话框已关闭！")
                )
                page.dialog = dlg
                dlg.open = True
                page.update()
                return
            th = threading.Thread(target=seachonline, args=(), daemon=True)
            th.start()
            btnSearch.icon = ft.icons.STOP
            btnSearch.text = "停止"
            btnSearch.update()
            # 显示
            show_download(False)
            # 发送消息
            if txtSearch.value.startswith('https://xueshu.baidu.com'):
                page.pubsub.send_others_on_topic("ref search","有人在进行自定义搜索......")
            else:
                page.pubsub.send_others_on_topic("ref search",f"有人在搜索：{txtSearch.value}")
        pass


    btnSearch.on_click = doSearch
    res1 = ft.Container(
        ft.Text(""),
        alignment=ft.alignment.center_right,
        width=250,
        height=30,
        # bgcolor=ft.colors.GREEN,
        margin=ft.margin.only(left=30)
    )
    def do_download_result(e):

        filename = "/ref/{0}.zip".format(page.session.get('cur_oper_dir'))  # 此时需要加上应用的上下文，参看ref-api
        page.launch_url(filename)
        # return FileResponse(
        #     filename,
        #     filename=os.path.basename(filename),
        #     media_type="application/octet-stream"  # 根据文件类型设置正确的 media_type
        # )
        # pass

    res2 = ft.Container(
        ft.ElevatedButton("download result",icon=ft.icons.DOWNLOAD,on_click=do_download_result),
        alignment=ft.alignment.center_right,
        width=350,
        height=30,
        margin=ft.margin.only(left=30)
        # bgcolor=ft.colors.YELLOW,
    )
    ani = ft.AnimatedSwitcher(
        res1,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,

    )

    def show_download(download:bool):
        if download:
            if len(lv.controls)>0:
                ani.content = res2
            else:
                ani.content = res1
        else:
            ani.content = res1
        ani.update()
    # 显示结果部分


    page.add(ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[
        txtSearch,
        btnSearch,
        ani,
     
    ]))

    page.add(ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[
        ft.Text("请选择导出格式："),c1,c2,c3,c4,c5
    ]))

    # print(f"Initial route: {page.route}")
    logging.getLogger("flet_core").info("Initial route: %s", page.route)
    # page.go(page.route)

    result = ft.Container(
        border=ft.Border.top,
        expand=1,
        content=lv,
        border_radius=70,

    )



    page.add(result)
    page.add(ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[
        ft.Text("Copyright @2024, author by : xugang & dingyi",text_align=ft.TextAlign.RIGHT,expand=1)
    ]))


    def on_message(topic, message):
        page.snack_bar = ft.SnackBar(ft.Text(message))
        page.snack_bar.open = True
        page.update()

    page.pubsub.subscribe_topic("ref search", on_message)

    page.update()

logging.getLogger("flet_core").setLevel(logging.INFO)
# ft.app(main )#)#,
