rem  打包主程序
pyinstaller -D -n  "DDE-OnePetrology"  --collect-all pandasgui --collect-all opencv-python --collect-all pyecharts --collect-all xmind --collect-all pyproj --collect-all xlrd --collect-all qtstylish   --collect-all sklearn -i "res/DDE-logo.ico"  --add-data  "config;config"  --add-data  "res;res" --add-data  "geopytool;geopytool" --add-data  "geopandas;geopandas" -w AppMain.py --noconsole  -y

rem  打包update升级程序 
pyinstaller -D -n  "update"   -i "res/DDE-logo.ico"    --add-data  "res;res" -w UpdateDlg.py --noconsole  -y  


rem  使用qgis的shell进行打包的脚本
rem  "D:\QGIS 3.22\bin\python-qgis-ltr.bat" -m PyInstaller -D -n  "update"   -i "res/DDE-logo.ico"    --add-data  "res;res" -w UpdateDlg.py --noconsole  -y


"D:\QGIS 3.22.12\bin\python-qgis-ltr.bat" -m PyInstaller ^
--add-data="D:\QGIS 3.22.12\apps\qgis-ltr\plugins;qgis\plugins" ^
--add-data="D:\QGIS 3.22.12\apps\Python39\Lib\site-packages\PyQt5\*.pyd;PyQt5" ^
--add-data="D:\QGIS 3.22.12\apps\qt5\plugins\styles;PyQt5\Qt\plugins\styles" ^
--add-data="D:\QGIS 3.22.12\apps\qt5\plugins\iconengines;PyQt5\Qt\plugins\iconengines" ^
--add-data="D:\QGIS 3.22.12\apps\qt5\plugins\imageformats;PyQt5\Qt\plugins\imageformats" ^
--add-data="D:\QGIS 3.22.12\apps\qt5\plugins\platforms;PyQt5\Qt\plugins\platforms" ^
--add-data="D:\QGIS 3.22.12\apps\qt5\plugins\platformthemes;PyQt5\Qt\plugins\platformthemes" ^
 -D -n  "DDE-OnePetrology"  --collect-all pandasgui --collect-all opencv-python --collect-all pyecharts --collect-all xmind --collect-all pyproj --collect-all xlrd --collect-all qtstylish   --collect-all sklearn -i "res/DDE-logo.ico"  --add-data  "config;config"  --add-data  "res;res" --add-data  "geopytool;geopytool" --add-data  "geopandas;geopandas" -w AppMain.py --noconsole  -y






rem pyinstaller -D -n  "DDE-OnePetrology"   --splash "res/splash.png"   -i "res/DDE-logo.ico"  -w AppMain.py

rem pyecharts
rem qtstylish

rem  主程序打包后容易出现找不到QtWebEngineProcess.exe的问题，处理方法：将PyQt5/Qt/bin（dist目录下也有）目录下的QtWebEngineProcess.exe和PyQt5/Qt/resource目录下的所有文件复制到dist目录下

rem 如果opencv错误，则大概率需要降低opencv的版本

rem  安装qgis（mamba install -c conda-forge  qgis）之后，遇到qtwebengine的问题之后，需要先卸载pyqt5，然后再重装即可。  然后把library\python下面的qgis复制到Lib\site-packages中，可以解决找不到qgis的问题。

rem  安装qgis的ltr版本，然后用osgeo4w shell进行 python包的安装。遇到pyqtwebengine不兼容的问题，需要按照下面方式解决:  https://blog.csdn.net/weixin_46770425/article/details/119493999
rem        python3 -m pip install --upgrade pip
rem        pip3 install SIP

rem        pip3 install pyQt5

rem        pip3 install --upgrade PyQt5

rem        pip3 install PyQtWebEngine
rem *********最重要的是保证 pyqt5的版本与qgis的版本一致   ***********，即，需要限定pyqtwebengine的版本，仍然有冲突时，卸载 pyqt5-qt包可以解决

rem   安装3.22 ltr版本，用OsGeo4w shell（管理员运行）安装缺失的包，然后把pyqt5卸载了重新安装为 5.15.3

rem  pip install requests_toolbelt pandasgui keras pyarango xlsxwriter scikit-learn tensorflow pypiwin32 pyecharts  camelot-py opencv-python beautifulsoup4 pyqtwebengine==5.15.3 markupsafe==2.0.1
rem  python -m pip install markupsafe==2.0.1   # 降低版本以规避错误
rem  现在冲突的是5.15.2 版本的pyqt5-qt ，解决这个问题的方法是： Qgis\apps\qt5  下面的所有文件，复制到  qgis\apps\python39\lib\site-packages\pyqt5\qt 下面，即强制把qt的版本升级到5.15.3 (默认的最新版本是5.15.2）



****************************************
qgis shell下需要安装的包

pip install  requests_toolbelt pyArango pandasgui xlsxwriter pyecharts camelot-py opencv-python scikit-learn bs4 keras tensorflow pypiwin32 xmind