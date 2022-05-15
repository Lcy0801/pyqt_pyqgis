import sys
from qgis.PyQt.QtWidgets import (
    QApplication,
    QWidget,
    QMessageBox,
    QTableWidgetItem,
    QHeaderView,
    QAbstractItemView,
    QMainWindow)
from qgis.core import QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsProject, QgsPointXY
from qgis.PyQt.QtGui import QPixmap, QBrush, QIcon
from qgis.PyQt.QtCore import Qt, QRect
from dcjgcx_ui import Ui_Form
from mdb import mdb_conn


class DCJGCX(QWidget, Ui_Form):
    def __init__(self, mdb, mainWindow):
        super(QWidget, self).__init__()
        self.setupUi(self)
        self.loadData(mdb)
        self.mainWindow = mainWindow
        self.zkNoList.currentTextChanged.connect(self.onzkNoListcurrentTextChanged)
        self.zkTable.setStyleSheet("selection-background-color:rgb(255,209,128)")
        self.zkQuery.clicked.connect(self.onzkQueryClicked)
        self.viewZKBar.clicked.connect(self.onviewZKBarClicked)
        self.zkEsc.clicked.connect(self.onzkEscClicked)
        self.zkTable.currentItemChanged.connect(self.onzkTableCurrentItemChanged)


    def loadData(self, mdb):
        self.conn = mdb_conn(mdb)
        if self.conn == None:
            QMessageBox.critical(self, "错误", "无法连接到数据库{}!".format(mdb), QMessageBox.Yes, QMessageBox.Yes)
            return
        sqlstr = "select count(*) from zuankong"
        cursor = self.conn.cursor()
        cursor.execute(sqlstr)
        zksdata = cursor.fetchone()
        zknum = zksdata[0]
        self.zkTable.setColumnCount(6)
        self.zkTable.setHorizontalHeaderLabels(['ID', "钻孔编号", "经度E_°", "维度_°", "高程_m", "孔深_m"])
        self.zkTable.setRowCount(zknum)
        QHeaderView.setSectionResizeMode(self.zkTable.horizontalHeader(), QHeaderView.Stretch)
        self.zkTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        sqlstr = "select * from zuankong order by OBJECTID"
        cursor = self.conn.cursor()
        cursor.execute(sqlstr)
        zksdata = cursor.fetchall()
        n = 0
        for zk in zksdata:
            # zktable
            zkid = QTableWidgetItem(str(zk[0]))
            zkid.setTextAlignment(Qt.AlignCenter)
            zkno = QTableWidgetItem(str(zk[1]))
            zkno.setTextAlignment(Qt.AlignCenter)
            zklon = QTableWidgetItem(str(zk[2]))
            zklon.setTextAlignment(Qt.AlignCenter)
            zklat = QTableWidgetItem(str(zk[3]))
            zklat.setTextAlignment(Qt.AlignCenter)
            zkh = QTableWidgetItem(str(zk[4]))
            zkh.setTextAlignment(Qt.AlignCenter)
            zkdepth = QTableWidgetItem(str(zk[5]))
            zkdepth.setTextAlignment(Qt.AlignCenter)
            self.zkTable.setItem(n, 0, zkid)
            self.zkTable.setItem(n, 1, zkno)
            self.zkTable.setItem(n, 2, zklon)
            self.zkTable.setItem(n, 3, zklat)
            self.zkTable.setItem(n, 4, zkh)
            self.zkTable.setItem(n, 5, zkdepth)
            # zknolist
            self.zkNoList.addItem(zk[1])
            n += 1
        self.conn.close()

    def onzkNoListcurrentTextChanged(self, currentText):
        zknum = self.zkTable.rowCount()
        for row in range(zknum):
            zknoItem = self.zkTable.item(row, 1)
            zkno = zknoItem.text()
            if zkno == currentText:
                self.zkTable.selectRow(row)
                break

    def onzkQueryClicked(self):
        self.zkTable.clearSelection()
        zknoInput = self.zkNoLineEdite.text()
        if zknoInput == "":
            QMessageBox.warning(self, "提示", "请输入要查询的转孔编号，再点击查询按钮!", QMessageBox.Yes, QMessageBox.Yes)
            return
        zknum = self.zkTable.rowCount()
        flag = False
        for row in range(zknum):
            zknoItem = self.zkTable.item(row, 1)
            zkno = zknoItem.text()
            if zkno == zknoInput:
                self.zkTable.selectRow(row)
                flag = True
                break
        if flag == False:
            QMessageBox.information(self, "查找结果", "根据输入的钻孔编码在数据库中没有查询到相关记录！", QMessageBox.Yes, QMessageBox.Yes)
        print(self.zkTable.currentRow())

    def onviewZKBarClicked(self):
        row = self.zkTable.currentRow()
        zknoItem = self.zkTable.item(row, 1)
        zkno = zknoItem.text()
        zkimgFile = "./zzt/{}.jpg".format(zkno)
        self.zkPixmap = QPixmap(zkimgFile)
        self.imgWindow = QMainWindow()
        self.imgWindow.setFixedSize(600, 840)
        self.imgWindow.setWindowIcon(QIcon("./icons/钻孔.png"))
        self.imgWindow.setWindowTitle("钻孔柱状图:{}".format(zkno))
        palette = self.imgWindow.palette()
        palette.setBrush(self.imgWindow.backgroundRole(), QBrush(
            self.zkPixmap.scaled(self.imgWindow.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
        self.imgWindow.setPalette(palette)
        self.imgWindow.show()

    def onzkTableCurrentItemChanged(self, cItem, pItem):
        crow = cItem.row()
        zknoItem = self.zkTable.item(crow, 1)
        zkno = zknoItem.text()
        self.mainWindow.zoomToZK(zkno)

    def onzkEscClicked(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dcjgcx = DCJGCX(r"C:\Users\user\Desktop\地质管理系统\ui\anping.mdb", None)
    dcjgcx.show()
    app.exec_()
