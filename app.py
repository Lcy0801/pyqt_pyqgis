from urllib.parse import quote
import threading
from qgis.PyQt.QtWidgets import QMainWindow, QAction, QMenu
from qgis.PyQt.QtCore import Qt, QObject, pyqtSignal
from qgis.PyQt.QtGui import QCursor, QIcon, QMouseEvent
from mainWindow_ui import Ui_MainWindow
from dcjgcx import DCJGCX
from jydzcx import JYDZCX
from dbdzcx import DBDZCX
from jgcx import JGCX
from dzzh import DZZH
from qgis.core import (
    QgsApplication,
    QgsProject,
    QgsRasterLayer,
    QgsVectorLayer,
    QgsLayerTreeModel,
    QgsCoordinateReferenceSystem,
    QgsExpression,
    QgsFeatureRequest,
    QgsProviderRegistry,
)
from qgis.gui import (
    QgsLayerTreeMapCanvasBridge,
    QgsMapToolZoom,
    QgsMapToolPan,
    QgsLayerTreeView,
    QgsDockWidget
)
import os
import time


class AppMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, mdb):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.mdb = mdb
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setWindowIcon(QIcon("./icons/App.ico"))
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.tabToolbar.setMovable(False)
        self.normalToolbar.setMovable(False)
        self.infoToolbar.setMovable(False)
        self.leftWindowBar.setMovable(False)
        self.rightWindowBar.setMovable(False)
        self.tabToolbar.actionTriggered.connect(self.ontabToolbarActionClicked)
        self.normaltab.trigger()
        self.normalToolbar.actionTriggered.connect(self.onnormalToolbarActionClicked)
        self.dcjg.triggered.connect(self.ondcjgClicked)
        self.jydzd.triggered.connect(self.onjydzdClicked)
        self.dzdbzd.triggered.connect(self.ondbdzdClicked)
        self.jgcx.triggered.connect(self.onjgcxClicked)
        self.dzzh.triggered.connect(self.ondzzhClicked)
        self.initTdTool()
        self.loadLayers()
        self.initMap()
        self.initToc()
        # self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=LightPalette()))
        self.minWindow.triggered.connect(self.onminWindowClicked)
        self.maxWindow.triggered.connect(self.onmaxWindowClicked)
        self.closeWindow.triggered.connect(self.oncloseWindowClicked)
        self.restoreWindow.triggered.connect(self.onrestoreWindowClicked)
        self.restoreWindow.setVisible(False)
        self.setStyleSheet(
            'QToolBar#rightWindowBar,QToolBar#leftWindowBar{background-color:qlineargradient(x1:0, y1:0, x2:0, y2:1,'
            'stop:0 white,stop:1 #EAF7FF)}')
        self.tabToolbar.setStyleSheet('background-color:#EAF7FF')
        self.normalToolbar.setStyleSheet('background-color:#EAF7FF')
        self.infoToolbar.setStyleSheet('background-color:#EAF7FF')

    def mouseMoveEvent(self, e: QMouseEvent):
        if e.buttons() != Qt.LeftButton:
            return
        dx = e.globalX() - self.oldmx
        dy = e.globalY() - self.oldmy
        oldx = self.pos().x()
        oldy = self.pos().y()
        newx = oldx + dx
        newy = oldy + dy
        self.move(newx, newy)
        self.oldmx = e.globalX()
        self.oldmy = e.globalY()

    def mousePressEvent(self, e: QMouseEvent):
        self.oldmx = e.globalX()
        self.oldmy = e.globalY()

    def onminWindowClicked(self):
        self.showMinimized()

    def onmaxWindowClicked(self):
        self.showFullScreen()
        self.maxWindow.setVisible(False)
        self.restoreWindow.setVisible(True)

    def oncloseWindowClicked(self):
        self.close()

    def onrestoreWindowClicked(self):
        self.showNormal()
        self.restoreWindow.setVisible(False)
        self.maxWindow.setVisible(True)

    def initTdTool(self):
        # 设置天地图工具
        self.tdMenu = QMenu()
        self.tdVector = QAction("天地图矢量")
        self.tdVector.setCheckable(True)
        self.tdImage = QAction("天地图影像")
        self.tdImage.setCheckable(True)
        self.tdTerrain = QAction("天地图地形")
        self.tdTerrain.setCheckable(True)
        self.tdMenu.addActions([self.tdVector, self.tdImage, self.tdTerrain])
        self.tdMenu.triggered.connect(self.ontdMenuClicked)
        self.tdMap.setMenu(self.tdMenu)

    def initMap(self):
        # 初始化地图
        self.mapProject = QgsProject.instance()
        self.setCentralWidget(self.mapCanvas)
        self.mapBridge = QgsLayerTreeMapCanvasBridge(self.mapProject.layerTreeRoot(), self.mapCanvas)
        self.mapCanvas.enableAntiAliasing(True)
        self.mapCanvas.setCanvasColor(Qt.white)
        self.mapSettings = self.mapCanvas.mapSettings()
        self.mapCrs = QgsCoordinateReferenceSystem.fromEpsgId(3857)
        self.mapSettings.setDestinationCrs(self.mapCrs)
        self.mapProject.addMapLayer(self.baseLayer)
        self.mapProject.addMapLayer(self.bjLayer)
        self.bjLayer.loadSldStyle("./map/范围.sld")
        self.mapProject.addMapLayer(self.zkdLayer)
        self.zkdLayer.loadSldStyle("./map/钻孔控制点.sld")

    def loadLayers(self):
        # 天地图影像
        imgUrl = 'http://t0.tianditu.gov.cn/img_w/wmts?service=wmts&request=GetTile&version=1.0.0&LAYER=img' \
                 '&tileMatrixSet=w&TileMatrix={z}&TileRow={y}&TileCol={' \
                 'x}&style=default&format=tiles&tk=b6faeac9c8ffc904c7d4ae6098468bb1&zmax=18&zmin=0'
        imgUrl_ = quote(imgUrl)
        self.imgTd = QgsRasterLayer("type=xyz&url={}".format(imgUrl_), "imgTd", "wms")
        imgAnnotationUrl = 'http://t0.tianditu.gov.cn/cia_w/wmts?service=wmts&request=GetTile&version=1.0.0&LAYER=cia' \
                           '&tileMatrixSet=w&TileMatrix={z}&TileRow={y}&TileCol={' \
                           'x}&style=default&format=tiles&tk=b6faeac9c8ffc904c7d4ae6098468bb1&zmax=18&zmin=0 '
        imgAnnotationUrl_ = quote(imgAnnotationUrl)
        self.imgAnnotationTd = QgsRasterLayer("type=xyz&url={}".format(imgAnnotationUrl_), "imgAnnotationTd", "wms")
        # 天地图矢量
        vectorUrl = 'https://t3.tianditu.gov.cn/vec_w/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=vec&STYLE' \
                    '=default&TILEMATRIXSET=w&FORMAT=tiles&TileMatrix={z}&TileRow={y}&TileCol={' \
                    'x}&tk=b6faeac9c8ffc904c7d4ae6098468bb1&zmax=18&zmin=0'
        vectorUrl_ = quote(vectorUrl)
        self.vectorTd = QgsRasterLayer("type=xyz&url={}".format(vectorUrl_), "vecotrTd", "wms")
        vectorAnnotationUrl = 'http://t0.tianditu.gov.cn/cva_w/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=cva' \
                              '&STYLE=default&TILEMATRIXSET=w&FORMAT=tiles&TileMatrix={z}&TileRow={y}&TileCol={' \
                              'x}&tk=b6faeac9c8ffc904c7d4ae6098468bb1&zmax=18&zmin=0'
        vectorAnnotationUrl_ = quote(vectorAnnotationUrl)
        self.vectorAnnotationTd = QgsRasterLayer("type=xyz&url={}".format(vectorAnnotationUrl_), "vectorAnnotationTd",
                                                 "wms")
        # 天地图地形
        terrainUrl = 'http://t0.tianditu.gov.cn/ter_w/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=ter&STYLE' \
                     '=default&TILEMATRIXSET=w&FORMAT=tiles&TileMatrix={z}&TileRow={y}&TileCol={' \
                     'x}&tk=b6faeac9c8ffc904c7d4ae6098468bb1&zmax=18&zmin=0 '
        terrainUrl_ = quote(terrainUrl)
        self.terrainTd = QgsRasterLayer("type=xyz&url={}".format(terrainUrl_), "terrainTd", "wms")
        terrainAnnotationUrl = 'http://t0.tianditu.gov.cn/cta_w/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=cta' \
                               '&STYLE=default&TILEMATRIXSET=w&FORMAT=tiles&TileMatrix={z}&TileRow={y}&TileCol={' \
                               'x}&tk=b6faeac9c8ffc904c7d4ae6098468bb1&zmax=18&zmin=0'

        terrainAnnotationUrl_ = quote(terrainAnnotationUrl)
        self.terrainAnnotationTd = QgsRasterLayer("type=xyz&url={}".format(terrainAnnotationUrl_),
                                                  "terrainAnnotationTd",
                                                  "wms")
        self.bjLayer = QgsVectorLayer("./map/范围.shp", "范围边界4326", "ogr")
        # 底图
        self.baseLayer = QgsRasterLayer(
            "url='http://map.geoq.cn/arcgis/rest/services/ChinaOnlineCommunity/MapServer' layer='0'",
            "baseLayer", "arcgismapserver")
        self.zkdLayer = QgsVectorLayer("./map/钻孔控制点.shp", "钻孔控制点", "ogr")

    def initToc(self):
        # 创建地图图层控件
        self.lyrTreeRoot = self.mapProject.layerTreeRoot()
        self.lyrTreeModel = QgsLayerTreeModel(self.lyrTreeRoot)
        self.lyrTreeModel.setFlag(QgsLayerTreeModel.AllowNodeReorder)
        self.lyrTreeModel.setFlag(QgsLayerTreeModel.AllowNodeChangeVisibility)
        self.lyrTreeModel.setFlag(QgsLayerTreeModel.ShowLegendAsTree)
        self.lyrTreeView = QgsLayerTreeView()
        self.lyrTreeView.setModel(self.lyrTreeModel)
        self.mapToc = QgsDockWidget(self)
        self.mapToc.setWidget(self.lyrTreeView)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.mapToc)
        self.tocBar.setCheckable(True)
        self.tocBar.setChecked(True)
        self.tocBar.trigger()

    def ontabToolbarActionClicked(self, tabTool: QAction):
        if tabTool.objectName() == 'normaltab':
            self.normalToolbar.setHidden(False)
            self.infoToolbar.setHidden(True)
        elif tabTool.objectName() == 'infotab':
            self.normalToolbar.setHidden(True)
            self.infoToolbar.setHidden(False)
        else:
            if tabTool.isChecked():
                self.mapToc.setHidden(False)
            else:
                self.mapToc.setHidden(True)

    def onnormalToolbarActionClicked(self, normalTool: QAction):
        toolText = normalTool.text()
        if toolText == "默认":
            self.mapCanvas.unsetMapTool(self.mapCanvas.mapTool())
        elif toolText == "放大":
            self.mapTool = QgsMapToolZoom(self.mapCanvas, False)
            self.mapCanvas.setMapTool(self.mapTool)
        elif toolText == "缩小":
            self.mapTool = QgsMapToolZoom(self.mapCanvas, True)
            self.mapCanvas.setMapTool(self.mapTool)
        elif toolText == "漫游":
            self.mapTool = QgsMapToolPan(self.mapCanvas)
            self.mapCanvas.setMapTool(self.mapTool)
        elif toolText == "前一视图":
            self.mapCanvas.zoomToPreviousExtent()
        elif toolText == "后一视图":
            self.mapCanvas.zoomToNextExtent()
        elif toolText == "全局视图":
            bjExtent = self.bjLayer.extent()
            self.mapCanvas.setExtent(bjExtent)
            self.mapCanvas.refresh()
        elif toolText == "天地图":
            cursorPos = QCursor().pos()
            cursorX = cursorPos.x()
            cursorY = cursorPos.y()
            self.tdMenu.show()
            self.tdMenu.move(cursorX, cursorY)
        else:
            pass

    def ontdMenuClicked(self, tdMenuAction: QAction):
        # 修改天地图底图
        txt = tdMenuAction.text()
        if txt == "天地图地形":
            if self.tdImage.isChecked():
                self.tdImage.setChecked(False)
                self.mapProject.layerTreeRoot().removeLayer(self.imgAnnotationTd)
                self.mapProject.layerTreeRoot().removeLayer(self.imgTd)
            if self.tdVector.isChecked():
                self.tdVector.setChecked(False)
                self.mapProject.layerTreeRoot().removeLayer(self.vectorTd)
                self.mapProject.layerTreeRoot().removeLayer(self.vectorAnnotationTd)
            if tdMenuAction.isChecked():
                self.mapProject.layerTreeRoot().insertLayer(2, self.terrainTd)
                self.mapProject.layerTreeRoot().insertLayer(2, self.terrainAnnotationTd)
            else:
                self.mapProject.layerTreeRoot().removeLayer(self.terrainTd)
                self.mapProject.layerTreeRoot().removeLayer(self.terrainAnnotationTd)
        elif txt == "天地图矢量":
            if self.tdTerrain.isChecked():
                self.tdTerrain.setChecked(False)
                self.mapProject.layerTreeRoot().removeLayer(self.terrainTd)
                self.mapProject.layerTreeRoot().removeLayer(self.terrainAnnotationTd)
            if self.tdImage.isChecked():
                self.tdImage.setChecked(False)
                self.mapProject.layerTreeRoot().removeLayer(self.imgTd)
                self.mapProject.layerTreeRoot().removeLayer(self.imgAnnotationTd)
            if tdMenuAction.isChecked():
                self.mapProject.layerTreeRoot().insertLayer(2, self.vectorTd)
                self.mapProject.layerTreeRoot().insertLayer(2, self.vectorAnnotationTd)
            else:
                self.mapProject.layerTreeRoot().removeLayer(self.vectorTd)
                self.mapProject.layerTreeRoot().removeLayer(self.vectorAnnotationTd)
        else:
            if self.tdTerrain.isChecked():
                self.tdTerrain.setChecked(False)
                self.mapProject.layerTreeRoot().removeLayer(self.terrainTd)
                self.mapProject.layerTreeRoot().removeLayer(self.terrainAnnotationTd)
            if self.tdVector.isChecked():
                self.tdVector.setChecked(False)
                self.mapProject.layerTreeRoot().removeLayer(self.vectorTd)
                self.mapProject.layerTreeRoot().removeLayer(self.vectorAnnotationTd)
            if tdMenuAction.isChecked():
                self.mapProject.layerTreeRoot().insertLayer(2, self.imgTd)
                self.mapProject.layerTreeRoot().insertLayer(2, self.imgAnnotationTd)
            else:
                self.mapProject.layerTreeRoot().removeLayer(self.imgAnnotationTd)
                self.mapProject.layerTreeRoot().removeLayer(self.imgTd)

    def ondcjgClicked(self):
        self.dcjgcx = DCJGCX(self.mdb, self)
        self.dcjgcx.show()

    def onjydzdClicked(self):
        self.jydzcx = JYDZCX(self.mdb, self)
        self.jydzcx.show()

    def ondbdzdClicked(self):
        self.dbdzcx = DBDZCX(self.mdb, self)
        self.dbdzcx.show()

    def onjgcxClicked(self):
        self.jgcxw = JGCX(self.mdb, self)
        self.jgcxw.show()

    def ondzzhClicked(self):
        self.dzzhcx = DZZH(self.mdb, self)
        self.dzzhcx.show()

    def zoomToZK(self, zkno):
        self.zkdLayer.removeSelection()
        zkexp = QgsExpression("钻孔='{}'".format(zkno))
        zkreq = QgsFeatureRequest(zkexp)
        zks = self.zkdLayer.getFeatures(zkreq)
        for zk in zks:
            # self.mapCanvas.zoomToFeatureIds(self.zkdLayer, [zk.id()])
            self.zkdLayer.select(zk.id())
            self.mapCanvas.zoomToSelected(self.zkdLayer)
            break

    def firstload(self):
        self.mapCanvas.setExtent(self.bjLayer.extent())
        self.mapCanvas.refresh()


class MySignal(QObject):
    signal = pyqtSignal()


def firstload(mysignal: MySignal):
    time.sleep(0.5)
    mysignal.signal.emit()


if __name__ == '__main__':
    QgsApplication.setPrefixPath('qgis', True)
    app = QgsApplication([], True)
    dirname = os.path.dirname(__file__)
    pluginPath = os.path.join(dirname, 'qgis', 'plugins')
    app.setPluginPath(pluginPath)
    app.initQgis()
    qtpluginPath = os.path.join(dirname, 'PyQt5', 'Qt', 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = qtpluginPath
    mdb = os.path.join(dirname, 'anping.mdb')
    appWindow = AppMainWindow(mdb)
    # 清理临时目录中的文件
    tempFiles = os.listdir("./temp")
    for tempFile in tempFiles:
        os.remove("./temp/{}".format(tempFile))
    appWindow.show()
    firstLoad = MySignal()
    firstLoad.signal.connect(appWindow.firstload)
    t = threading.Thread(target=firstload, args=(firstLoad,))
    t.start()
    app.exec_()
    app.exitQgis()
    QgsVectorLayer()
