"D:\QGIS 3.22\bin\python-qgis-ltr.bat" -m PyInstaller ^
--add-data="D:\QGIS 3.22\apps\qgis-ltr\plugins;qgis\plugins" ^
--add-data="D:\QGIS 3.22\apps\Python39\Lib\site-packages\PyQt5\*.pyd;PyQt5" ^
--add-data="D:\QGIS 3.22\apps\qt5\plugins\styles;PyQt5\Qt\plugins\styles" ^
--add-data="D:\QGIS 3.22\apps\qt5\plugins\iconengines;PyQt5\Qt\plugins\iconengines" ^
--add-data="D:\QGIS 3.22\apps\qt5\plugins\imageformats;PyQt5\Qt\plugins\imageformats" ^
--add-data="D:\QGIS 3.22\apps\qt5\plugins\platforms;PyQt5\Qt\plugins\platforms" ^
--add-data="D:\QGIS 3.22\apps\qt5\plugins\platformthemes;PyQt5\Qt\plugins\platformthemes" ^
 -D -n  "DDE-OnePetrology"  --collect-all pandasgui --collect-all opencv-python --collect-all pyecharts --collect-all xmind --collect-all pyproj --collect-all xlrd --collect-all qtstylish   --collect-all sklearn -i "res/DDE-logo.ico"  --add-data  "config;config"  --add-data  "res;res" --add-data  "geopytool;geopytool" --add-data  "geopandas;geopandas" -w AppMain.py --noconsole  -y

