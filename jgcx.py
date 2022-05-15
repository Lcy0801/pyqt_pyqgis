import sys
import os
from qgis.PyQt.QtWidgets import (
    QApplication,
    QWidget,
    QMessageBox,
    QTableWidgetItem,
    QAbstractItemView)
from qgis.PyQt.QtCore import Qt, QVariant
from qgis.core import (
    QgsFeature,
    QgsPointXY,
    QgsGeometry,
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
    QgsFields,
    QgsField,
    QgsVectorFileWriter,
    QgsWkbTypes,
    QgsVectorLayer)
from jgcx_ui import Ui_Form
from geopy import distance
from mdb import mdb_conn
import re
import time


def dist(lat1, lon1, lat2, lon2):
    poi1 = (lat1, lon1)
    poi2 = (lat2, lon2)
    return distance.distance(poi1, poi2).meters


class JGCX(QWidget, Ui_Form):
    def __init__(self, mdb, mainWindow):
        super(QWidget, self).__init__()
        self.setupUi(self)
        self.mdb = mdb
        self.mainWindow = mainWindow
        self.loadzks()
        self.escButton.clicked.connect(self.onescButtonClicked)
        self.queryButton.clicked.connect(self.onqueryButtonClicked)
        self.lonlineEdit.setPlaceholderText("十进制度")
        self.latlineEdit.setPlaceholderText("十进制度")
        self.queryTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.queryTable.setStyleSheet("selection-background-color:rgb(255,209,128)")
        self.bufferLayer = None
        self.setWindowTitle("结果查询")

    def loadzks(self):
        self.conn = mdb_conn(self.mdb)
        if self.conn == None:
            QMessageBox.critical(self, "错误", "无法连接到数据库{}!".format(self.mdb), QMessageBox.Yes, QMessageBox.Yes)
            return
        sql = 'select 钻孔编号,经度E_°,纬度N_° from zuankong'
        cursor = self.conn.cursor()
        cursor.execute(sql)
        zks = cursor.fetchall()
        self.zks = []
        for zk in zks:
            self.zks.append(zk)
        self.conn.close()

    def onescButtonClicked(self):
        if self.bufferLayer:
            self.mainWindow.mapProject.layerTreeRoot().removeLayer(self.bufferLayer)
        self.close()

    def onqueryButtonClicked(self):
        lon = self.lonlineEdit.text()
        lat = self.latlineEdit.text()
        radius = self.radiuslineEdit.text()
        radius = float(radius)
        patternStr = '^([0-9]|([+-]{1}[0-9]{1}))[0-9]*\.?([0-9]+$)'
        if re.match(patternStr, lon) == None:
            QMessageBox.critical(self, "错误", "经度输入不合法！", QMessageBox.Yes, QMessageBox.Yes)
            return
        if re.match(patternStr, lat) == None:
            QMessageBox.critical(self, "错误", "纬度输入不合法！", QMessageBox.Yes, QMessageBox.Yes)
            return
        lon = float(lon)
        lat = float(lat)
        if lon < -180 or lon > 180:
            QMessageBox.critical(self, "错误", "经度范围不合法！", QMessageBox.Yes, QMessageBox.Yes)
            return
        if lat < -90 or lat > 90:
            QMessageBox.critical(self, "错误", "纬度范围不合法！", QMessageBox.Yes, QMessageBox.Yes)
            return
        zknos = []
        for zk in self.zks:
            zklon = float(zk[1])
            zklat = float(zk[2])
            distvalue = dist(lat, lon, zklat, zklon)
            if distvalue <= radius:
                zknos.append("'{}'".format(zk[0]))
        if len(zknos) == 0:
            QMessageBox.Information(self, "查询结果", "查询结果为空！", QMessageBox.Yes, QMessageBox.Yes)
            return
        self.loadResult(zknos)
        self.loadBufferLayer(lon, lat, radius)

    def loadResult(self, zknos):
        zknos_ = ','.join(zknos)
        self.conn = mdb_conn(self.mdb)
        if self.conn == None:
            QMessageBox.critical(self, "错误", "无法连接到数据库{}!".format(self.mdb), QMessageBox.Yes, QMessageBox.Yes)
            return
        sql = 'select * from dibiaodizhendong where 钻孔编号 in ({})'.format(zknos_)
        cursor = self.conn.cursor()
        cursor.execute(sql)
        datas = cursor.fetchall()
        num = len(datas)
        self.queryTable.setColumnCount(9)
        self.queryTable.setHorizontalHeaderLabels(
            ['OBJECTID', '钻孔编号', '超越概率', 'Amax_gal_', 'bm', 'Field5', 'T1__sec_', 'Tg__sec_', 'g'])
        self.queryTable.setRowCount(num)
        n = 0
        for data in datas:
            zkid = QTableWidgetItem(str(data[0]))
            zkid.setTextAlignment(Qt.AlignCenter)
            zkno = QTableWidgetItem(str(data[1]))
            zkno.setTextAlignment(Qt.AlignCenter)
            glit = QTableWidgetItem(str(data[2]))
            glit.setTextAlignment(Qt.AlignCenter)
            Amax_gal_ = QTableWidgetItem(str(data[3]))
            Amax_gal_.setTextAlignment(Qt.AlignCenter)
            bm = QTableWidgetItem(str(data[4]))
            bm.setTextAlignment(Qt.AlignCenter)
            Field5 = QTableWidgetItem(str(data[5]))
            Field5.setTextAlignment(Qt.AlignCenter)
            T1__sec_ = QTableWidgetItem(str(data[6]))
            T1__sec_.setTextAlignment(Qt.AlignCenter)
            Tg__sec_ = QTableWidgetItem(str(data[7]))
            Tg__sec_.setTextAlignment(Qt.AlignCenter)
            git = QTableWidgetItem(str(data[8]))
            git.setTextAlignment(Qt.AlignCenter)
            self.queryTable.setItem(n, 0, zkid)
            self.queryTable.setItem(n, 1, zkno)
            self.queryTable.setItem(n, 2, glit)
            self.queryTable.setItem(n, 3, Amax_gal_)
            self.queryTable.setItem(n, 4, bm)
            self.queryTable.setItem(n, 5, Field5)
            self.queryTable.setItem(n, 6, T1__sec_)
            self.queryTable.setItem(n, 7, Tg__sec_)
            self.queryTable.setItem(n, 8, git)
            n += 1
        self.conn.close()

    def loadBufferLayer(self, lon, lat, radius):
        if self.bufferLayer:
            self.mainWindow.mapProject.layerTreeRoot().removeLayer(self.bufferLayer)
            self.bufferLayer = None
        crs4326 = QgsCoordinateReferenceSystem.fromEpsgId(4326)
        crs3857 = QgsCoordinateReferenceSystem.fromEpsgId(3857)
        xform = QgsCoordinateTransform(crs4326, crs3857, self.mainWindow.mapProject.transformContext())
        poi = QgsPointXY(lon, lat)
        poi_ = xform.transform(poi)
        poigeom = QgsGeometry.fromPointXY(poi_)
        buffergeom = poigeom.buffer(radius, 5)
        fields = QgsFields()
        fields.append(QgsField('经度', QVariant.Double))
        fields.append(QgsField('纬度', QVariant.Double))
        fields.append(QgsField('半径', QVariant.Double))
        save_options = QgsVectorFileWriter.SaveVectorOptions()
        save_options.driverName = "ESRI Shapefile"
        save_options.fileEncoding = "UTF-8"
        bufferShp = "./temp/{}.shp".format(int(time.time() * pow(10, 6)))
        writer = QgsVectorFileWriter.create(
            bufferShp,
            fields,
            QgsWkbTypes.Polygon,
            self.mainWindow.mapCrs,
            self.mainWindow.mapProject.transformContext(),
            save_options
        )
        bufferFea = QgsFeature()
        bufferFea.setGeometry(buffergeom)
        bufferFea.setFields(fields)
        bufferFea.setAttribute("经度", lon)
        bufferFea.setAttribute("纬度", lat)
        bufferFea.setAttribute("半径", radius)
        writer.addFeature(bufferFea)
        del writer
        self.bufferLayer = QgsVectorLayer(bufferShp, "查询缓冲区", "ogr")
        self.bufferLayer.loadSldStyle("./map/buffer.sld")
        self.mainWindow.mapProject.layerTreeRoot().insertLayer(2, self.bufferLayer)
        self.mainWindow.mapCanvas.setExtent(self.bufferLayer.extent())


if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    plugin_path = os.path.join(dirname, 'PyQt5', 'Qt5', 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    app = QApplication(sys.argv)
    appWindow = JGCX(r'C:\Users\user\Desktop\地质管理系统\ui\anping.mdb', None)
    appWindow.show()
    app.exec_()
