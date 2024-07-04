from qgis._core import QgsCoordinateReferenceSystem
from qgis.core import QgsApplication, QgsProject, QgsRasterLayer
from qgis.gui import QgsMapCanvas

if __name__ == "__main__":

    # Create a reference to the QgsApplication.  Setting the
    # second argument to False disables the GUI.
    # QgsApplication.setPrefixPath("qgis", True)
    qgs = QgsApplication([], True)
    # QgsApplication.setPrefixPath("D:\\QGIS 3.22.12", True)
    print("prefix", QgsApplication.prefixPath())
    qgs.initQgis()
    # app = QApplication(sys.argv)
    project = QgsProject.instance()
    # Print the current project file name (might be empty in case no projects have been loaded)
    # print(project.fileName())

    # Load another project
    project.read('shp2web/shp2web.qgz')
    print(project.crs())
    # project.setCrs(QgsCoordinateReferenceSystem("EPSG:4326"))
    layers =[]
    for layer in project.mapLayers():
        if project.mapLayer(layer).isValid():
            layers.append(project.mapLayer(layer))
            print(layer,project.mapLayer(layer).crs())
        else:
            print(layer, " is invalid")
            # layers.append(project.mapLayer(layer))
        # print(layer)#
    # 添加底图
    urlWithParams = 'crs=EPSG:4326&dpiMode=7&format=image/png&layers=dde:world2022&styles=&tileMatrixSet=EPSG:4326&url=https://petrology.deep-time.org/geoserver/gwc/service/wmts'
    rlayer = QgsRasterLayer(urlWithParams, 'DDE岩浆岩图2022', 'wms')
    print(rlayer,rlayer.crs())
    if not rlayer.isValid():
        print("图层加载失败！")

    layers.append(rlayer)
    # app = QApplication(sys.argv)
    # Create and show widget
    from QMapWidget import QMapWidget
    dfe = QMapWidget()

    # vlayer = QgsVectorLayer('shp2web/igneous_rock.shp', "points layer", "ogr")
    # if not vlayer.isValid():
    #     print("Layer failed to load!")

    # add layer to the registry
    # QgsProject.instance().addMapLayer(vlayer)

    # set extent to the extent of our layer
    # dfe.setExtent(vlayer.extent())

    # set the map canvas layer set
    # dfe.setLayers([vlayer])

    dfe.setLayers(layers)
    # dfe.setDestinationCrs()
    dfe.setExtent(layers[-1].extent())
    # dfe.refresh()
    dfe.show()
    # sys.exit(app.exec())
    exitCode = qgs.exec()
    qgs.exitQgis()