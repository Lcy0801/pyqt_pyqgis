import sys
import os
from qgis.PyQt.QtWidgets import (
    QApplication,
    QWidget,
    QMessageBox,
    QTableWidgetItem,
    QAbstractItemView
)
from qgis.PyQt.QtGui import QPixmap
from qgis.PyQt.QtCore import Qt
from qgis.core import QgsVectorLayer, QgsCoordinateReferenceSystem
from qgis import processing

from dbdzcx_ui import Ui_Form
from mdb import mdb_conn


class DBDZCX(QWidget, Ui_Form):
    def __init__(self, mdb, mainWindow):
        super(QWidget, self).__init__()
        self.setupUi(self)
        self.mdb = mdb
        self.mainWindow = mainWindow
        self.loadgl()
        self.loadfw()
        self.escButton.clicked.connect(self.onescButtonClicked)
        self.queryButton.clicked.connect(self.onqueryButtonClicked)
        self.queryTabel.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.mainWindow.fypLayer = None
        self.queryTabel.setStyleSheet("selection-background-color:rgb(255,209,128)")

    def loadgl(self):
        self.conn = mdb_conn(self.mdb)
        if self.conn == None:
            QMessageBox.critical(self, "错误", "无法连接到数据库{}".format(self.mdb), QMessageBox.Yes, QMessageBox.Yes)
            return
        sql = "select distinct 超越概率 from dibiaodizhendong"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        gls = cursor.fetchall()
        for gl in gls:
            self.glcomboBox.addItem(gl[0])
        self.conn.close()

    def loadfw(self):
        self.conn = mdb_conn(self.mdb)
        if self.conn == None:
            QMessageBox.critical(self, "错误", "无法连接到数据库{}".format(self.mdb), QMessageBox.Yes, QMessageBox.Yes)
            return
        sql = "select distinct 钻孔编号 from dibiaodizhendong"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        zks = cursor.fetchall()
        for zk in zks:
            zkno = zk[0][2:]
            zkno = int(zkno)
            self.fwcomboBox.insertItem(zkno - 1, zk[0])
        self.fwcomboBox.addItem("目标区")
        self.conn.close()

    def onescButtonClicked(self):
        if self.mainWindow.fypLayer:
            self.mainWindow.mapProject.layerTreeRoot().removeLayer(self.mainWindow.fypLayer)
        self.close()

    def onqueryButtonClicked(self):
        glindex = self.glcomboBox.currentIndex()
        fwindex = self.fwcomboBox.currentIndex()
        if glindex == -1 or fwindex == -1:
            QMessageBox.warning(self, "警告", "请先设置“超越概率”参数和“范围”参数！", QMessageBox.Yes, QMessageBox.Yes)
            return
        self.conn = mdb_conn(self.mdb)
        if self.conn == None:
            QMessageBox.critical(self, "错误", "无法连接到数据库{}".format(self.mdb), QMessageBox.Yes, QMessageBox.Yes)
            return
        gl = self.glcomboBox.currentText()
        fw = self.fwcomboBox.currentText()
        sql = "select * from dibiaodizhendong where 钻孔编号='{}' and 超越概率='{}'".format(fw, gl)
        cursor = self.conn.cursor()
        cursor.execute(sql)
        datas = cursor.fetchall()
        self.queryTabel.setColumnCount(9)
        self.queryTabel.setHorizontalHeaderLabels(
            ['OBJECTID', '钻孔编号', '超越概率', 'Amax_gal_', 'bm', 'Field5', 'T1__sec_', 'Tg__sec_', 'g'])
        num = len(datas)
        self.queryTabel.setRowCount(num)
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
            self.queryTabel.setItem(n, 0, zkid)
            self.queryTabel.setItem(n, 1, zkno)
            self.queryTabel.setItem(n, 2, glit)
            self.queryTabel.setItem(n, 3, Amax_gal_)
            self.queryTabel.setItem(n, 4, bm)
            self.queryTabel.setItem(n, 5, Field5)
            self.queryTabel.setItem(n, 6, T1__sec_)
            self.queryTabel.setItem(n, 7, Tg__sec_)
            self.queryTabel.setItem(n, 8, git)
            n += 1
        self.conn.close()
        self.displayImg(fw, gl)
        if fw == "目标区":
            self.addShp(gl)

    def displayImg(self, fw, gl):
        imgFile = "./dbdzd/{}{}.jpg".format(fw, gl)
        imgFilePix = QPixmap(imgFile)
        imgFilePix = imgFilePix.scaled(self.imgWindow.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        imgFilePix.save("dbdzd.jpg")
        self.imgWindow.setStyleSheet("background-image:url(dbdzd.jpg)")

    def addShp(self, gl: str):
        index = gl.index('年')
        glyear = gl[0:index]
        glvalue = gl[index + 1:-1]
        shpFile = './map/地表地震动/{}{}.shp'.format(glyear, glvalue)
        if self.mainWindow.fypLayer:
            self.mainWindow.mapProject.layerTreeRoot().removeLayer(self.mainWindow.fypLayer)
        self.mainWindow.fypLayer = QgsVectorLayer(shpFile, "{}_{}".format(glyear, glvalue), "ogr")
        self.mainWindow.mapProject.layerTreeRoot().insertLayer(0, self.mainWindow.fypLayer)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    appWindow = DBDZCX(r"C:\Users\user\Desktop\地质管理系统\ui\anping.mdb", None)
    appWindow.show()
    app.exec_()
